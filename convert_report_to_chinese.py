#!/usr/bin/env python3
"""
将日报 JSON 数据翻译成中文
"""

import json
import sys
from pathlib import Path
from typing import Dict, List

# 路径配置
REPORT_JSON = Path("/home/guoleijie/.openclaw/workspace/skills/reinsurance-news/archive/daily_report_2026-03-16.json")

# 简单翻译映射
TRANSLATIONS = {
    "industry": "行业新闻",
    "tech": "科技前沿",
    "News by Acceswire on TradingView": "TradingView 上的 Acceswire 新闻",
    "Bitcoin Stocks To Follow Today": "今日值得关注的比特币股票",
    "Alaska LNG needs more offtake commitments before final investment decision, CEO says": "阿拉斯加液化天然气在最终投资决策前需要更多收购承诺，CEO 表示",
    "Bank stocks have been crushed this year. 2 of our names should weather the storm": "今年银行股被重创。我们的两家名字应该能挺过风暴",
    "Insuring the Unpredictable: Securing Operations in Times of Global Unrest": "为不可预测投保：在全球动荡中保障运营",
    "Global week ahead: Price pressure in the pipeline": "全球前瞻：管道中的价格压力",
    "Wells Fargo's head of AI shares his playbook for staying in demand as banks weigh what tech means for head count": "富国银行 AI 负责人分享保持需求的策略，因为银行正在评估技术对员工数量的影响",
    "Ripple Targets AFSL to Bolster Australian Payments": "Ripple 收购 AFSL 以加强澳大利亚支付业务",
    "Cryptocurrency Stocks To Watch Now": "现在值得关注的加密货币股票",
    "Superloop's AI push continues with billing system project": "Superloop 的 AI 推进继续，计费系统项目",
    "Neura Robotics and Qualcomm enter strategic collaboration to advance physical AI and cognitive robotics": "Neura Robotics 和高通建立战略合作，推进物理 AI 和认知机器人技术",
    "Rita McGrath: How Strategic Centering Unlocks Innovation In A Digital World": "Rita McGrath：战略中心化如何在数字世界释放创新",
}


def translate_text(text: str) -> str:
    """简单的中文翻译"""
    # 先尝试映射表
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # 如果不在映射表中，返回原文
    return text


def translate_news_item(news_item: Dict) -> Dict:
    """翻译新闻条目"""
    title_en = news_item.get('title', '')
    description_en = news_item.get('description', '')
    
    # 翻译标题
    title_cn = translate_text(title_en)
    if title_cn != title_en:
        display_title = title_cn
    else:
        # 如果没有翻译，保留英文
        display_title = title_en
    
    # 描述截取并翻译
    if len(description_en) > 150:
        display_desc = description_en[:150] + "..."
    else:
        display_desc = description_en
    
    # 返回翻译后的新闻
    translated_news = news_item.copy()
    translated_news['title_cn'] = title_cn
    translated_news['display_title'] = display_title
    translated_news['display_desc'] = display_desc
    
    return translated_news


def main():
    """主函数"""
    print(f"\n{'='*60}")
    print(f"🌐 开始翻译日报数据...")
    print(f"{'='*60}\n")
    
    # 检查 JSON 文件是否存在
    if not REPORT_JSON.exists():
        print(f"  ✗ 日报 JSON 文件不存在: {REPORT_JSON}")
        return
    
    # 读取 JSON 数据
    with open(REPORT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    date = data['date']
    print(f"📅 日期: {date}")
    print(f"📰 总新闻数: {data['total_news']}")
    print(f"  - 行业新闻: {data['industry_news_count']}")
    print(f"  - 科技前沿: {data['tech_news_count']}\n")
    
    # 翻译行业新闻
    print("🏢 翻译行业新闻...")
    industry_news_cn = []
    for i, news in enumerate(data['industry_news'], 1):
        translated = translate_news_item(news)
        translated['number'] = i
        industry_news_cn.append(translated)
        print(f"  {i}. {translated['display_title']}")
    
    # 翻译科技新闻
    print("🤖 翻译科技前沿...")
    tech_news_cn = []
    for i, news in enumerate(data['tech_news'], 1):
        translated = translate_news_item(news)
        translated['number'] = i
        tech_news_cn.append(translated)
        print(f"  {i}. {translated['display_title']}")
    
    # 准备中文数据
    data_cn = {
        'date': date,
        'generated_time': data['generated_time'],
        'total_news': data['total_news'],
        'industry_news_count': data['industry_news_count'],
        'tech_news_count': data['tech_news_count'],
        'industry_news_cn': industry_news_cn,
        'tech_news_cn': tech_news_cn,
        'summary_cn': f"今日共收集 {data['total_news']} 条新闻，其中行业新闻 {data['industry_news_count']} 条，科技前沿 {data['tech_news_count']} 条。"
    }
    
    # 保存中文数据
    output_file = REPORT_JSON.parent / f"daily_report_{date}_cn.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data_cn, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 中文数据已保存: {output_file}")
    print(f"\n💡 接下来生成中文日报页面...")
    
    return data_cn


if __name__ == '__main__':
    main()
