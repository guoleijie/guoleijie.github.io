#!/bin/bash

# 个人主页部署脚本
# 使用方法：./deploy.sh

set -e

echo "🚀 开始部署个人主页..."

# 进入项目目录
cd ~/.openclaw/workspace/personal-homepage

# 检查是否有修改
if git diff-index --quiet HEAD --; then
    echo "✅ 没有需要提交的修改"
else
    echo "📝 提交修改..."
    git add .
    git commit -m "Update: $(date '+%Y-%m-%d %H:%M:%S')"
fi

# 推送到 GitHub
echo "📤 推送到 GitHub..."
git push origin main

echo "✅ 部署完成！"
echo "🌐 请访问：https://guoleijie.github.io"
echo "⏱️  GitHub Pages 可能需要 1-2 分钟生效"
