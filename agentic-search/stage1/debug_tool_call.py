#!/usr/bin/env python3
"""
调试tool calling问题
"""

import json
import logging
import sys
import os

# 添加核心目录到 Python 路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from llm_client import get_llm_client

# 设置日志
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_simple_tool_call():
    """测试简单的工具调用"""
    try:
        client = get_llm_client()

        # 简单的工具定义
        tools = [{
            "type": "function",
            "function": {
                "name": "keyword_search",
                "description": "搜索关键词",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "搜索关键词"
                        }
                    },
                    "required": ["query"]
                }
            }
        }]

        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Search for 'LLM'"}
        ]

        print("发送请求...")
        print(f"Tools: {json.dumps(tools, indent=2, ensure_ascii=False)}")
        print(f"Messages: {json.dumps(messages, indent=2, ensure_ascii=False)}")

        response = client.chat_completion(
            messages=messages,
            temperature=0.3,
            tools=tools,
            tool_choice={"type": "auto"}
        )

        print(f"响应: {json.dumps(response, indent=2, ensure_ascii=False)}")

    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_simple_tool_call()