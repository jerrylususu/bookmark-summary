#!/usr/bin/env python3
"""
关键词搜索工具
搜索文件名和文件内容
"""

import os
import subprocess
from typing import List, Dict, Any

def keyword_search(query: str, max_results: int = 10) -> Dict[str, Any]:
    """
    关键词搜索

    Args:
        query: 搜索词
        max_results: 最大结果数

    Returns:
        搜索结果字典
    """
    try:
        # 切换到项目根目录
        project_root = "/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary"
        os.chdir(project_root)

        # 使用 grep 搜索
        cmd = ["grep", "-rn", "--max-count", str(max_results), query, "."]
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            results = []

            for line in lines:
                if ':' in line:
                    parts = line.split(':', 2)
                    if len(parts) >= 3:
                        file_path = parts[0]
                        line_num = int(parts[1])
                        content = parts[2]
                        results.append({
                            "file_path": file_path,
                            "line_number": line_num,
                            "content": content.strip(),
                            "context": f"{file_path}:{line_num}"
                        })

            return {
                "success": True,
                "query": query,
                "results_count": len(results),
                "results": results
            }
        else:
            return {
                "success": True,
                "query": query,
                "results_count": 0,
                "results": [],
                "message": "未找到匹配结果"
            }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "query": query,
            "results_count": 0,
            "results": []
        }

if __name__ == "__main__":
    # 测试代码
    import json
    result = keyword_search("embedding", 5)
    print(json.dumps(result, indent=2, ensure_ascii=False))