#!/bin/bash
# 一键部署脚本 - GitHub Pages
# 使用方法：./push-to-github.sh

set -e

echo "🚀 准备推送到 GitHub..."

# 配置 Git
cd ~/.openclaw/workspace/personal-homepage

# 检查远程仓库
if git remote | grep -q "origin"; then
    echo "✅ 远程仓库已配置"
else
    echo "❌ 远程仓库未配置"
    exit 1
fi

# 推送到 GitHub
echo ""
echo "📦 推送代码..."
git push -u origin main

echo ""
echo "✅ 推送成功！"
echo ""
echo "🌐 访问你的个人主页："
echo "   https://guoleijie.github.io"
echo ""
echo "⏱️  GitHub Pages 需要 1-2 分钟生效"
echo ""
