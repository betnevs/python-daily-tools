#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
命令行版本的日常工具集合
可以通过命令行参数直接调用各种功能
"""

import argparse
import hashlib
import base64
import urllib.parse
import datetime
import time
import sys


class ToolsCLI:
    """命令行工具类"""
    
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
            formats = [
                '%Y-%m-%d %H:%M:%S',
                '%Y-%m-%d',
                '%Y/%m/%d %H:%M:%S',
                '%Y/%m/%d'
            ]
            
            for fmt in formats:
                try:
                    dt = datetime.datetime.strptime(datetime_str, fmt)
                    return str(int(dt.timestamp()))
                except ValueError:
                    continue
            
            return "不支持的日期格式"
        except Exception as e:
            return f"转换失败: {str(e)}"


def main():
    """主函数"""
    parser = argparse.ArgumentParser(description='日常工具集合 - 命令行版本')
    parser.add_argument('action', choices=[
        'md5', 'url-encode', 'url-decode', 
        'base64-encode', 'base64-decode',
        'ts-to-dt', 'dt-to-ts', 'now-ts', 'now-dt'
    ], help='要执行的操作')
    parser.add_argument('input', nargs='?', help='输入内容')
    
    args = parser.parse_args()
    tools = ToolsCLI()
    
    # 对于不需要输入的操作
    if args.action == 'now-ts':
        print(int(time.time()))
        return
    elif args.action == 'now-dt':
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return
    
    # 需要输入内容的操作
    if not args.input:
        print("错误: 此操作需要输入内容")
        sys.exit(1)
    
    if args.action == 'md5':
        print(tools.md5_hash(args.input))
    elif args.action == 'url-encode':
        print(tools.url_encode(args.input))
    elif args.action == 'url-decode':
        print(tools.url_decode(args.input))
    elif args.action == 'base64-encode':
        print(tools.base64_encode(args.input))
    elif args.action == 'base64-decode':
        print(tools.base64_decode(args.input))
    elif args.action == 'ts-to-dt':
        print(tools.timestamp_to_datetime(args.input))
    elif args.action == 'dt-to-ts':
        print(tools.datetime_to_timestamp(args.input))


if __name__ == "__main__":
    main()