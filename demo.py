#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日常工具集合演示脚本
"""

from daily_tools import DailyTools

def demo():
    """演示所有功能"""
    tools = DailyTools()
    
    print("=" * 60)
    print("           日常工具集合功能演示")
    print("=" * 60)
    
    # 测试文本
    test_text = "Hello World 你好世界"
    test_url = "https://example.com/search?q=hello world&lang=zh"
    test_base64 = "SGVsbG8gV29ybGQg5L2g5aW95LiW55WM"
    test_timestamp = 1640995200
    test_datetime = "2024-07-24 15:30:00"
    
    print(f"\n1. MD5哈希演示")
    print(f"   输入: {test_text}")
    print(f"   MD5:  {tools.md5_hash(test_text)}")
    
    print(f"\n2. URL编码演示")
    print(f"   原文: {test_url}")
    encoded_url = tools.url_encode(test_url)
    print(f"   编码: {encoded_url}")
    print(f"   解码: {tools.url_decode(encoded_url)}")
    
    print(f"\n3. Base64编码演示")
    print(f"   原文: {test_text}")
    encoded_b64 = tools.base64_encode(test_text)
    print(f"   编码: {encoded_b64}")
    print(f"   解码: {tools.base64_decode(encoded_b64)}")
    
    print(f"\n4. 时间戳转换演示")
    print(f"   时间戳: {test_timestamp}")
    print(f"   日期时间: {tools.timestamp_to_datetime(test_timestamp)}")
    print(f"   日期时间: {test_datetime}")
    print(f"   时间戳: {tools.datetime_to_timestamp(test_datetime)}")
    
    print(f"\n5. 当前时间")
    print(f"   当前时间戳: {tools.current_timestamp()}")
    print(f"   当前日期时间: {tools.current_datetime()}")
    
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)

if __name__ == "__main__":
    demo()