# 日常工具集合

这是一个Python实现的日常工具集合，包含常用的文本处理和时间转换功能。

## 功能特性

1. **MD5哈希** - 计算文本的MD5哈希值
2. **URL编码/解码** - URL编码和解码功能
3. **Base64编码/解码** - Base64编码和解码功能
4. **时间戳转换** - Linux时间戳和日期时间格式之间的转换

## 使用方法

### 🚀 简化版本 (ptl) - 推荐使用

最简单的使用方式，命令简短易记：

```bash
# MD5哈希
ptl md5 "hello world"

# URL编码/解码
ptl url "hello world"
ptl unurl "hello%20world"

# Base64编码/解码
ptl b64 "hello world"
ptl unb64 "aGVsbG8gd29ybGQ="

# 时间戳转换
ptl ts2dt 1640995200
ptl dt2ts "2022-01-01 12:00:00"

# 获取当前时间
ptl now      # 当前时间戳
ptl time     # 当前日期时间

# 查看帮助
ptl help
```

#### 安装简化版本

**方法1: 使用别名 (推荐)**
```bash
# 运行设置脚本
bash setup_alias.sh
source ~/.bashrc  # 或 ~/.zshrc
```

**方法2: 系统安装 (Linux/Mac)**
```bash
sudo bash install.sh
```

**方法3: 临时使用**
```bash
python ptl md5 "hello world"
```

### 交互式版本 (daily_tools.py)

运行交互式版本，通过菜单选择功能：

```bash
python daily_tools.py
```

### 完整命令行版本 (tools_cli.py)

直接通过命令行参数使用：

```bash
# MD5哈希
python tools_cli.py md5 "hello world"

# URL编码
python tools_cli.py url-encode "hello world"

# URL解码
python tools_cli.py url-decode "hello%20world"

# Base64编码
python tools_cli.py base64-encode "hello world"

# Base64解码
python tools_cli.py base64-decode "aGVsbG8gd29ybGQ="

# 时间戳转日期时间
python tools_cli.py ts-to-dt 1640995200

# 日期时间转时间戳
python tools_cli.py dt-to-ts "2022-01-01 12:00:00"

# 获取当前时间戳
python tools_cli.py now-ts

# 获取当前日期时间
python tools_cli.py now-dt
```

## 支持的日期格式

- `YYYY-MM-DD HH:MM:SS` (如: 2024-01-01 12:00:00)
- `YYYY-MM-DD` (如: 2024-01-01)
- `YYYY/MM/DD HH:MM:SS` (如: 2024/01/01 12:00:00)
- `YYYY/MM/DD` (如: 2024/01/01)

## 时间戳支持

- 支持秒级时间戳 (10位数字)
- 支持毫秒级时间戳 (13位数字，自动转换)

## 依赖

只使用Python标准库，无需安装额外依赖。