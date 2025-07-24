#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PTL 简化版本功能演示
"""

import subprocess
import sys

def run_ptl(command):
    """运行ptl命令并返回结果"""
    try:
        result = subprocess.run([sys.executable, 'ptl'] + command.split(), 
                              capture_output=True, text=True, cwd='.')
        return result.stdout.strip()
    except Exception as e:
        return f"错误: {e}"

def demo():
    """演示PTL简化版本的所有功能"""
    print("=" * 60)
    print("           PTL 简化版本功能演示")
    print("=" * 60)
    
    demos = [
        ("MD5哈希", 'md5 "Hello World 你好世界"'),
        ("URL编码", 'url "https://example.com/search?q=hello world"'),
        ("URL解码", 'unurl "https%3A//example.com/search%3Fq%3Dhello%20world"'),
        ("Base64编码", 'b64 "Hello World 你好世界"'),
        ("Base64解码", 'unb64 "SGVsbG8gV29ybGQg5L2g5aW95LiW55WM"'),
        ("时间戳转日期", 'ts2dt 1640995200'),
        ("日期转时间戳", 'dt2ts "2024-07-24 15:30:00"'),
        ("当前时间戳", 'now'),
        ("当前日期时间", 'time'),
    ]
    
    for desc, cmd in demos:
        print(f"\n{desc}:")
        print(f"  命令: ptl {cmd}")
        result = run_ptl(cmd)
        print(f"  结果: {result}")
    
    print(f"\n帮助信息:")
    print(f"  命令: ptl help")
    help_result = run_ptl('help')
    print("  " + help_result.replace('\n', '\n  '))
    
    print("\n" + "=" * 60)
    print("演示完成！现在您可以使用简化的 ptl 命令了")
    print("=" * 60)

if __name__ == "__main__":
    demo()