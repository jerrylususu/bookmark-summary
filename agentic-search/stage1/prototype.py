#!/usr/bin/env python3
"""
原型入口程序
硬编码测试查询或接受命令行参数，输出完整推理过程和最终答案
"""

import argparse
import json
import sys
import os
from datetime import datetime

# 添加核心目录到 Python 路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'core'))

from agent import AgenticAgent

def main():
    parser = argparse.ArgumentParser(description='Agentic Search 原型')
    parser.add_argument('--query', '-q', type=str, help='搜索查询')
    parser.add_argument('--test', '-t', action='store_true', help='运行硬编码测试查询')
    parser.add_argument('--verbose', '-v', action='store_true', help='详细输出')

    args = parser.parse_args()

    # 硬编码的测试查询
    test_queries = [
        "Find all articles about LLM embeddings",
        "What frontend technology articles are there in June 2024?",
        "What are the best practices related to Embeddings?",
        "查找关于LLM的文章",
        "2024年6月有哪些前端技术相关的文章？"
    ]

    print("=" * 60)
    print("🤖 Agentic Search 原型")
    print("=" * 60)

    # 创建代理
    agent = AgenticAgent()

    # 确定要执行的查询
    if args.query:
        queries = [args.query]
    elif args.test:
        queries = test_queries
        print(f"🧪 运行 {len(queries)} 个测试查询")
    else:
        # 默认运行一个测试查询
        queries = [test_queries[0]]
        print("🔍 运行默认测试查询")

    # 处理每个查询
    for i, query in enumerate(queries, 1):
        if len(queries) > 1:
            print(f"\n{'='*60}")
            print(f"查询 {i}/{len(queries)}: {query}")
            print(f"{'='*60}")
        else:
            print(f"\n查询: {query}")

        start_time = datetime.now()

        # 处理查询
        result = agent.process_query(query)

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()

        # 输出结果
        print(f"\n{'='*60}")
        print("📋 最终答案")
        print(f"{'='*60}")
        print(result.get("answer", "无法生成答案"))

        print(f"\n📊 统计信息:")
        print(f"  - 工具调用次数: {result.get('tool_calls_count', 0)}")
        print(f"  - 置信度: {result.get('confidence', 'unknown')}")
        print(f"  - 处理时间: {duration:.2f} 秒")

        sources = result.get('sources', [])
        if sources:
            print(f"  - 来源文件 ({len(sources)} 个):")
            for source in sources[:5]:  # 最多显示5个来源
                print(f"    • {source}")
            if len(sources) > 5:
                print(f"    ... 还有 {len(sources) - 5} 个文件")

        # 详细输出模式
        if args.verbose:
            print(f"\n🔧 工具调用详情:")
            for j, call in enumerate(agent.tool_calls, 1):
                print(f"  {j}. {call['tool']}")
                print(f"     参数: {json.dumps(call['params'], ensure_ascii=False)}")
                result_data = call['result']
                if result_data.get('success'):
                    if result_data.get('results'):
                        print(f"     结果: 找到 {len(result_data['results'])} 条记录")
                    else:
                        print(f"     结果: 无匹配内容")
                else:
                    print(f"     错误: {result_data.get('error', '未知错误')}")

        print(f"\n{'='*60}")

    print("\n✅ 查询处理完成")

if __name__ == "__main__":
    main()