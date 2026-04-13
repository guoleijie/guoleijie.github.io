#!/usr/bin/env python3
"""
自动更新首页(index.html)和日报列表页(blog/index.html)的日报卡片。

用法:
  python3 update_homepage_reports.py <cn_json_path>

脚本会:
  1. 读取 cn.json 获取当天日报数据
  2. 自动推断期数（扫描现有卡片最大期数 + 1）
  3. 更新首页 hero 按钮 + 日报卡片（保持最新3篇）
  4. 更新日报列表页（在对应月份顶部插入新卡片）
"""

import json
import re
import sys
from datetime import datetime
from pathlib import Path

WEEKDAYS = {0: "周一", 1: "周二", 2: "周三", 3: "周四", 4: "周五", 5: "周六", 6: "周日"}
SITE_DIR = Path(__file__).parent


def get_weekday_cn(date_str: str) -> str:
    return WEEKDAYS[datetime.strptime(date_str, "%Y-%m-%d").weekday()]


def find_issue_numbers(html: str) -> list[int]:
    """从 HTML 中提取所有日报期数"""
    return [int(m) for m in re.findall(r'第(\d+)期', html)]


def build_homepage_card(date_str: str, issue_num: int, summaries: list) -> str:
    """首页日报卡片（带摘要列表）"""
    y, m, d = date_str[:4], date_str[5:7], date_str[8:10]
    weekday = get_weekday_cn(date_str)
    items = "\n".join(f"            <li>{s}</li>" for s in summaries[:3])
    return (
        f'        <a href="/blog/{y}/{m}/{d}-daily-report.html" class="report-card">\n'
        f'          <div class="report-date">\n'
        f'            <i data-lucide="calendar" style="width:14px;height:14px;"></i> <span>{y}年{int(m)}月{int(d)}日</span>\n'
        f'          </div>\n'
        f'          <h3>再保险日报 · 第{issue_num}期 | {y}年{m}月{d}日（{weekday}）</h3>\n'
        f'          <ul class="report-summary">\n'
        f'{items}\n'
        f'          </ul>\n'
        f'          <span class="report-link"><span data-i18n="reports_read_more">阅读全文</span> <i data-lucide="arrow-right" style="width:14px;height:14px;"></i></span>\n'
        f'        </a>'
    )


def build_blog_card(date_str: str, issue_num: int, total: int, industry: int, tech: int) -> str:
    """日报列表页卡片（简洁风格）"""
    y, m, d = date_str[:4], date_str[5:7], date_str[8:10]
    weekday = get_weekday_cn(date_str)
    return (
        f'                <a href="/blog/{y}/{m}/{d}-daily-report.html" class="report-card">\n'
        f'                    <div class="report-date">\n'
        f'                        <span class="day">{int(d)}</span>\n'
        f'                        <span class="month">{m}月</span>\n'
        f'                    </div>\n'
        f'                    <div class="report-info">\n'
        f'                        <h4>再保险行业日报 第{issue_num}期 | {y}年{m}月{d}日（{weekday}）</h4>\n'
        f'                        <p>共 {total} 条新闻：{industry} 条行业新闻，{tech} 条科技前沿</p>\n'
        f'                    </div>\n'
        f'                    <i data-lucide="arrow-right" class="report-arrow" style="width:18px;height:18px;"></i>\n'
        f'                </a>'
    )


def update_homepage(data: dict, date_str: str):
    """更新首页 index.html"""
    index_file = SITE_DIR / "index.html"
    html = index_file.read_text(encoding="utf-8")

    y, m, d = date_str[:4], date_str[5:7], date_str[8:10]

    # 推断新期数
    existing_issues = find_issue_numbers(html)
    issue_num = max(existing_issues) + 1 if existing_issues else 1

    # 摘要：行业前2 + 科技前1
    industry_titles = [n["title_cn"] for n in data.get("industry_news_cn", [])[:2]]
    tech_titles = [n["title_cn"] for n in data.get("tech_news_cn", [])[:1]]
    summaries = industry_titles + tech_titles

    # 检查是否已存在同一天的卡片（避免重复插入）
    today_url = f'/blog/{y}/{m}/{d}-daily-report.html'
    if today_url in html:
        print(f"  ⏭ 首页已存在 {date_str} 的卡片，跳过更新")
        return

    # --- 1. 更新 hero 按钮 ---
    html = re.sub(
        r'(<a href=")/blog/\d{4}/\d{2}/\d{2}-daily-report\.html(" class="btn btn-primary">)',
        f'\\1/blog/{y}/{m}/{d}-daily-report.html\\2',
        html, count=1
    )
    print(f"  ✓ Hero按钮 → /blog/{y}/{m}/{d}-daily-report.html")

    # --- 2. 替换 reports-grid 内的卡片区域 ---
    # 定位 reports-grid 区域
    grid_start = html.find('<div class="reports-grid">')
    if grid_start == -1:
        print("  ✗ 未找到 reports-grid")
        return

    # 找到 grid 闭合（下一个同级 div 的开始作为终点）
    grid_close_area = html[grid_start:]
    # reports-grid 后面跟着 </div>\n      <div style="text-align:center
    grid_end_marker = '\n      <div style="text-align:center'
    end_offset = grid_close_area.find(grid_end_marker)
    if end_offset == -1:
        print("  ✗ 未找到 grid 结束标记")
        return

    grid_block = grid_close_area[:end_offset + len(grid_end_marker)]

    # 从现有 grid 中提取卡片（非贪婪匹配每个 <a ... report-card">...</a>）
    card_pattern = re.compile(
        r'(<a href="/blog/\d{4}/\d{2}/\d{2}-daily-report\.html" class="report-card">.*?</a>)',
        re.DOTALL
    )
    existing_cards = card_pattern.findall(grid_block)

    # 保留最新的2篇，加上新的1篇 = 3篇
    kept = existing_cards[:2]
    new_card = build_homepage_card(date_str, issue_num, summaries)

    new_grid_block = f'<div class="reports-grid">\n\n{new_card}\n\n' + "\n\n".join(kept) + "\n\n"

    html = html[:grid_start] + new_grid_block + html[grid_start + end_offset:]
    print(f"  ✓ 首页卡片 → 第{issue_num}期（共{len(kept)+1}篇）")

    index_file.write_text(html, encoding="utf-8")


def update_blog_list(data: dict, date_str: str):
    """更新日报列表页 blog/index.html"""
    list_file = SITE_DIR / "blog" / "index.html"
    html = list_file.read_text(encoding="utf-8")

    y, m, d = date_str[:4], date_str[5:7], date_str[8:10]

    # 推断新期数
    existing_issues = find_issue_numbers(html)
    issue_num = max(existing_issues) + 1 if existing_issues else 1

    total = data.get("total_news", 0)
    industry = data.get("industry_news_count", 0)
    tech = data.get("tech_news_count", 0)

    new_card = build_blog_card(date_str, issue_num, total, industry, tech)

    # 检查是否已存在同一天的卡片
    today_url = f'/blog/{y}/{m}/{d}-daily-report.html'
    if today_url in html:
        print(f"  ⏭ 列表页已存在 {date_str} 的卡片，跳过更新")
        return

    # 查找月份区域
    month_header = f'<h3>📅 {y}年{int(m):02d}月</h3>'
    month_pos = html.find(month_header)
    if month_pos == -1:
        # 月份标题不存在，自动创建新的月份区块
        print(f"  ➕ 月份 {y}年{m}月 不存在，自动创建")
        new_month_block = f'''            <div class="month-group">
                <h3>📅 {y}年{int(m):02d}月</h3>

{new_card}

            </div>'''
        # 在第一个 month-group 之前插入
        first_month = html.find('<div class="month-group">')
        if first_month == -1:
            print("  ✗ 未找到任何月份区块")
            return
        html = html[:first_month] + new_month_block + "\n" + html[first_month:]
        list_file.write_text(html, encoding="utf-8")
        print(f"  ✓ 新月份 {y}年{m}月 已创建并插入第{issue_num}期")
        return

    # 在该月份的第一个 <a href="/blog/ 前插入
    first_card_pos = html.find('<a href="/blog/', month_pos)
    if first_card_pos == -1:
        print("  ✗ 未找到现有卡片")
        return

    html = html[:first_card_pos] + new_card + "\n\n" + html[first_card_pos:]
    print(f"  ✓ 列表页 → 第{issue_num}期插入到 {y}年{m}月")

    list_file.write_text(html, encoding="utf-8")


def main():
    if len(sys.argv) < 2:
        print("用法: python3 update_homepage_reports.py <cn_json_path>")
        sys.exit(1)

    cn_json = Path(sys.argv[1])
    if not cn_json.exists():
        print(f"错误: {cn_json} 不存在")
        sys.exit(1)

    with open(cn_json, "r", encoding="utf-8") as f:
        data = json.load(f)

    date_str = data["date"]
    print(f"\n📋 自动更新日报页面 - {date_str}")
    print("=" * 50)

    update_homepage(data, date_str)
    update_blog_list(data, date_str)

    print("=" * 50)
    print("✅ 完成！请执行 git add & git push")


if __name__ == "__main__":
    main()
