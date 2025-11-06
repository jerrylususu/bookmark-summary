#!/usr/bin/env python3
"""
核心代理逻辑
维护对话历史、工具选择和调用循环、答案生成和总结
"""

import json
import sys
import os
from typing import List, Dict, Any, Optional
from datetime import datetime

# 添加工具目录到 Python 路径
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'tools'))
# 添加父目录到 Python 路径以导入 embedding_pipeline
sys.path.append("/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary")

try:
    from embedding_pipeline import TokenSplitter
    TOKENIZER_AVAILABLE = True
except ImportError as e:
    print(f"Tokenizer import warning: {e}")
    TOKENIZER_AVAILABLE = False

try:
    from keyword_search import keyword_search
    from vector_search import vector_search
    from text_reader import text_reader
except ImportError as e:
    print(f"Import error: {e}")

try:
    from llm_client import get_llm_client
    LLM_AVAILABLE = True
except ImportError as e:
    print(f"LLM client import warning: {e}")
    LLM_AVAILABLE = False

class AgenticAgent:
    def __init__(self):
        self.conversation_history = []
        self.tool_calls = []
        self.max_tool_calls = 10
        self.max_tokens = 60000
        self.current_tokens = 0

        # 初始化tokenizer（与embedding_pipeline.py保持一致）
        if TOKENIZER_AVAILABLE:
            self.tokenizer = TokenSplitter(encoding_name="cl100k_base")
        else:
            self.tokenizer = None

        # 初始化LLM客户端
        if not LLM_AVAILABLE:
            raise RuntimeError("LLM不可用，无法启动代理")

        try:
            self.llm_client = get_llm_client()
            self.use_llm = True
            print("✅ LLM客户端初始化成功")
        except Exception as e:
            raise RuntimeError(f"LLM客户端初始化失败: {e}")

    def add_message(self, role: str, content: str):
        """添加消息到对话历史"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        self.conversation_history.append(message)

    def estimate_tokens(self, text: str) -> int:
        """使用与embedding_pipeline.py一致的tokenizer估算token数量"""
        if self.tokenizer:
            return self.tokenizer.count(text)
        else:
            # 回退到简单的字符数/4估算
            return max(1, len(text) // 4)

    def check_token_limit(self, new_content: str) -> bool:
        """检查是否超过 token 限制"""
        estimated_tokens = self.estimate_tokens(new_content)
        return (self.current_tokens + estimated_tokens) < self.max_tokens

    def choose_tool(self, query: str, previous_results: List[Dict]) -> Optional[Dict[str, Any]]:
        """
        根据当前情况选择工具

        Returns:
            tool_call dict 或 None
        """
        # 如果启用LLM，使用LLM进行工具选择
        if self.use_llm and self.llm_client:
            available_tools = ["keyword_search", "vector_search", "text_reader"]
            try:
                llm_decision = self.llm_client.choose_tool(
                    query, available_tools, previous_results, self.conversation_history
                )
                if llm_decision:
                    print(f"🤖 LLM选择工具: {llm_decision['tool']} (native tool calling)")
                    return {
                        "tool": llm_decision["tool"],
                        "params": llm_decision["params"]
                    }
                else:
                    print("🤖 LLM认为搜索已完成")
                    return None
            except Exception as e:
                print(f"❌ LLM工具选择失败: {e}")
                raise ValueError(f"LLM工具选择失败: {e}")

        # 这个方法在LLM模式下不应该被调用
        raise RuntimeError("在LLM模式下，工具选择应该完全由LLM处理，不应到达这里的回退逻辑")

    def execute_tool(self, tool_call: Dict[str, Any]) -> Dict[str, Any]:
        """执行工具调用"""
        tool_name = tool_call["tool"]
        params = tool_call["params"]

        try:
            if tool_name == "keyword_search":
                result = keyword_search(**params)
            elif tool_name == "vector_search":
                result = vector_search(**params)
            elif tool_name == "text_reader":
                result = text_reader(**params)
            else:
                result = {
                    "success": False,
                    "error": f"Unknown tool: {tool_name}"
                }

            # 记录工具调用
            call_record = {
                "tool": tool_name,
                "params": params,
                "result": result,
                "timestamp": datetime.now().isoformat()
            }
            self.tool_calls.append(call_record)

            # 在结果中添加工具使用信息，供LLM决策参考
            result["tool_used"] = tool_name

            return result

        except Exception as e:
            error_result = {
                "success": False,
                "error": str(e),
                "tool": tool_name,
                "params": params,
                "tool_used": tool_name  # 添加工具使用信息
            }
            self.tool_calls.append({
                "tool": tool_name,
                "params": params,
                "result": error_result,
                "timestamp": datetime.now().isoformat()
            })
            return error_result

    def should_continue_search(self) -> bool:
        """判断是否应该继续搜索"""
        if len(self.tool_calls) >= self.max_tool_calls:
            return False

        # 如果最近几次搜索都没有结果，停止搜索
        recent_failures = sum(1 for call in self.tool_calls[-3:]
                            if not call["result"].get("success") or
                               not call["result"].get("results"))
        if recent_failures >= 2:
            return False

        return True

    def generate_answer(self, query: str) -> Dict[str, Any]:
        """生成最终答案"""
        # 收集所有有用信息
        all_results = []
        search_results_with_tools = []

        for call in self.tool_calls:
            result = call["result"]
            if result.get("success") and result.get("results"):
                all_results.extend(result["results"])
                # 为LLM准备包含工具信息的结果
                search_results_with_tools.append({
                    "tool_name": call["tool"],
                    "success": result.get("success", False),
                    "results": result.get("results", [])
                })

        # 如果启用LLM且结果不为空，使用LLM生成答案
        if self.use_llm and self.llm_client and search_results_with_tools:
            try:
                print("🤖 使用LLM生成答案...")
                llm_answer = self.llm_client.generate_answer(query, search_results_with_tools)
                print("✅ LLM答案生成完成")

                # 生成来源列表
                sources = []
                for call in self.tool_calls:
                    result = call["result"]
                    if result.get("success") and result.get("results"):
                        for item in result["results"]:
                            if item.get('file_path'):
                                sources.append(item['file_path'])
                            elif item.get('document_id'):
                                sources.append(item['document_id'])

                sources = list(set(sources))  # 去重

                return {
                    "success": True,
                    "answer": llm_answer,
                    "sources": sources,
                    "tool_calls_count": len(self.tool_calls),
                    "confidence": "high" if len(all_results) > 3 else "medium"
                }
            except Exception as e:
                print(f"❌ LLM答案生成失败: {e}")
                raise ValueError(f"LLM答案生成失败: {e}")

        # 如果没有搜索结果，返回空答案
        if not all_results:
            return {
                "success": True,
                "answer": f"很抱歉，没有找到与您的问题「{query}」相关的信息。",
                "sources": [],
                "tool_calls_count": len(self.tool_calls),
                "confidence": "low"
            }

        # 生成答案
        answer_parts = [f"根据搜索结果，关于「{query}」的回答如下：\n"]

        # 按工具类型分组整理结果
        keyword_results = []
        vector_results = []
        text_results = []

        for call in self.tool_calls:
            result = call["result"]
            if result.get("success") and result.get("results"):
                if call["tool"] == "keyword_search":
                    keyword_results.extend(result["results"])
                elif call["tool"] == "vector_search":
                    vector_results.extend(result["results"])
                elif call["tool"] == "text_reader":
                    text_results.append(result)

        # 添加向量搜索结果（语义相关）
        if vector_results:
            answer_parts.append("## 语义相关内容：")
            for i, result in enumerate(vector_results[:3]):
                answer_parts.append(f"{i+1}. **{result.get('title', '未知标题')}** ({result.get('month', '未知时间')})")
                if result.get('heading'):
                    answer_parts.append(f"   章节: {result['heading']}")
                answer_parts.append(f"   相似度: {result.get('similarity', 0):.3f}")
                answer_parts.append(f"   摘要: {result.get('content', '')[:200]}...")
                answer_parts.append("")

        # 添加关键词搜索结果
        if keyword_results:
            answer_parts.append("## 关键词匹配内容：")
            for i, result in enumerate(keyword_results[:3]):
                answer_parts.append(f"{i+1}. **文件**: {result.get('file_path', '')}")
                answer_parts.append(f"   位置: 第{result.get('line_number', 0)}行")
                answer_parts.append(f"   内容: {result.get('content', '')[:150]}...")
                answer_parts.append("")

        # 添加文本读取结果
        if text_results:
            answer_parts.append("## 详细内容：")
            for result in text_results[:2]:
                answer_parts.append(f"**文件**: {result.get('file_path', '')}")
                answer_parts.append(f"**行范围**: {result.get('start_line', 0)}-{result.get('end_line', 0)}")
                content = result.get('content', '')[:500]
                answer_parts.append(f"**内容预览**:\n```\n{content}\n```")
                answer_parts.append("")

        # 生成来源列表
        sources = []
        for call in self.tool_calls:
            result = call["result"]
            if result.get("success") and result.get("results"):
                for item in result["results"]:
                    if item.get('file_path'):
                        sources.append(item['file_path'])
                    elif item.get('document_id'):
                        sources.append(item['document_id'])

        sources = list(set(sources))  # 去重

        final_answer = {
            "success": True,
            "answer": "\n".join(answer_parts),
            "sources": sources,
            "tool_calls_count": len(self.tool_calls),
            "confidence": "high" if len(all_results) > 3 else "medium"
        }

        return final_answer

    def process_query(self, query: str) -> Dict[str, Any]:
        """处理用户查询的主要流程"""
        self.add_message("user", query)

        print(f"\n=== 开始处理查询: {query} ===")

        while self.should_continue_search():
            # 选择工具
            tool_call = self.choose_tool(query, [call["result"] for call in self.tool_calls])
            if not tool_call:
                print("没有合适的工具可以继续搜索")
                break

            print(f"\n--- 调用工具: {tool_call['tool']} ---")
            print(f"参数: {json.dumps(tool_call['params'], ensure_ascii=False, indent=2)}")

            # 执行工具
            result = self.execute_tool(tool_call)

            print(f"结果: {'成功' if result.get('success') else '失败'}")
            if result.get("results"):
                print(f"找到 {len(result['results'])} 条结果")
                # 显示前几个结果的摘要，便于理解LLM获得了什么信息
                for i, item in enumerate(result["results"][:2], 1):
                    if tool_call['tool'] == "vector_search":
                        title = item.get('title', '未知标题')[:50]
                        content = item.get('content', '')[:100]
                        print(f"  结果{i}: {title} - {content}...")
                    elif tool_call['tool'] == "keyword_search":
                        file_path = item.get('file_path', '')
                        line_num = item.get('line_number', 0)
                        content = item.get('content', '')[:80]
                        print(f"  结果{i}: {file_path}:{line_num} - {content}...")
                    elif tool_call['tool'] == "text_reader":
                        file_path = item.get('file_path', '')
                        content = item.get('content', '')[:100]
                        print(f"  结果{i}: {file_path} - {content}...")
            elif result.get("error"):
                print(f"错误: {result['error']}")

            # 将工具调用结果添加到对话历史
            tool_result_summary = f"调用了工具 {tool_call['tool']}，参数：{json.dumps(tool_call['params'], ensure_ascii=False)}\n结果："
            if result.get("success"):
                if result.get("results"):
                    tool_result_summary += f"成功找到 {len(result['results'])} 条结果。\n前几个结果摘要：\n"
                    for i, item in enumerate(result["results"][:3], 1):
                        if tool_call['tool'] == "vector_search":
                            tool_result_summary += f"{i}. {item.get('title', '未知标题')} - {item.get('content', '')[:150]}...\n"
                        elif tool_call['tool'] == "keyword_search":
                            tool_result_summary += f"{i}. {item.get('file_path', '')}:{item.get('line_number', 0)} - {item.get('content', '')[:100]}...\n"
                        elif tool_call['tool'] == "text_reader":
                            tool_result_summary += f"{i}. {item.get('file_path', '')} 内容片段: {item.get('content', '')[:150]}...\n"
                else:
                    tool_result_summary += "成功但无匹配结果。\n"
            else:
                tool_result_summary += f"失败: {result.get('error', '未知错误')}\n"

            self.add_message("assistant", tool_result_summary)

        # 生成最终答案
        print(f"\n=== 生成答案 ===")
        final_answer = self.generate_answer(query)

        self.add_message("assistant", final_answer.get("answer", ""))

        return final_answer

if __name__ == "__main__":
    # 测试代码
    agent = AgenticAgent()
    result = agent.process_query("LLM embedding")
    print("\n" + "="*50)
    print("最终答案:")
    print(result.get("answer", ""))
    print(f"\n来源: {result.get('sources', [])}")
    print(f"工具调用次数: {result.get('tool_calls_count', 0)}")