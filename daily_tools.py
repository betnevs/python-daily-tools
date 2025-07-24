#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
日常工具集合
支持MD5、URL编码/解码、Base64编码/解码、时间戳转换等功能
"""

import hashlib
import base64
import urllib.parse
import datetime
import time
import sys


class DailyTools:
    """日常工具类"""
    
    @staticmethod
    def md5_hash(text):
        """计算MD5哈希值"""
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    
    @staticmethod
    def url_encode(text):
        """URL编码"""
        return urllib.parse.quote(text, safe='')
    
    @staticmethod
    def url_decode(text):
        """URL解码"""
        return urllib.parse.unquote(text)
    
    @staticmethod
    def base64_encode(text):
        """Base64编码"""
        return base64.b64encode(text.encode('utf-8')).decode('utf-8')
    
    @staticmethod
    def base64_decode(text):
        """Base64解码"""
        try:
            return base64.b64decode(text).decode('utf-8')
        except Exception as e:
            return f"解码失败: {str(e)}"
    
    @staticmethod
    def timestamp_to_datetime(timestamp):
        """时间戳转换为日期时间格式"""
        try:
            # 支持秒级和毫秒级时间戳
            if len(str(int(float(timestamp)))) > 10:
                timestamp = float(timestamp) / 1000
            dt = datetime.datetime.fromtimestamp(float(timestamp))
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            return f"转换失败: {str(e)}"
    
    @staticmethod
    def datetime_to_timestamp(datetime_str):
        """日期时间格式转换为时间戳"""
        try:
            # 支持多种日期格式
            formats = [
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d',
                '%Y/%m/%d %H:%M:%S',
                '%Y/%m/%d',
                '%m/%d/%Y %H:%M:%S',
                '%m/%d/%Y'
            ]
            
            for fmt in formats:
                try:
                    dt = datetime.datetime.strptime(datetime_str, fmt)
                    return int(dt.timestamp())
                except ValueError:
                    continue
            
            return "不支持的日期格式，请使用如: 2024-01-01 12:00:00"
        except Exception as e:
            return f"转换失败: {str(e)}"
    
    @staticmethod
    def current_timestamp():
        """获取当前时间戳"""
        return int(time.time())
    
    @staticmethod
    def current_datetime():
        """获取当前日期时间"""
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def show_menu():
    """显示菜单"""
    print("\n" + "="*50)
    print("           日常工具集合")
    print("="*50)
    print("1. MD5 哈希")
    print("2. URL 编码")
    print("3. URL 解码")
    print("4. Base64 编码")
    print("5. Base64 解码")
    print("6. 时间戳转日期时间")
    print("7. 日期时间转时间戳")
    print("8. 获取当前时间戳")
    print("9. 获取当前日期时间")
    print("0. 退出")
    print("="*50)


def main():
    """主函数"""
    tools = DailyTools()
    
    while True:
        show_menu()
        choice = input("请选择功能 (0-9): ").strip()
        
        if choice == '0':
            print("感谢使用，再见！")
            break
        elif choice == '1':
            text = input("请输入要计算MD5的文本: ")
            result = tools.md5_hash(text)
            print(f"MD5结果: {result}")
        elif choice == '2':
            text = input("请输入要URL编码的文本: ")
            result = tools.url_encode(text)
            print(f"URL编码结果: {result}")
        elif choice == '3':
            text = input("请输入要URL解码的文本: ")
            result = tools.url_decode(text)
            print(f"URL解码结果: {result}")
        elif choice == '4':
            text = input("请输入要Base64编码的文本: ")
            result = tools.base64_encode(text)
            print(f"Base64编码结果: {result}")
        elif choice == '5':
            text = input("请输入要Base64解码的文本: ")
            result = tools.base64_decode(text)
            print(f"Base64解码结果: {result}")
        elif choice == '6':
            timestamp = input("请输入时间戳 (支持秒级和毫秒级): ")
            result = tools.timestamp_to_datetime(timestamp)
            print(f"转换结果: {result}")
        elif choice == '7':
            datetime_str = input("请输入日期时间 (如: 2024-01-01 12:00:00): ")
            result = tools.datetime_to_timestamp(datetime_str)
            print(f"时间戳结果: {result}")
        elif choice == '8':
            result = tools.current_timestamp()
            print(f"当前时间戳: {result}")
        elif choice == '9':
            result = tools.current_datetime()
            print(f"当前日期时间: {result}")
        else:
            print("无效选择，请重新输入！")
        
        input("\n按回车键继续...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n程序被用户中断，再见！")
        sys.exit(0)
    except Exception as e:
        print(f"\n程序出现错误: {str(e)}")
        sys.exit(1)