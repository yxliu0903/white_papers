#!/bin/bash

# Cognition JSON文件动态展示系统启动脚本

echo "=========================================="
echo "  Cognition JSON文件动态展示系统"
echo "=========================================="
echo ""

# 切换到正确的目录
cd /mnt/iem-nas/home/liuyixiu/AI_Archer_local/white_papers

# 检查Python是否安装
if ! command -v python &> /dev/null; then
    echo "错误: 未找到Python，请先安装Python"
    exit 1
fi

# 检查展示页面是否存在
if [ ! -f "json_files_display.html" ]; then
    echo "错误: 未找到 json_files_display.html 文件"
    exit 1
fi

# 检查cognition目录是否存在
if [ ! -d "cognition" ]; then
    echo "错误: 未找到 cognition 目录"
    exit 1
fi

# 统计JSON文件数量
JSON_COUNT=$(find cognition -name "*.json" | wc -l)
echo "发现 $JSON_COUNT 个JSON文件在 cognition 目录中"
echo ""

# 检查端口是否被占用
PORT=8000
if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
    echo "警告: 端口 $PORT 已被占用"
    echo "正在尝试使用端口 8001..."
    PORT=8001
    if lsof -Pi :$PORT -sTCP:LISTEN -t >/dev/null ; then
        echo "错误: 端口 8001 也被占用，请手动关闭占用端口的程序"
        exit 1
    fi
fi

echo "正在启动HTTP服务器..."
echo "服务器地址: http://localhost:$PORT"
echo "展示页面: http://localhost:$PORT/json_files_display.html"
echo ""
echo "使用说明:"
echo "1. 打开展示页面后，点击'选择JSON文件'按钮"
echo "2. 选择 cognition 目录中的所有JSON文件"
echo "3. 点击'开始动态展示'按钮"
echo "4. 观察纸张一页一页地动态添加，营造错乱感"
echo ""
echo "按 Ctrl+C 停止服务器"
echo ""

# 启动HTTP服务器
python -m http.server $PORT 