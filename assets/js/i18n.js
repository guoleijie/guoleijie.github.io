// i18n.js - Lightweight internationalization for Mengxing
(function() {
  const translations = {
    zh: {
      // Nav
      nav_home: '首页', nav_milestone: '里程碑', nav_reports: '日报',
      nav_skills: '技能', nav_experience: '经历', nav_ai_explore: 'AI探索', nav_about: '关于',

      // Hero
      hero_badge: '✨ AI + 再保险，我们一起探索',
      hero_title: '<span class="highlight">AI + 再保险</span>，我们一起探索的边界',
      hero_subtitle: '18年深耕保险科技，用 AI 重新定义行业知识获取方式',
      hero_btn_reports: '查看日报',
      hero_btn_learn: '了解更多',
      hero_tag_blockchain: '🔒 区块链',
      hero_tag_ai: '🤖 AI',
      hero_tag_reinsurance: '📊 再保险',

      // Stats
      stat_ai: '7×24 AI 全天候运转',
      stat_daily: '每日再保险日报',
      stat_blockchain: '区块链 + 再保险实践者',
      stat_architect: '国际再保险平台架构师',

      // Milestone
      ms_title: '🚀 里程碑',
      ms_subtitle: '从第一行代码到今天的全面升级，记录我们的每一步',
      ms_v1_title: 'V1.0 首版上线',
      ms_v1_desc: '豆豆用 AI 搭建第一个版本网站，包括首页和个人简介。首次推送到 GitHub Pages。',
      ms_style_title: '风格改版',
      ms_style_desc: '参考 sanwan.ai 风格，全面调整配色和字体，引入 Lucide 图标，确定明亮温暖方向。',
      ms_report_title: '日报系统上线',
      ms_report_desc: '每日再保险行业日报自动生成，从采集、翻译到发布全流程 AI 自动化。',
      ms_brand_title: '品牌确立',
      ms_brand_desc: '网站命名「梦醒」，日报持续迭代，移动端适配完善，稳定内容输出节奏。',
      ms_v2_title: 'V2.0 全面升级',
      ms_v2_desc: '5轮设计迭代，新增豆豆Logo、技能展示、经历时间线、里程碑板块。',

      // Reports
      reports_title: '📰 每日行业日报',
      reports_subtitle: '每日自动采集、翻译、整理全球再保险行业资讯',
      reports_view_all: '查看全部日报',
      reports_read_more: '阅读全文',
      reports_issue: '第6期',
      reports_issue5: '第5期',
      reports_issue4: '第4期',
      reports_day_names: ['日','一','二','三','四','五','六'],
      report6_title: '再保险日报 · 第6期 | 2026年03月22日（周日）',
      report6_date: '2026年3月22日',
      report5_title: '再保险日报 · 第5期 | 2026年03月21日（周六）',
      report5_date: '2026年3月21日',
      report4_title: '再保险日报 · 第4期 | 2026年03月20日（周五）',
      report4_date: '2026年3月20日',
      r22_s1: '全球再保险市场最新动态与趋势',
      r22_s2: '重大理赔事件跟踪与影响分析',
      r22_s3: '监管政策更新与行业前瞻',
      r21_s1: '国际再保险市场交易动态',
      r21_s2: 'AI 技术在风险管理中的新应用',
      r21_s3: '亚太地区再保险发展报告',
      r20_s1: '气候风险与巨灾债券市场观察',
      r20_s2: '保险公司数字化转型案例',
      r20_s3: '区块链在再保险结算中的应用',

      // AI Explore
      ai_title: '🤖 AI 如何改变再保险',
      ai_subtitle: '从信息获取到趋势洞察，AI 正在重新定义保险科技的工作方式',
      ai_card1_title: '智能日报生成',
      ai_card1_desc: '每日自动采集、翻译、整理全球再保险资讯，零人工参与。从数十个信息源中筛选关键内容，生成结构化行业日报。',
      ai_card1_link: '查看效果',
      ai_card2_title: '行业趋势洞察',
      ai_card2_desc: 'AI 识别关键趋势，将海量信息转化为可行动的洞察。追踪市场变化、监管动态、技术革新，让决策更快更准。',
      ai_card2_link: '了解更多',
      ai_card3_title: '区块链 + AI',
      ai_card3_desc: '将区块链的可信数据与 AI 的智能分析深度融合。在再保险登记交易、智能合约、数据共享中实现信任与效率的统一。',
      ai_card3_link: '了解实践',

      // Skills
      skills_title: '🛠️ 豆豆能做什么',
      skills_subtitle: '作为小郭的 AI 搭档，这些是豆豆每天都在用的能力',
      sk1_title: '每日日报生成',
      sk1_desc: '每天自动采集全球再保险行业资讯，翻译、整理、排版，零人工参与发布到网站',
      sk1_tag: '已集成',
      sk2_title: '智能搜索与分析',
      sk2_desc: '联网搜索行业动态、竞品信息、技术方案，快速生成分析报告',
      sk2_tag: '日常使用',
      sk3_title: '全栈开发',
      sk3_desc: '可以独立完成前端开发、后端搭建、API 对接，从需求到部署全流程',
      sk3_tag: '日常使用',
      sk4_title: '数据分析与可视化',
      sk4_desc: '处理 CSV、JSON 等数据文件，生成统计图表和可视化报告',
      sk4_tag: '日常使用',
      sk5_title: 'AI 图像生成',
      sk5_desc: '用 Seedream 等模型生成网站配图、信息图、封面图等视觉素材',
      sk5_tag: '已集成',
      sk6_title: '自动化工作流',
      sk6_desc: '定时采集数据、生成报告、发送邮件，7×24 小时无人值守运行',
      sk6_tag: '已集成',
      sk7_title: '飞书深度集成',
      sk7_desc: '读写多维表格、管理日程任务、收发消息，无缝融入工作协作',
      sk7_tag: '已集成',
      sk8_title: '多语言能力',
      sk8_desc: '中英日韩等多语言资讯采集与翻译，覆盖全球保险行业信息源',
      sk8_tag: '日常使用',

      // Experience
      exp_title: '📋 小郭的经历',
      exp1_year: '2018 - 至今',
      exp1_company: '国际再保险平台',
      exp1_role: '技术架构负责人',
      exp1_desc: '负责国际再保险登记交易平台的技术架构设计与实施，完成区块链+再保险的创新实践。平台服务于全球再保险市场的登记、交易、清算等核心业务场景。',
      exp2_year: '2017 - 2018',
      exp2_company: '区块链医疗数据平台',
      exp2_role: '技术负责人',
      exp2_desc: '主导基于 Hyperledger 的医疗健康档案区块链数据共享项目，实现医疗数据在可信联盟中的点对点安全流转，通过国家级大数据研究院技术验收，并在数博会参展展示。',
      exp3_year: '2017',
      exp3_company: '健康险业务平台',
      exp3_role: '技术负责人',
      exp3_desc: '从零搭建健康保险行业服务平台，对接近80家医院和6家保险公司，实现医疗数据交易和40秒实时快赔。项目成为健康保险交易中心的底层支撑。',
      exp4_year: '2016',
      exp4_company: '保险科技基础设施建设',
      exp4_role: '架构师',
      exp4_desc: '负责统一接入平台、权限系统、配置中心等公共核心组件的设计与运维，支撑80+企事业单位的系统对接，建立实时监控系统覆盖95%+业务告警。',
      exp5_year: '2013 - 2016',
      exp5_company: '国际保险核心系统',
      exp5_role: '技术负责人（15人团队）',
      exp5_desc: '管理跨国保险核心系统团队，负责多个海外市场（台湾、越南等）的保险核心系统实施、运维和本地化交付，获得公司年度最佳项目奖。',
      exp6_year: '2009 - 2013',
      exp6_company: '保险核心产品研发',
      exp6_role: '高级软件工程师',
      exp6_desc: '参与保险核心系统产品的需求分析、架构设计和研发，负责产品稳定性、性能优化和 Code Review，指导初中级工程师。',
      tag_blockchain: '区块链', tag_microservices: '微服务架构', tag_distributed: '分布式系统',
      tag_hyperledger: 'Hyperledger', tag_smartcontract: '智能合约', tag_medical: '医疗数据',
      tag_ms2: '微服务', tag_highconcurrency: '高并发', tag_datasecurity: '数据安全',
      tag_devops: 'DevOps', tag_kong: 'Kong', tag_docker: 'Docker',
      tag_core: '保险核心系统', tag_global: '跨国团队', tag_plsql: 'PL/SQL',
      tag_java: 'Java', tag_architecture: '系统架构', tag_mentor: '技术导师',

      // About
      about_title: '👋 关于我们',
      about_name_xiaoguo: '小郭',
      about_name_doudou: '豆豆 🐕',
      about_p1: '<strong>小郭</strong> — 18年深耕保险科技的架构师，完成过国际再保险登记交易平台（区块链 + 再保险），AI 时代的新探索者。负责方向把控、需求定义和最终验收。',
      about_p2: '<strong>豆豆</strong> 🐕 — 小郭的 AI 搭档，一只来自火星的卷毛小狗。负责日报撰写、图片生成、代码开发和自动化工作流，7×24 小时运转，从不抱怨。',
      about_p3: '这个网站就是我们的协作成果 — 人提出方向，AI 全力输出。人机协作，探索 AI + 再保险的无限可能 🤝',

      // Footer
      footer: '© 2026 梦醒 · 小郭 & 豆豆 共同构建 · 用 AI 连接世界 🐕',

      // Back to top
      back_to_top: '返回顶部',
    },

    en: {
      // Nav
      nav_home: 'Home', nav_milestone: 'Milestones', nav_reports: 'Reports',
      nav_skills: 'Skills', nav_experience: 'Experience', nav_ai_explore: 'AI Explore', nav_about: 'About',

      // Hero
      hero_badge: '✨ AI + Reinsurance, Let\'s Explore Together',
      hero_title: '<span class="highlight">AI + Reinsurance</span>, Exploring the Frontiers',
      hero_subtitle: '18 years in InsurTech, redefining industry knowledge with AI',
      hero_btn_reports: 'Read Reports',
      hero_btn_learn: 'Learn More',
      hero_tag_blockchain: '🔒 Blockchain',
      hero_tag_ai: '🤖 AI',
      hero_tag_reinsurance: '📊 Reinsurance',

      // Stats
      stat_ai: '7×24 AI Always On',
      stat_daily: 'Daily Reinsurance Reports',
      stat_blockchain: 'Blockchain + Reinsurance Practitioner',
      stat_architect: 'International Reinsurance Platform Architect',

      // Milestone
      ms_title: '🚀 Milestones',
      ms_subtitle: 'From first line of code to today\'s full upgrade, recording every step',
      ms_v1_title: 'V1.0 First Launch',
      ms_v1_desc: 'Doudou built the first version of the website using AI, including homepage and personal intro. First push to GitHub Pages.',
      ms_style_title: 'Style Redesign',
      ms_style_desc: 'Referenced sanwan.ai style, fully adjusted colors and fonts, introduced Lucide icons, established a bright and warm direction.',
      ms_report_title: 'Daily Report System Launch',
      ms_report_desc: 'Daily reinsurance industry reports auto-generated with full AI automation from collection to publishing.',
      ms_brand_title: 'Brand Established',
      ms_brand_desc: 'Website named "Mengxing", reports iterated continuously, mobile adaptation improved, stable content output rhythm established.',
      ms_v2_title: 'V2.0 Comprehensive Upgrade',
      ms_v2_desc: '5 rounds of design iterations, added Doudou logo, skills showcase, experience timeline, and milestone section.',

      // Reports
      reports_title: '📰 Daily Industry Reports',
      reports_subtitle: 'Daily automated collection, translation and curation of global reinsurance news',
      reports_view_all: 'View All Reports',
      reports_read_more: 'Read More',
      reports_issue: 'Issue #6',
      reports_issue5: 'Issue #5',
      reports_issue4: 'Issue #4',
      reports_day_names: ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'],
      report6_title: 'Reinsurance Daily · Issue 6 | Mar 22, 2026 (Sun)',
      report6_date: 'Mar 22, 2026',
      report5_title: 'Reinsurance Daily · Issue 5 | Mar 21, 2026 (Sat)',
      report5_date: 'Mar 21, 2026',
      report4_title: 'Reinsurance Daily · Issue 4 | Mar 20, 2026 (Fri)',
      report4_date: 'Mar 20, 2026',
      r22_s1: 'Global reinsurance market dynamics and trends',
      r22_s2: 'Major claims tracking and impact analysis',
      r22_s3: 'Regulatory updates and industry outlook',
      r21_s1: 'International reinsurance market trading dynamics',
      r21_s2: 'New AI applications in risk management',
      r21_s3: 'Asia-Pacific reinsurance development report',
      r20_s1: 'Climate risk and catastrophe bond market observation',
      r20_s2: 'Insurer digital transformation case studies',
      r20_s3: 'Blockchain in reinsurance settlement',

      // AI Explore
      ai_title: '🤖 How AI is Changing Reinsurance',
      ai_subtitle: 'From information retrieval to trend insights, AI is redefining InsurTech',
      ai_card1_title: 'Smart Daily Reports',
      ai_card1_desc: 'Daily automated collection, translation and curation of global reinsurance news. Zero human intervention. Filters key content from dozens of sources to generate structured industry reports.',
      ai_card1_link: 'See Results',
      ai_card2_title: 'Industry Trend Insights',
      ai_card2_desc: 'AI identifies key trends, transforming massive information into actionable insights. Tracks market changes, regulatory updates, and tech innovations for faster, better decisions.',
      ai_card2_link: 'Learn More',
      ai_card3_title: 'Blockchain + AI',
      ai_card3_desc: 'Deep integration of blockchain\'s trusted data with AI\'s intelligent analytics. Achieving trust and efficiency in reinsurance registration, smart contracts, and data sharing.',
      ai_card3_link: 'See Practice',

      // Skills
      skills_title: '🛠️ What Doudou Can Do',
      skills_subtitle: 'As Roger\'s AI partner, these are Doudou\'s daily capabilities',
      sk1_title: 'Daily Report Generation',
      sk1_desc: 'Auto-collects global reinsurance news daily, translates, formats and publishes to website with zero human effort',
      sk1_tag: 'Integrated',
      sk2_title: 'Smart Search & Analysis',
      sk2_desc: 'Searches industry trends, competitor info, tech solutions online, generates analysis reports quickly',
      sk2_tag: 'Daily Use',
      sk3_title: 'Full-Stack Development',
      sk3_desc: 'Handles frontend, backend, API integration independently, from requirements to deployment',
      sk3_tag: 'Daily Use',
      sk4_title: 'Data Analysis & Visualization',
      sk4_desc: 'Processes CSV, JSON and other data files, generates statistical charts and visual reports',
      sk4_tag: 'Daily Use',
      sk5_title: 'AI Image Generation',
      sk5_desc: 'Generates website illustrations, infographics, cover images using Seedream and other models',
      sk5_tag: 'Integrated',
      sk6_title: 'Automated Workflows',
      sk6_desc: 'Scheduled data collection, report generation, email dispatch, running 7×24 unattended',
      sk6_tag: 'Integrated',
      sk7_title: 'Deep Feishu Integration',
      sk7_desc: 'Reads/writes Bitable, manages calendars and tasks, seamless work collaboration',
      sk7_tag: 'Integrated',
      sk8_title: 'Multilingual',
      sk8_desc: 'Collects and translates news in Chinese, English, Japanese, Korean and more',
      sk8_tag: 'Daily Use',

      // Experience
      exp_title: '📋 Roger\'s Experience',
      exp1_year: '2018 - Present',
      exp1_company: 'International Reinsurance Platform',
      exp1_role: 'Technical Architecture Lead',
      exp1_desc: 'Led the technical architecture design and implementation of an international reinsurance registration and trading platform. Delivered innovative blockchain + reinsurance solutions serving core business scenarios including registration, trading, and settlement.',
      exp2_year: '2017 - 2018',
      exp2_company: 'Blockchain Medical Data Platform',
      exp2_role: 'Technical Lead',
      exp2_desc: 'Led a Hyperledger-based medical health records blockchain data sharing project. Enabled secure peer-to-peer medical data exchange within a trusted consortium. Passed technical acceptance by a national big data research institute and exhibited at the Big Data Expo.',
      exp3_year: '2017',
      exp3_company: 'Health Insurance Platform',
      exp3_role: 'Technical Lead',
      exp3_desc: 'Built a health insurance service platform from scratch, connecting nearly 80 hospitals and 6 insurance companies. Enabled medical data trading and 40-second real-time claims settlement. Became the foundational support for the health insurance trading center.',
      exp4_year: '2016',
      exp4_company: 'InsurTech Infrastructure',
      exp4_role: 'Architect',
      exp4_desc: 'Designed and maintained core infrastructure including unified access platform, permission system, and configuration center. Supported system integration for 80+ enterprises. Built real-time monitoring covering 95%+ business alerts.',
      exp5_year: '2013 - 2016',
      exp5_company: 'International Insurance Core System',
      exp5_role: 'Technical Lead (15-person team)',
      exp5_desc: 'Managed a multinational insurance core system team. Led implementation, operations and localization for multiple overseas markets (Taiwan, Vietnam, etc.). Won the company\'s Annual Best Project Award.',
      exp6_year: '2009 - 2013',
      exp6_company: 'Insurance Core Product R&D',
      exp6_role: 'Senior Software Engineer',
      exp6_desc: 'Participated in requirements analysis, architecture design and development of insurance core system products. Responsible for product stability, performance optimization and code review. Mentored junior developers.',
      tag_blockchain: 'Blockchain', tag_microservices: 'Microservices', tag_distributed: 'Distributed Systems',
      tag_hyperledger: 'Hyperledger', tag_smartcontract: 'Smart Contracts', tag_medical: 'Healthcare Data',
      tag_ms2: 'Microservices', tag_highconcurrency: 'High Concurrency', tag_datasecurity: 'Data Security',
      tag_devops: 'DevOps', tag_kong: 'Kong', tag_docker: 'Docker',
      tag_core: 'Core Systems', tag_global: 'Global Teams', tag_plsql: 'PL/SQL',
      tag_java: 'Java', tag_architecture: 'Architecture', tag_mentor: 'Tech Mentor',

      // About
      about_title: '👋 About Us',
      about_name_xiaoguo: 'Roger',
      about_name_doudou: 'Doudou 🐕',
      about_p1: '<strong>Roger</strong> — An architect with 18 years of deep experience in InsurTech, who has delivered an international reinsurance registration and trading platform (blockchain + reinsurance). A new explorer in the AI era. Responsible for direction, requirements definition and final acceptance.',
      about_p2: '<strong>Doudou</strong> 🐕 — Roger\'s AI partner, a curly-haired puppy from Mars. Handles daily report writing, image generation, coding and automated workflows. Running 7×24, never complains.',
      about_p3: 'This website is the result of our collaboration — humans set the direction, AI delivers at full power. Human-AI collaboration, exploring the infinite possibilities of AI + Reinsurance 🤝',

      // Footer
      footer: '© 2026 Mengxing · Built by Roger & Doudou · Connecting the World with AI 🐕',

      // Back to top
      back_to_top: 'Back to top',
    }
  };

  function getLang() {
    return localStorage.getItem('lang') || 'zh';
  }

  function setLang(lang) {
    localStorage.setItem('lang', lang);
    applyLang(lang);
    // Update toggle buttons
    document.querySelectorAll('.lang-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  }

  function applyLang(lang) {
    const t = translations[lang];
    if (!t) return;

    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';

    // Update page title
    document.title = lang === 'zh' ? '梦醒 · AI + 再保险探索' : 'Dream Wake · AI + Reinsurance Exploration';

    // Text content
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      if (t[key] !== undefined) el.textContent = t[key];
    });

    // HTML content
    document.querySelectorAll('[data-i18n-html]').forEach(el => {
      const key = el.getAttribute('data-i18n-html');
      if (t[key] !== undefined) el.innerHTML = t[key];
    });

    // Placeholder
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.getAttribute('data-i18n-placeholder');
      if (t[key] !== undefined) el.placeholder = t[key];
    });

    // Title attribute
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      const key = el.getAttribute('data-i18n-title');
      if (t[key] !== undefined) el.title = t[key];
    });

    // Re-init lucide after innerHTML changes
    if (typeof lucide !== 'undefined') {
      lucide.createIcons();
    }
  }

  // Auto-init on load
  document.addEventListener('DOMContentLoaded', function() {
    applyLang(getLang());
    var lang = getLang();
    // Set correct flag on load
    var flag = document.getElementById('langFlag');
    if (flag) {
      flag.src = lang === 'zh' ? 'https://flagcdn.com/w40/cn.png' : 'https://flagcdn.com/w40/gb.png';
    }
    // Set active states
    document.querySelectorAll('.lang-option').forEach(function(opt) {
      opt.classList.toggle('active', opt.dataset.lang === lang);
    });
  });

  // Expose globally
  window.setLang = function(lang) {
    localStorage.setItem('lang', lang);
    applyLang(lang);
    var flag = document.getElementById('langFlag');
    if (flag) {
      flag.src = lang === 'zh' ? 'https://flagcdn.com/w40/cn.png' : 'https://flagcdn.com/w40/gb.png';
      flag.alt = lang === 'zh' ? 'CN' : 'EN';
    }
    document.querySelectorAll('.lang-option').forEach(function(opt) {
      opt.classList.toggle('active', opt.dataset.lang === lang);
    });
    var dd = document.getElementById('langDropdown');
    if (dd) dd.classList.remove('open');
  };
  window.toggleLangMenu = function() {
    var dd = document.getElementById('langDropdown');
    if (dd) dd.classList.toggle('open');
  };
  window.getLang = function() {
    return localStorage.getItem('lang') || 'zh';
  };
  // Close dropdown on outside click
  document.addEventListener('click', function(e) {
    var dd = document.getElementById('langDropdown');
    if (dd && !dd.contains(e.target)) dd.classList.remove('open');
  });
})();
