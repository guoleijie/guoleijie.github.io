#!/bin/bash
# Deploy to Cloudflare Pages (国内加速)
# Usage: bash deploy_to_cf_pages.sh

set -e

SITE_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_NAME="guoleijie-site"

# 读取 token
if [ -f "$HOME/.openclaw/openclaw.json" ]; then
  TOKEN=$(python3 -c "import json; d=json.load(open('$HOME/.openclaw/openclaw.json')); print(d.get('env',{}).get('CLOUDFLARE_API_TOKEN',''))")
fi

if [ -z "$TOKEN" ]; then
  echo "❌ 未找到 CLOUDFLARE_API_TOKEN"
  exit 1
fi

echo "🚀 正在部署到 Cloudflare Pages..."

# 清理代理避免上传失败
unset http_proxy https_proxy HTTP_PROXY HTTPS_PROXY all_proxy ALL_PROXY

export CLOUDFLARE_API_TOKEN="$TOKEN"
npx wrangler pages deploy "$SITE_DIR" --project-name="$PROJECT_NAME" --branch=main --commit-dirty=true 2>&1

echo "✅ CF Pages 部署完成"
