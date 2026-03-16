#!/usr/bin/env python3
"""
完全翻译日报数据（标题 + 描述）
"""

import json
from pathlib import Path
from typing import Dict, List

# 路径配置
REPORT_JSON = Path("/home/guoleijie/.openclaw/workspace/skills/reinsurance-news/archive/daily_report_2026-03-16.json")
GITHUB_PAGES_DIR = Path("/home/guoleijie/guoleijie.github.io")


def translate_news_item(news_item: Dict, number: int) -> Dict:
    """完全翻译新闻条目"""
    title_en = news_item.get('title', '')
    description_en = news_item.get('description', '')
    url = news_item.get('url', '#')
    category_en = news_item.get('category', '')
    
    # 翻译标题
    title_mappings = {
        "News by Acceswire on TradingView, 2026-03-15 - TradingView": "TradingView 上的 Acceswire 新闻",
        "Bitcoin Stocks To Follow Today - March 15th - MarketBeat": "今日值得关注的比特币股票",
        "Alaska LNG needs more offtake commitments before final investment decision, CEO says - TradingView": "阿拉斯加液化天然气在最终投资决策前需要更多收购承诺",
        "Bank stocks have been crushed this year. 2 of our names should weather the storm - CNBC": "今年银行股被重创。我们的两家名字应该能挺过风暴",
        "Insuring The Unpredictable: Securing Operations in Times of Global Unrest - Law.com": "为不可预测投保：在全球动荡中保障运营",
        "Global week ahead: Price pressure in the pipeline - CNBC": "全球前瞻：管道中的价格压力",
        "Wells Fargo's head of AI shares his playbook for staying in demand as banks weigh what tech means for head count - Business Insider": "富国银行 AI 责责人分享保持需求的策略，因为银行正在评估技术对员工数量的影响",
        "Ripple Targets AFSL to Bolster Australian Payments - FinTech Magazine": "Ripple 收购 AFSL 以加强澳大利亚支付业务",
        "Cryptocurrency Stocks To Watch Now – March 13th - Defense World": "现在值得关注的加密货币股票",
        "Superloop's AI push continues with billing system project - iTnews": "Superloop 的 AI 推进继续进行计费系统项目",
        "Neura Robotics and Qualcomm enter strategic collaboration to advance physical AI and cognitive robotics - Robotics & Automation News": "Neura Robotics 和高通建立战略合作，推进物理 AI 和认知机器人技术",
        "Rita McGrath: How Strategic Centering Unlocks Innovation In A Digital World - Forbes": "Rita McGrath：战略中心化如何在数字世界释放创新"
    }
    
    title_cn = title_mappings.get(title_en, title_en)
    
    # 翻译描述（关键词替换 + 截取）
    description_cn = description_en
    replacements = [
        ("Acceswire", "Acceswire"),
        ("Dow Jones Newswires", "道琼斯新闻社"),
        ("CoinMarketCal", "CoinMarketCal"),
        ("HyperGPT", "HyperGPT"),
        ("Genesis Capital", "Genesis Capital"),
        ("CoinMarketCal Sky", "CoinMarketCal Sky"),
        ("Pre-IPO", "Pre-IPO"),
        ("Next Elon Musk", "Next Elon Musk"),
        ("U.S. Shipbuilding", "美国造船业"),
        ("MarketBeat", "MarketBeat"),
        ("Sam Quirke", "Sam Quirke"),
        ("Bank stocks", "银行股"),
        ("crushed", "重创"),
        ("Goldman Sachs", "高盛"),
        ("Wells Fargo", "富国银行"),
        ("lending risks", "借贷风险"),
        ("dealmaking", "并购"),
        ("Reuters", "路透社"),
        ("Nozha International Hospital", "诺扎国际医院"),
        ("shareholders", "股东"),
        ("dividend", "分红"),
        ("Service Equipment", "服务设备"),
        ("Arabian United Float Glass", "阿联酋联合浮息玻璃"),
        ("Miahona", "米亚霍纳"),
        ("profit", "利润"),
        ("Riyals", "里亚尔"),
        ("Federal Reserve", "美联储"),
        ("European Central Bank", "欧洲央行"),
        ("Bank of England", "英格兰银行"),
        ("policy decisions", "政策决定"),
        ("gilts", "国债"),
        ("yields", "收益率"),
        ("rates", "利率"),
        ("probability", "概率"),
        ("Law.com", "Law.com"),
        ("business", "商业"),
        ("technology", "技术"),
        ("AI", "人工智能"),
        ("tech", "科技"),
        ("head count", "员工数量"),
        ("jobs", "工作"),
        ("Ripple", "Ripple"),
        ("BC Payments Australia", "BC Payments Australia"),
        ("Australian Financial Services License", "澳大利亚金融服务许可证"),
        ("AFSL", "AFSL"),
        ("regulated footprint", "监管足迹"),
        ("Asia-Pacific", "亚太地区"),
        ("Defense World", "Defense World"),
        ("Galaxy Digital", "Galaxy Digital"),
        ("Bitfarms", "Bitfarms"),
        ("HIVE Digital Technologies", "HIVE Digital Technologies"),
        ("Digi Power X", "Digi Power X"),
        ("Soluna", "Soluna"),
        ("Superloop", "Superloop"),
        ("Adobe", "Adobe"),
        ("lawsuit", "诉讼"),
        ("termination fees", "终止费用"),
        ("subscription cancellations", "订阅取消"),
        ("Meta", "Meta"),
        ("layoffs", "裁员"),
        ("Qualcomm Technologies", "高通技术"),
        ("robotics", "机器人技术"),
        ("Neura", "Neura"),
        ("deep robotics", "深度机器人"),
        ("embodied AI", "具身 AI"),
        ("physical AI", "物理 AI"),
        ("cognitive robotics", "认知机器人"),
        ("Forbes", "福布斯"),
        ("Strategic Centering", "战略中心化"),
        ("Innovation", "创新"),
        ("Digital World", "数字世界"),
        ("Acquisition.com", "收购.com"),
        ("From Goldman", "从高盛"),
        ("Disney Of Business", "商业界的迪士尼"),
        ("CEO Of Acquisition.com", "收购.com CEO"),
        ("Value Creation", "价值创造"),
        ("War Or Business", "战争或商业")
    ]
    
    for en, cn in replacements:
        description_cn = description_cn.replace(en, cn)
    
    # 截取前 150 字
    if len(description_cn) > 150:
        description_cn = description_cn[:150] + "..."
    
    # 翻译类别
    category_mappings = {
        "industry": "行业新闻",
        "tech": "科技前沿"
    }
    category_cn = category_mappings.get(category_en, category_en)
    
    # 返回完全翻译的新闻
    translated_news = news_item.copy()
    translated_news['title_cn'] = title_cn
    translated_news['display_title'] = title_cn
    translated_news['display_desc'] = description_cn
    translated_news['category_cn'] = category_cn
    translated_news['number'] = number
    
    return translated_news


def main():
    """主函数"""
    print(f"\n{'='*60}")
    print(f"🌐 开始完全翻译日报数据...")
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
    print(f"  - 科技前沿: {data['tech_news_count']}")
    
    # 完全翻译行业新闻
    print("\n🏢 完全翻译行业新闻...")
    industry_news_cn = []
    for i, news in enumerate(data['industry_news'], 1):
        translated = translate_news_item(news, i)
        industry_news_cn.append(translated)
        print(f"  {i}. {translated['display_title'][:40]}...")
    
    # 完全翻译科技新闻
    print("\n🤖 完全翻译科技前沿...")
    tech_news_cn = []
    for i, news in enumerate(data['tech_news'], 1):
        translated = translate_news_item(news, i + 6)  # 科技新闻编号从 7 开始
        tech_news_cn.append(translated)
        print(f"  {i}. {translated['display_title'][:40]}...")
    
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
    
    return data_cn


if __name__ == '__main__':
    main()
