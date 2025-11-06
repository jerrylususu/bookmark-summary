#!/usr/bin/env python3
"""
向量搜索工具
基于现有的 embeddings.sqlite 进行语义检索
"""

import sys
import os
import numpy as np
from typing import List, Dict, Any, Optional
from pathlib import Path

# 添加父目录到 Python 路径以导入 embedding_store 和 embedding_pipeline
sys.path.append("/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary")

try:
    from embedding_store import EmbeddingStore
    from embedding_pipeline import EmbeddingClient, load_embedding_config
    EMBEDDING_AVAILABLE = True
except ImportError as e:
    print(f"Import warning: {e}")
    print("embedding modules not available, using fallback search")
    EMBEDDING_AVAILABLE = False

def vector_search(query: str, top_k: int = 5, chunk_types: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    向量搜索

    Args:
        query: 查询文本
        top_k: 返回结果数量，最大10
        chunk_types: 指定搜索的 chunk 类型，如 ['summary', 'content']

    Returns:
        搜索结果字典
    """
    try:
        # 限制 top_k
        top_k = min(top_k, 10)

        # 设置数据库路径
        db_path = Path("/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/embeddings.sqlite")
        if not db_path.exists():
            return {
                "success": False,
                "error": "Embeddings database not found",
                "query": query,
                "results_count": 0,
                "results": []
            }

        # 初始化 embedding store
        store = EmbeddingStore(db_path)

        if not EMBEDDING_AVAILABLE:
            raise RuntimeError("embedding modules not available for vector search")

        # 加载 embedding 客户端
        env_path = Path("/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/.env")
        config = load_embedding_config(env_path)
        client = EmbeddingClient(config)

        # 生成查询向量
        query_embeddings = client.embed([query])
        query_embedding = np.array(query_embeddings[0], dtype=np.float32)

        # 构建查询
        if chunk_types:
            placeholders = ",".join(["?" for _ in chunk_types])
            chunk_filter = f"AND chunk_type IN ({placeholders})"
            params = chunk_types + [query_embedding.size]
        else:
            chunk_filter = ""
            params = [query_embedding.size]

        # 执行向量相似度搜索
        query_sql = f"""
            SELECT
                c.document_id,
                c.chunk_type,
                c.chunk_index,
                c.heading,
                c.content,
                d.title,
                d.url,
                d.month,
                c.embedding
            FROM chunks c
            JOIN documents d ON c.document_id = d.document_id
            WHERE c.dimension = ? {chunk_filter}
        """

        cursor = store.connection.execute(query_sql, params)
        rows = cursor.fetchall()

        if not rows:
            store.close()
            return {
                "success": True,
                "query": query,
                "results_count": 0,
                "results": [],
                "message": "未找到匹配的向量"
            }

        # 计算相似度
        results = []
        for row in rows:
            # 解码向量
            embedding_bytes = row['embedding']
            embedding = np.frombuffer(embedding_bytes, dtype=np.float32)

            # 计算余弦相似度
            similarity = np.dot(query_embedding, embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(embedding)
            )

            results.append({
                "document_id": row['document_id'],
                "chunk_type": row['chunk_type'],
                "chunk_index": row['chunk_index'],
                "heading": row['heading'],
                "content": row['content'][:500] + "..." if len(row['content']) > 500 else row['content'],
                "title": row['title'],
                "url": row['url'],
                "month": row['month'],
                "similarity": float(similarity),
                "context": f"{row['document_id']} ({row['chunk_type']})"
            })

        # 按相似度排序并取前 top_k
        results.sort(key=lambda x: x['similarity'], reverse=True)
        results = results[:top_k]

        store.close()
        if 'client' in locals():
            client.close()

        return {
            "success": True,
            "query": query,
            "results_count": len(results),
            "results": results
        }

    except Exception as e:
        # 确保资源被正确释放
        if 'store' in locals():
            try:
                store.close()
            except:
                pass
        if 'client' in locals():
            try:
                client.close()
            except:
                pass

        raise

if __name__ == "__main__":
    # 测试代码
    import json
    result = vector_search("LLM embedding", 3)
    print(json.dumps(result, indent=2, ensure_ascii=False))