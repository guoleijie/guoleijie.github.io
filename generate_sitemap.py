#!/usr/bin/env python3
"""自动生成 sitemap.xml，扫描所有 HTML 文件"""
import glob
import re
from datetime import datetime, timezone

BASE_URL = "https://guoleijie.github.io"

def get_changefreq(filepath):
    if "daily-report" in filepath:
        return "monthly"
    elif "blog" in filepath:
        return "weekly"
    else:
        return "weekly"

def get_priority(filepath):
    if filepath == "index.html":
        return "1.0"
    elif filepath == "blog/index.html":
        return "0.9"
    elif "daily-report" in filepath:
        return "0.7"
    else:
        return "0.8"

def extract_lastmod(filepath):
    """从文件内容提取日期，用于 lastmod"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        # 尝试从日报标题提取日期
        m = re.search(r'(\d{4})-(\d{2})-(\d{2})', filepath)
        if m:
            return f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        return datetime.now().strftime('%Y-%m-%d')
    except:
        return datetime.now().strftime('%Y-%m-%d')

def main():
    # 收集所有HTML文件
    files = set()
    for pattern in ['**/*.html']:
        files.update(glob.glob(pattern, recursive=True))
    
    # 排除
    files = {f for f in files if not f.startswith('.')}
    
    urls = []
    for f in sorted(files):
        url = f"{BASE_URL}/{f}" if f != "index.html" else BASE_URL
        urls.append((url, f))
    
    # 生成XML
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url, filepath in urls:
        changefreq = get_changefreq(filepath)
        priority = get_priority(filepath)
        lastmod = extract_lastmod(filepath)
        xml += f'  <url>\n'
        xml += f'    <loc>{url}</loc>\n'
        xml += f'    <lastmod>{lastmod}</lastmod>\n'
        xml += f'    <changefreq>{changefreq}</changefreq>\n'
        xml += f'    <priority>{priority}</priority>\n'
        xml += f'  </url>\n'
    xml += '</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write(xml)
    
    print(f"✅ sitemap.xml 已生成，包含 {len(urls)} 个URL")

if __name__ == '__main__':
    main()
