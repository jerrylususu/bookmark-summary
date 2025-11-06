#!/usr/bin/env python3
"""
LLM客户端
基于.env中的配置调用LLM API，用于智能工具选择和答案生成
"""

import json
import logging
import os
import requests
from typing import Dict, List, Optional, Any
from pathlib import Path
from dotenv import load_dotenv

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LLMClient:
    """LLM API客户端"""

    def __init__(self, env_path: Optional[Path] = None):
        """初始化LLM客户端

        Args:
            env_path: .env文件路径，默认为当前目录的.env
        """
        if env_path is None:
            env_path = Path("/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary/.env")

        load_dotenv(dotenv_path=env_path, override=False)

        self.api_key = os.environ.get("LLM_TOKEN")
        self.model = os.environ.get("LLM_MODEL", "gpt-3.5-turbo")
        self.base_url = os.environ.get("LLM_ENDPOINT")

        if not self.api_key:
            raise ValueError("Environment variable LLM_TOKEN is required for LLM requests.")
        if not self.base_url:
            raise ValueError("Environment variable LLM_ENDPOINT is required for LLM requests.")

        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        })

        self.request_timeout = 60
        self.max_retries = 3
        self.retry_backoff = 2.0

    def chat_completion(self, messages: List[Dict[str, str]],
                       temperature: float = 0.7, tools: Optional[List[Dict]] = None,
                       tool_choice: Optional[Dict] = None) -> Dict[str, Any]:
        """调用LLM生成回复

        Args:
            messages: 消息列表，格式为[{"role": "user|assistant|system", "content": "..."}]
            temperature: 温度参数，控制随机性
            tools: 工具定义列表（用于function calling）
            tool_choice: 工具选择策略

        Returns:
            包含content和tool_calls的完整响应
        """
        if not messages:
            raise ValueError("Messages list cannot be empty")

        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
        }

        # 添加工具定义
        if tools:
            payload["tools"] = tools
        if tool_choice:
            payload["tool_choice"] = tool_choice

        attempt = 0
        while True:
            try:
                logger.info(f"Calling LLM API (attempt {attempt + 1})")
                response = self.session.post(
                    self.base_url,
                    json=payload,
                    timeout=self.request_timeout,
                )
                response.raise_for_status()

            except requests.HTTPError as exc:
                attempt += 1
                status = exc.response.status_code if exc.response else "?"
                if (
                    attempt < self.max_retries
                    and status in (429, 500, 502, 503, 504)
                ):
                    backoff = self.retry_backoff ** attempt
                    logger.warning(
                        "LLM request failed with status %s (attempt %d/%d). Retrying in %.1fs.",
                        status, attempt, self.max_retries, backoff
                    )
                    import time
                    time.sleep(backoff)
                    continue
                error_text = exc.response.text if exc.response else str(exc)
                logger.error(f"LLM request failed with status {status}: {error_text}")
                if exc.response:
                    logger.error(f"Request payload: {json.dumps(payload, indent=2, ensure_ascii=False)}")
                raise RuntimeError(f"LLM API error: {error_text}")

            except requests.RequestException as exc:
                attempt += 1
                if attempt < self.max_retries:
                    backoff = self.retry_backoff ** attempt
                    logger.warning(
                        "LLM request connection error (attempt %d/%d). Retrying in %.1fs.",
                        attempt, self.max_retries, backoff
                    )
                    import time
                    time.sleep(backoff)
                    continue
                logger.error(f"LLM request connection error: {exc}")
                raise

            break

        try:
            response_data = response.json()
            if "choices" not in response_data or not response_data["choices"]:
                raise RuntimeError("LLM API returned no choices")

            message = response_data["choices"][0]["message"]
            content = message.get("content", "")
            tool_calls = message.get("tool_calls", [])

            # 提取token使用信息
            usage = response_data.get("usage", {})
            prompt_tokens = usage.get("prompt_tokens", 0)
            completion_tokens = usage.get("completion_tokens", 0)
            total_tokens = usage.get("total_tokens", 0)

            logger.info(f"LLM response received: content={len(content) if content else 0} chars, tool_calls={len(tool_calls)}")
            if total_tokens > 0:
                logger.info(f"Token usage - Prompt: {prompt_tokens}, Completion: {completion_tokens}, Total: {total_tokens}")

            return {
                "content": content.strip() if content else "",
                "tool_calls": tool_calls
            }

        except (KeyError, json.JSONDecodeError) as exc:
            logger.error(f"Failed to parse LLM response: {exc}")
            logger.error(f"Response data: {response.text}")
            raise RuntimeError(f"Failed to parse LLM response: {exc}")

    def choose_tool(self, query: str, available_tools: List[str],
                   previous_results: List[Dict], conversation_history: List[Dict] = None) -> Optional[Dict[str, Any]]:
        """使用LLM选择下一个工具（优先使用native tool calling，fallback到JSON）

        Args:
            query: 用户查询
            available_tools: 可用工具列表
            previous_results: 之前的搜索结果

        Returns:
            工具调用字典或None
        """
        # 定义工具schema
        tools = []

        if "keyword_search" in available_tools:
            tools.append({
                "type": "function",
                "function": {
                    "name": "keyword_search",
                    "description": "搜索文件内容中的关键词匹配，适合查找特定术语或文件",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "搜索关键词"
                            },
                            "max_results": {
                                "type": "integer",
                                "description": "最大结果数"
                            }
                        },
                        "required": ["query"]
                    }
                }
            })

        if "vector_search" in available_tools:
            tools.append({
                "type": "function",
                "function": {
                    "name": "vector_search",
                    "description": "基于语义相似度搜索，适合概念性、主题性查询",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "查询文本"
                            },
                            "top_k": {
                                "type": "integer",
                                "description": "返回结果数量"
                            }
                        },
                        "required": ["query"]
                    }
                }
            })

        if "text_reader" in available_tools:
            tools.append({
                "type": "function",
                "function": {
                    "name": "text_reader",
                    "description": "读取指定文件的详细内容。当vector_search或keyword_search返回了文件路径后，使用此工具获取完整信息",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "file_path": {
                                "type": "string",
                                "description": "文件路径（从搜索结果中的file_path或document_id字段提取）"
                            },
                            "start_line": {
                                "type": "integer",
                                "description": "开始行号"
                            },
                            "end_line": {
                                "type": "integer",
                                "description": "结束行号"
                            }
                        },
                        "required": ["file_path"]
                    }
                }
            })

        # 构建搜索结果摘要和可用文件信息
        previous_summary = ""
        tool_usage_count = {"keyword_search": 0, "vector_search": 0, "text_reader": 0}
        available_files = []

        if previous_results:
            previous_summary = "之前的搜索结果摘要:\n"
            for i, result in enumerate(previous_results[-3:], 1):
                if result.get("success") and result.get("results"):
                    previous_summary += f"{i}. 成功找到 {len(result['results'])} 条结果\n"
                    for item in result["results"][:2]:
                        if item.get('file_path'):
                            available_files.append(item['file_path'])
                            previous_summary += f"   - 发现文件: {item['file_path'][:80]}...\n"
                        elif item.get('document_id'):
                            doc_parts = item['document_id'].split(':', 2)
                            if len(doc_parts) >= 3:
                                year_month = doc_parts[0]
                                timestamp = int(doc_parts[1])
                                slug = doc_parts[2]
                                from datetime import datetime
                                dt = datetime.fromtimestamp(timestamp)
                                date_str = dt.strftime('%Y-%m-%d')
                                file_path = f"{year_month}/{date_str}-{slug}.md"
                                available_files.append(file_path)
                                previous_summary += f"   - 发现文档: {file_path[:80]}...\n"
                else:
                    previous_summary += f"{i}. 搜索失败或无结果\n"

            if available_files:
                previous_summary += f"\n可用的文件路径供text_reader使用:\n"
                for file_path in available_files[:3]:
                    previous_summary += f"  - {file_path}\n"

        # 统计工具使用频率
        for result in previous_results:
            if result.get("tool_used"):
                tool_usage_count[result["tool_used"]] = tool_usage_count.get(result["tool_used"], 0) + 1

        # 先尝试native tool calling
        system_prompt = f"""你是一个智能搜索助手。你的任务是根据用户的查询和之前的搜索结果，选择最合适的下一个工具。

工作流程指导：
1. 第一轮使用vector_search查找概念性内容，或keyword_search查找具体术语
2. 如果搜索结果返回了有价值的文件路径或document_id，使用text_reader读取详细内容
3. text_reader应该用在找到相关文件后需要获取完整信息的场景

重要原则：
1. 概念性查询优先用vector_search，具体术语用keyword_search
2. 当看到vector_search/keyword_search结果中有文件路径时，应该用text_reader获取完整内容
3. 避免重复使用同一种工具超过3次，要尝试不同的搜索策略

{previous_summary}"""

        # 构建消息列表
        messages = [{"role": "system", "content": system_prompt}]

        # 添加对话历史
        if conversation_history:
            for msg in conversation_history:
                messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        # 添加当前查询
        messages.append({
            "role": "user",
            "content": f"用户查询: {query}\n\n请根据当前情况选择下一个工具调用。"
        })

        # 尝试native tool calling
        if tools:
            try:
                logger.info(f"尝试native tool calling，提供{len(tools)}个工具")
                response = self.chat_completion(
                    messages=messages,
                    temperature=0.3,
                    tools=tools,
                    tool_choice={"type": "auto"}
                )

                tool_calls = response.get("tool_calls", [])

                if tool_calls:
                    # 处理第一个tool call
                    tool_call = tool_calls[0]
                    function_name = tool_call["function"]["name"]

                    if function_name in available_tools:
                        # 解析参数
                        try:
                            arguments = json.loads(tool_call["function"]["arguments"])
                            logger.info(f"LLM通过native tool calling选择了工具: {function_name}")
                            return {
                                "tool": function_name,
                                "params": arguments,
                                "reasoning": "LLM native tool calling"
                            }
                        except json.JSONDecodeError as e:
                            logger.error(f"Failed to parse tool arguments: {e}")
                        else:
                            logger.warning(f"LLM选择了不可用的工具: {function_name}")
                else:
                    logger.info("LLM认为搜索已完成 (native tool calling)")
                    return None

            except Exception as e:
                logger.warning(f"Native tool calling失败，fallback到JSON模式: {e}")

        # Fallback到JSON模式
        logger.info("使用JSON模式进行工具选择")

        tool_descriptions = {
            "keyword_search": "搜索文件内容中的关键词匹配，适合查找特定术语或文件",
            "vector_search": "基于语义相似度搜索，适合概念性、主题性查询",
            "text_reader": "读取指定文件的详细内容。当vector_search或keyword_search返回了文件路径后，使用此工具获取完整信息。参数：file_path(文件路径)，start_line(开始行，默认1)，end_line(结束行，默认200)"
        }

        # 构建工具选择提示
        tools_info = "\n".join([
            f"- {tool}: {desc}"
            for tool, desc in tool_descriptions.items()
            if tool in available_tools
        ])

        # 构建工具使用建议
        tool_suggestion = ""
        if tool_usage_count.get("vector_search", 0) >= 3:
            tool_suggestion = "\n\n注意：已经多次使用vector_search，建议尝试keyword_search或text_reader来获取不同类型的信息。"
        elif tool_usage_count.get("keyword_search", 0) >= 3:
            tool_suggestion = "\n\n注意：已经多次使用keyword_search，建议尝试vector_search或text_reader来获取不同类型的信息。"

        json_system_prompt = f"""你是一个智能搜索助手。你的任务是根据用户的查询和之前的搜索结果，选择最合适的下一个工具。

工作流程指导：
1. 第一轮使用vector_search查找概念性内容，或keyword_search查找具体术语
2. 如果搜索结果返回了有价值的文件路径或document_id，使用text_reader读取详细内容
3. text_reader应该用在找到相关文件后需要获取完整信息的场景

重要原则：
1. 概念性查询优先用vector_search，具体术语用keyword_search
2. 当看到vector_search/keyword_search结果中有文件路径时，应该用text_reader获取完整内容
3. 避免重复使用同一种工具超过3次，要尝试不同的搜索策略

请按照以下JSON格式回复，不要包含任何其他文本：
{{
    "tool": "工具名称",
    "params": {{"参数名": "参数值"}},
    "reasoning": "选择这个工具的原因"
}}

如果认为搜索已经完成，不需要更多工具，请回复：
{{
    "tool": null,
    "reasoning": "搜索已完成的原因"
}}

参数说明：
- keyword_search: {{"query": "搜索关键词", "max_results": 数字}}
- vector_search: {{"query": "查询文本", "top_k": 数字}}
- text_reader: {{"file_path": "从搜索结果中的file_path或document_id字段提取", "start_line": 1, "end_line": 200}}{tool_suggestion}"""

        json_messages = [{"role": "system", "content": json_system_prompt}]

        # 添加对话历史
        if conversation_history:
            for msg in conversation_history:
                json_messages.append({
                    "role": msg["role"],
                    "content": msg["content"]
                })

        # 添加当前的工具选择请求
        json_messages.append({"role": "user", "content": f"""用户查询: {query}

可用工具:
{tools_info}

{previous_summary}

请选择下一个工具调用。"""})

        try:
            response = self.chat_completion(json_messages, temperature=0.3)
            content = response.get("content", "")

            # 尝试解析JSON回复
            try:
                decision = json.loads(content)
                if decision.get("tool") is None:
                    logger.info(f"LLM认为搜索已完成 (JSON模式): {decision.get('reasoning', 'No reason')}")
                    return None

                tool_name = decision["tool"]
                if tool_name not in available_tools:
                    logger.warning(f"LLM选择了不可用的工具 (JSON模式): {tool_name}")
                    return None

                params = decision.get("params", {})
                reasoning = decision.get("reasoning", "No reasoning provided")

                logger.info(f"LLM通过JSON模式选择了工具: {tool_name}")
                return {"tool": tool_name, "params": params, "reasoning": reasoning}

            except json.JSONDecodeError:
                logger.error(f"LLM返回了无效的JSON: {content}")
                raise ValueError(f"LLM returned invalid JSON: {content}")

        except Exception as e:
            logger.error(f"LLM工具选择失败 (JSON模式): {e}")
            raise

    def generate_answer(self, query: str, search_results: List[Dict]) -> str:
        """使用LLM基于搜索结果生成最终答案

        Args:
            query: 用户查询
            search_results: 搜索结果列表

        Returns:
            生成的答案
        """
        if not search_results:
            return f"很抱歉，没有找到与您的问题「{query}」相关的信息。"

        # 整理搜索结果
        results_summary = []
        for i, result in enumerate(search_results, 1):
            if result.get("success") and result.get("results"):
                tool_name = result.get("tool_name", "unknown")
                results_summary.append(f"结果 {i} (来源: {tool_name}):")

                for j, item in enumerate(result["results"][:3], 1):  # 每个工具最多显示3个结果
                    if tool_name == "vector_search":
                        results_summary.append(
                            f"  {j}. {item.get('title', '未知标题')} - {item.get('content', '')[:200]}..."
                        )
                    elif tool_name == "keyword_search":
                        results_summary.append(
                            f"  {j}. 文件 {item.get('file_path', '')} 第{item.get('line_number', 0)}行: {item.get('content', '')[:150]}..."
                        )
                    elif tool_name == "text_reader":
                        results_summary.append(
                            f"  {j}. 文件内容预览: {item.get('content', '')[:300]}..."
                        )

        if not results_summary:
            return f"很抱歉，搜索过程中虽然执行了工具，但没有找到与您的问题「{query}」相关的有效信息。"

        system_prompt = """你是一个智能搜索助手。请根据用户提供的搜索结果，生成准确、有用、简洁的答案。

要求：
1. 基于搜索结果回答问题，不要添加搜索结果之外的信息
2. 如果搜索结果不足以回答问题，要诚实说明
3. 答案要结构化、易读
4. 使用中文回答"""

        user_prompt = f"""用户查询: {query}

搜索结果:
{chr(10).join(results_summary)}

请基于以上搜索结果回答用户的问题。"""

        try:
            response = self.chat_completion(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5
            )
            return response.get("content", "")

        except Exception as e:
            logger.error(f"LLM answer generation failed: {e}")
            # 回退到简单答案生成
            return f"根据搜索结果，关于「{query}」找到了 {len(search_results)} 个相关结果，但生成详细答案时遇到了问题。请查看搜索结果获取更多信息。"

    def close(self):
        """关闭会话"""
        if self.session:
            self.session.close()


# 全局LLM客户端实例
_llm_client: Optional[LLMClient] = None

def get_llm_client() -> LLMClient:
    """获取LLM客户端实例（单例模式）"""
    global _llm_client
    if _llm_client is None:
        _llm_client = LLMClient()
    return _llm_client


if __name__ == "__main__":
    # 测试代码
    client = get_llm_client()

    # 测试工具选择
    print("=== 测试工具选择 ===")
    tool_decision = client.choose_tool(
        "LLM embedding相关文章",
        ["keyword_search", "vector_search", "text_reader"],
        []
    )
    print(f"工具选择结果: {tool_decision}")

    # 测试答案生成
    print("\n=== 测试答案生成 ===")
    test_results = [
        {
            "tool_name": "vector_search",
            "success": True,
            "results": [
                {"title": "Embedding最佳实践", "content": "embedding是表示文本语义的向量..."},
                {"title": "LLM架构解析", "content": "大型语言模型使用embedding层..."}
            ]
        }
    ]
    answer = client.generate_answer("什么是embedding", test_results)
    print(f"生成的答案:\n{answer}")

    client.close()