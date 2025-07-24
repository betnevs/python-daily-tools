#!/bin/bash
# PTL 安装脚本

echo "正在安装 PTL (Python Tools Library)..."

# 检查是否有写入权限
if [ ! -w "/usr/local/bin" ]; then
    echo "需要管理员权限来安装到 /usr/local/bin"
    echo "请使用 sudo 运行此脚本: sudo ./install.sh"
    echo ""
    echo "或者手动安装:"
    echo "1. 复制 ptl 文件到您的 PATH 中的任意目录"
    echo "2. 给予执行权限: chmod +x ptl"
    echo "3. 或者创建别名: alias ptl='python /path/to/ptl'"
    exit 1
fi

# 复制文件到系统路径
cp ptl /usr/local/bin/ptl
chmod +x /usr/local/bin/ptl

echo "安装完成！"
echo ""
echo "现在您可以在任何地方使用 ptl 命令了:"
echo "  ptl md5 \"hello world\""
echo "  ptl url \"hello world\""
echo "  ptl b64 \"hello world\""
echo "  ptl help"
echo ""
echo "如需卸载，请删除文件: sudo rm /usr/local/bin/ptl"