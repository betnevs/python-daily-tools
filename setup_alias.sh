#!/bin/bash
# 设置 ptl 别名的脚本

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PTL_PATH="$SCRIPT_DIR/ptl"

echo "正在设置 ptl 别名..."

# 检查shell类型并添加别名
if [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
elif [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
else
    SHELL_RC="$HOME/.profile"
fi

# 检查别名是否已存在
if grep -q "alias ptl=" "$SHELL_RC" 2>/dev/null; then
    echo "ptl 别名已存在于 $SHELL_RC"
else
    echo "alias ptl='python $PTL_PATH'" >> "$SHELL_RC"
    echo "别名已添加到 $SHELL_RC"
fi

echo ""
echo "请运行以下命令使别名生效:"
echo "  source $SHELL_RC"
echo ""
echo "或者重新打开终端"
echo ""
echo "然后您就可以使用:"
echo "  ptl md5 \"hello world\""
echo "  ptl help"