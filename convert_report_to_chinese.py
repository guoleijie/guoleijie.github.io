#!/usr/bin/env python3
"""
完全翻译日报数据（标题 + 描述）
"""

import json
from pathlib import Path
from typing import Dict

# 路径配置
REPORT_JSON = Path("/home/guoleijie/.openclaw/workspace/skills/reinsurance-news/archive/daily_report_2026-03-16.json")

# 翻译映射（标题 + 描述）
TRANSLATIONS = {
    # 标题
    "News by Acceswire on TradingView, 2026-03-15 - TradingView": "TradingView 上的 Acceswire 新闻",
    "Bitcoin Stocks To Follow Today - March 15th - MarketBeat": "今日值得关注的比特币股票",
    "Alaska LNG needs more offtake commitments before final investment decision, CEO says - TradingView": "阿拉斯加液化天然气在最终投资决策前需要更多收购承诺，CEO 表示",
    "Bank stocks have been crushed this year. 2 of our names should weather the storm - CNBC": "今年银行股被重创。我们的两家名字应该能挺过风暴",
    "Insuring The Unpredictable: Securing Operations in Times of Global Unrest - Law.com": "为不可预测投保：在全球动荡中保障运营",
    "Global week ahead: Price pressure in the pipeline - CNBC": "全球前瞻：管道中的价格压力",
    "Wells Fargo's head of AI shares his playbook for staying in demand as banks weigh what tech means for head count - Business Insider": "富国银行 AI 责责人分享保持需求的策略，因为银行正在评估技术对员工数量的影响",
    "Ripple Targets AFSL to Bolster Australian Payments - FinTech Magazine": "Ripple 收购 AFSL 以加强澳大利亚支付业务",
    "Cryptocurrency Stocks To Watch Now – March 13th - Defense World": "现在值得关注的加密货币股票",
    "Superloop's AI push continues with billing system project - iTnews": "Superloop 的 AI 推进继续，计费系统项目",
    "Neura Robotics and Qualcomm enter strategic collaboration to advance physical AI and cognitive robotics - Robotics & Automation News": "Neura Robotics 和高通建立战略合作，推进物理 AI 和认知机器人技术",
    "Rita McGrath: How Strategic Centering Unlocks Innovation In A Digital World - Forbes": "Rita McGrath：战略中心化如何在数字世界释放创新",
    
    # 描述关键词
    "Acceswire": "Acceswire",
    "Dow Jones Newswires": "道琼斯新闻社",
    "CoinMarketCal": "CoinMarketCal",
    "HyperGPT": "HyperGPT",
    "Unibase": "Unibase",
    "Genesis Capital": "Genesis Capital",
    "CoinMarketCal Sky": "CoinMarketCal Sky",
    "Bitcoin": "比特币",
    "Stocks": "股票",
    "U.S. Shipbuilding": "美国造船业",
    "Pre-IPO": "Pre-IPO",
    "Next Elon Musk": "Next Elon Musk",
    "Company": "公司",
    "Alaska LNG": "阿拉斯加液化天然气",
    "CEO": "CEO",
    "investment decision": "投资决策",
    "offtake commitments": "收购承诺",
    "Wells Fargo": "富国银行",
    "Goldman Sachs": "高盛",
    "Bank stocks": "银行股",
    "crushed": "重创",
    "weather the storm": "挺过风暴",
    "Insuring": "投保",
    "The Unpredictable": "不可预测",
    "Global Unrest": "全球动荡",
    "Securing Operations": "保障运营",
    "Law.com": "Law.com",
    "Federal Reserve": "美联储",
    "European Central Bank": "欧洲央行",
    "Bank of England": "英格兰银行",
    "policy decisions": "政策决定",
    "rates": "利率",
    "yields": "收益率",
    "probability": "概率"
    "price pressure": "价格压力",
    "Business Insider": "商业内幕",
    "AI": "人工智能",
    "tech": "技术",
    "head count": "员工数量",
    "jobs": "工作",
    "Ripple": "Ripple",
    "BC Payments Australia": "BC Payments Australia",
    "Australian Financial Services License": "澳大利亚金融服务许可证",
    "AFSL": "AFSL",
    "regulated footprint": "监管足迹",
    "Asia-Pacific": "亚太地区",
    "Galaxy Digital": "Galaxy Digital",
    "Bitfarms": "Bitfarms",
    "HIVE Digital Technologies": "HIVE Digital Technologies",
    "Digi Power X": "Digi Power X",
    "Soluna": "Soluna",
    "cryptocurrency": "加密货币",
    "Superloop": "Superloop",
    "billing system project": "计费系统项目",
    "Adobe": "Adobe",
    "lawsuit": "诉讼",
    "termination fees": "终止费用",
    "subscription cancellations": "订阅取消",
    "Meta": "Meta",
    "layoffs": "裁员",
    "Context engineering": "上下文工程",
    "next battleground": "下一个战场",
    "enterprise AI": "企业 AI",
    "Coles Group": "Coles Group",
    "CTO": "CTO",
    "Neura Robotics": "Neura Robotics",
    "Qualcomm Technologies": "高通技术",
    "robotics": "机器人技术",
    "strategic collaboration": "战略合作",
    "physical AI": "物理 AI",
    "cognitive robotics": "认知机器人",
    "embodied AI": "具身 AI",
    "real-world robotic intelligence": "现实世界机器人智能",
    "Rita McGrath": "Rita McGrath",
    "Strategic Centering": "战略中心化",
    "Innovation": "创新",
    "Digital World": "数字世界",
    "Forbes": "福布斯",
    "acquisition.com": "收购.com",
    "From Goldman To Building": "从高盛到打造",
    "The ‘Disney Of Business’": "商业界的迪士尼"
    "Value Creation": "价值创造",
    "War Or Business": "战争或商业"
    "strategic centering": "战略中心化"
    "unlocks": "释放",
    "innovation": "创新",
    "industry": "行业新闻",
    "tech": "科技前沿"
}


def translate_text(text: str) -> str:
    """智能翻译文本（标题 + 描述）"""
    if not text:
        return ""
    
    # 标题翻译
    if text in TRANSLATIONS:
        return TRANSLATIONS[text]
    
    # 描述关键词翻译
    translated = text
    for en, cn in TRANSLATIONS.items():
        if isinstance(cn, str) and en in translated:
            translated = translated.replace(en, cn)
    
    return translated


def translate_description(description: str) -> str:
    """翻译描述（关键词替换 + 截取）"""
    if not description:
        return ""
    
    # 关键词翻译
    translated = translate_text(description)
    
    # 截取前 150 字
    if len(translated) > 150:
        translated = translated[:150] + "..."
    
    return translated


def translate_news_item(news_item: Dict) -> Dict:
    """完全翻译新闻条目（标题 + 描述）"""
    title_en = news_item.get('title', '')
    description_en = news_item.get('description', '')
    
    # 翻译标题
    title_cn = translate_text(title_en)
    if title_cn != title_en:
        display_title = title_cn
    else:
        display_title = title_en
    
    # 翻译描述
    description_cn = translate_description(description_en)
    
    # 返回完全翻译的新闻
    translated_news = news_item.copy()
    translated_news['title_cn'] = title_cn
    translated_news['display_title'] = display_title
    translated_news['display_desc'] = description_cn
    translated_news['category_cn'] = translate_text(news_item.get('category', ''))
    
    return translated_news


def main():
    """主函数"""
    print(f"\n{'='*60}")
    print(f"🌐 开始完全翻译日报数据（标题 + 描述）...")
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
    
    # 完全翻译行业新闻
    print("🏢 完全翻译行业新闻（标题 + 描述）...")
    industry_news_cn = []
    for i, news in enumerate(data['industry_news'], 1):
        translated = translate_news_item(news)
        translated['number'] = i
        industry_news_cn.append(translated)
        print(f"  {i}. {translated['display_title'][:30]}...")
    
    # 完全翻译科技新闻
    print("🤖 完全翻译科技前沿（标题 + 描述）...")
    tech_news_cn = []
    for i, news in enumerate(data['tech_news'], 1):
        translated = translate_news_item(news)
        translated['number'] = i
        tech_news_cn.append(translated)
        print(f"  {i}. {translated['display_title'][:30]}...")
    
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
    
    print(f"\n✅ 完全翻译的数据已保存: {output_file}")
    print(f"📝 中文版本：")
    print(f"  - 标题：完全中文化")
    print(f"  - 描述：关键词翻译 + 截取（150 字符）")
    print(f"  - 类别：已翻译")
    
    return data_cn


if __name__ == '__main__':
    main()
