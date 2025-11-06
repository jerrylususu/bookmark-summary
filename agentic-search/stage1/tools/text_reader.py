#!/usr/bin/env python3
"""
文本范围读取工具
读取指定文件的行号范围内容
"""

import os
from typing import List, Dict, Any

def text_reader(file_path: str, start_line: int = 1, end_line: int = 200) -> Dict[str, Any]:
    """
    读取指定文件的行范围内容

    Args:
        file_path: 文件路径
        start_line: 开始行号（从1开始）
        end_line: 结束行号

    Returns:
        读取结果字典
    """
    try:
        # 限制最大读取行数
        max_lines = 200
        if end_line - start_line + 1 > max_lines:
            end_line = start_line + max_lines - 1

        # 构建完整路径
        base_path = "/home/jerrylu/code/251028-bookmark-by-month/bookmark-summary"
        if not os.path.isabs(file_path):
            full_path = os.path.join(base_path, file_path)
        else:
            full_path = file_path

        if not os.path.exists(full_path):
            return {
                "success": False,
                "error": f"文件不存在: {full_path}",
                "file_path": file_path,
                "start_line": start_line,
                "end_line": end_line,
                "content": ""
            }

        # 读取文件内容
        with open(full_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # 获取指定行范围
        total_lines = len(lines)
        if start_line < 1:
            start_line = 1
        if end_line > total_lines:
            end_line = total_lines

        if start_line > total_lines:
            return {
                "success": False,
                "error": f"开始行号超出文件范围（文件共{total_lines}行）",
                "file_path": file_path,
                "start_line": start_line,
                "end_line": end_line,
                "total_lines": total_lines,
                "content": ""
            }

        # 提取指定行内容
        selected_lines = lines[start_line - 1:end_line]
        content = ''.join(selected_lines)

        return {
            "success": True,
            "file_path": file_path,
            "full_path": full_path,
            "start_line": start_line,
            "end_line": end_line,
            "total_lines": total_lines,
            "lines_read": len(selected_lines),
            "content": content
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "file_path": file_path,
            "start_line": start_line,
            "end_line": end_line,
            "content": ""
        }

if __name__ == "__main__":
    # 测试代码
    import json
    result = text_reader("embedding_store.py", 1, 20)
    print(json.dumps(result, indent=2, ensure_ascii=False))