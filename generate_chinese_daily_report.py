#!/usr/bin/env python3
"""
生成中文日报 HTML 页面
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict

# 路径配置
REPORT_JSON_CN = Path("/home/guoleijie/.openclaw/workspace/skills/reinsurance-news/archive/daily_report_2026-03-16_cn.json")
GITHUB_PAGES_DIR = Path("/home/guoleijie/guoleijie.github.io")


def render_news_items(news_list):
    """渲染新闻列表项 HTML（中文版）"""
    if not news_list:
        return "<p>暂无新闻</p>"

    items_html = []
    for i, news in enumerate(news_list, 1):
        title = news.get('display_title', news.get('title', '无标题'))
        description = news.get('display_desc', news.get('description', ''))
        url = news.get('url', '#')
        category_cn = news.get('category', '')

        # 新闻标题样式
        title_html = f"""<div class="news-number">{i}.</div>
<div class="news-content">
    <div class="news-title" data-category="{category_cn}">
      <a href="{url}" target="_blank">{title}</a>
    </div>
    <div class="news-description">{description}</div>
    <div class="news-meta">
      <span class="news-category">{category_cn}</span>
    </div>
</div>"""
        items_html.append(title_html)

    return '\n'.join(items_html)


def render_github_report(data: Dict, date: str):
    """渲染 GitHub Pages 日报 HTML（中文版）"""
    
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    
    # 渲染新闻列表
    industry_html = render_news_items(data['industry_news_cn'])
    tech_html = render_news_items(data['tech_news_cn'])
    
    # 生成完整 HTML
    report_html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>日报 - {date} | 梦醒</title>
    <link rel="stylesheet" href="/assets/css/report.css">
    <link href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <!-- 进度条 -->
    <div class="progress-bar"></div>

    <!-- 导航栏 -->
    <nav>
        <a href="/" class="nav-logo">
            <i data-lucide="code-2" class="icon"></i>
            <span>梦醒</span>
        </a>
        <button class="menu-toggle" id="menuToggle">
            <i data-lucide="menu"></i>
        </button>
        <ul class="nav-links" id="navLinks">
            <li><a href="/">首页</a></li>
            <li><a href="/blog/">博客</a></li>
            <li><a href="/blog/{year}/{month}/">{year}年{month}月</a></li>
        </ul>
    </nav>

    <!-- 日报内容 -->
    <article class="daily-report">
        <header class="report-header">
            <h1>📰 再保险行业日报 - {date}</h1>
            <div class="report-meta">
                <span class="date">
                    <i data-lucide="calendar"></i>
                    {year}年{month}月{day}日
                </span>
                <span class="weekday">
                    <i data-lucide="clock"></i>
                    正常
                </span>
            </div>
        </header>

        <section class="report-section">
            <h2><i data-lucide="newspaper"></i> 行业新闻</h2>
            <div class="news-content">
                {industry_html}
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="cpu"></i> 科技前沿</h2>
            <div class="news-content">
                {tech_html}
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="bar-chart-2"></i> 今日总结</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="newspaper"></i>
                    </div>
                    <div class="stat-value">{data['total_news']}</div>
                    <div class="stat-label">总新闻数</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="briefcase"></i>
                    </div>
                    <div class="stat-value">{data['industry_news_count']}</div>
                    <div class="stat-label">行业新闻</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="cpu"></i>
                    </div>
                    <div class="stat-value">{data['tech_news_count']}</div>
                    <div class="stat-label">科技前沿</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="clock"></i>
                    </div>
                    <div class="stat-value">{data['generated_time'].split()[1][:5]}</div>
                    <div class="stat-label">生成时间</div>
                </div>
            </div>
            <div class="summary-text">
                {data['summary_cn']}
            </div>
        </section>

        <footer class="report-footer">
            <p>💡 由 AI 自动生成 - 豆豆（火星王子）</p>
            <div class="navigation">
                <a href="/blog/{year}/{month}/" class="nav-link">
                    <i data-lucide="arrow-left"></i>
                    {year}年{month}月日报
                </a>
                <a href="/blog/" class="nav-link">
                    <i data-lucide="layout-grid"></i>
                    所有日报
                </a>
                <a href="/" class="nav-link">
                    <i data-lucide="home"></i>
                    返回首页
                </a>
            </div>
        </footer>
    </article>

    <script src="/assets/js/main.js"></script>
    <script>lucide.createIcons();</script>
</body>
</html>"""
    
    return report_html


def update_blog_index(github_pages_dir: Path, date: str, data: Dict):
    """更新博客列表页（中文版）"""
    
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    
    blog_index_file = github_pages_dir / "blog" / "index.html"
    
    # 检查博客索引文件是否存在
    if not blog_index_file.exists():
        print("  ✗ 博客索引文件不存在，跳过更新")
        return
    
    # 读取现有博客索引
    with open(blog_index_file, 'r', encoding='utf-8') as f:
        blog_index_content = f.read()
    
    # 检查该月份的部分是否存在
    if f'<h3>📅 {year}年{month}月</h3>' not in blog_index_content:
        # 月份不存在，添加新的月份部分
        new_month_section = f"""        <section class="blog-list">
            <!-- {year}年{month}月 -->
            <div class="blog-month">
                <h3>📅 {year}年{month}月</h3>
                <div class="blog-posts">
                    <a href="/blog/{year}/{month}/{day}-daily-report.html" class="blog-post">
                        <div class="blog-date">
                            <span class="day">{day}</span>
                            <span class="month">{month}月</span>
                        </div>
                        <div class="blog-content">
                            <h4>再保险行业日报 - {date}</h4>
                            <p>{data['summary_cn']}</p>
                        </div>
                        <i data-lucide="arrow-right" class="blog-arrow"></i>
                    </a>
                </div>
            </div>
        </section>"""
        # 在"blog-list"的最后添加新的月份
        blog_index_content = blog_index_content.replace(
            '</section>\n    </div>\n</div>',
            f'{new_month_section}\n    </div>\n</div>'
        )
    else:
        # 月份已存在，添加新的日报卡片
        blog_card = f"""                    <a href="/blog/{year}/{month}/{day}-daily-report.html" class="blog-post">
                        <div class="blog-date">
                            <span class="day">{day}</span>
                            <span class="month">{month}月</span>
                        </div>
                        <div class="blog-content">
                            <h4>再保险行业日报 - {date}</h4>
                            <p>{data['summary_cn']}</p>
                        </div>
                        <i data-lucide="arrow-right" class="blog-arrow"></i>
                    </a>"""
        # 在"blog-posts"中的月份部分后面添加
        blog_index_content = blog_index_content.replace(
            f'</div>\n                </div>\n            </div>',
            f'{blog_card}\n                </div>\n            </div>'
        )
    
    # 保存博客索引
    with open(blog_index_file, 'w', encoding='utf-8') as f:
        f.write(blog_index_content)
    
    print(f"  ✓ 博客列表已更新")


def main():
    """主函数"""
    print(f"\n{'='*60}")
    print(f"🌐 开始生成中文日报 HTML...")
    print(f"{'='*60}\n")
    
    # 检查中文 JSON 文件是否存在
    if not REPORT_JSON_CN.exists():
        print(f"  ✗ 中文日报 JSON 文件不存在: {REPORT_JSON_CN}")
        return
    
    # 读取中文 JSON 数据
    with open(REPORT_JSON_CN, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    date = data['date']
    
    print(f"📅 日期: {date}")
    print(f"📰 总新闻数: {data['total_news']}")
    print(f"  - 行业新闻: {data['industry_news_count']}")
    print(f"  - 科技前沿: {data['tech_news_count']}")
    
    # 生成日报 HTML
    report_html = render_github_report(data, date)
    
    # 创建目录
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    
    blog_dir = GITHUB_PAGES_DIR / "blog" / year / month
    blog_dir.mkdir(parents=True, exist_ok=True)
    
    # 保存日报文件
    report_file = blog_dir / f"{day}-daily-report.html"
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(report_html)
    
    print(f"\n✅ 日报 HTML 已生成: {report_file}")
    
    # 更新博客列表
    update_blog_index(GITHUB_PAGES_DIR, date, data)
    
    print(f"\n{'='*60}")
    print(f"✅ 中文日报 HTML 生成完成！")
    print(f"{'='*60}\n")
    print(f"🌐 访问: https://guoleijie.github.io/blog/{year}/{month}/{day}-daily-report.html")
    print(f"\n💡 请执行:")
    print(f"   cd {GITHUB_PAGES_DIR}")
    print(f"   git add .")
    print(f"   git commit -m 'Add Chinese daily report {date}'")
    print(f"   git push origin master")


if __name__ == '__main__':
    main()
