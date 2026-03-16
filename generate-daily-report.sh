#!/bin/bash
# 生成日报脚本
# 用法: ./generate-daily-report.sh [YYYY-MM-DD]

set -e

# 参数处理
DATE=${1:-$(date +%Y-%m-%d)}
YEAR=$(echo $DATE | cut -d- -f1)
MONTH=$(echo $DATE | cut -d- -f2)
DAY=$(echo $DATE | cut -d- -f3)

# 计算星期
WEEKDAY=$(date -d "$DATE" +%A 2>/dev/null || date -j -f "%Y-%m-%d" "$DATE" +%A 2>/dev/null || echo "星期一")

# 日报目录
REPORT_DIR="blog/$YEAR/$MONTH"
REPORT_FILE="$REPORT_DIR/${DAY}-daily-report.html"

# 创建目录
mkdir -p "$REPORT_DIR"

# 日报内容
cat > "$REPORT_FILE" << 'EOF'
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>日报 - DATE_PLACEHOLDER | 梦醒</title>
    <link rel="stylesheet" href="/assets/css/report.css">
    <link href="https://cdn.jsdelivr.net/npm/lxgw-wenkai-webfont@1.7.0/style.css" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">
        <div class="container">
            <a href="/" class="logo">
                <i data-lucide="zap"></i>
                <span>梦醒</span>
            </a>
            <ul class="nav-links">
                <li><a href="/">首页</a></li>
                <li><a href="/blog/">博客</a></li>
                <li><a href="/blog/DATES/">DATES</a></li>
            </ul>
        </div>
    </nav>

    <!-- 日报内容 -->
    <article class="daily-report">
        <header class="report-header">
            <h1>📊 日报 - DATE_PLACEHOLDER</h1>
            <div class="report-meta">
                <span class="date">
                    <i data-lucide="calendar"></i>
                    YEAR_PLACEHOLDER年MONTH_PLACEHOLDER月DAY_PLACEHOLDER日
                </span>
                <span class="weekday">
                    <i data-lucide="clock"></i>
                    WEEKDAY_PLACEHOLDER
                </span>
                <span class="status">
                    <i data-lucide="check-circle"></i>
                    正常
                </span>
            </div>
        </header>

        <section class="report-section">
            <h2><i data-lucide="check-square"></i> 今日完成</h2>

            <div class="task-group">
                <h3>重点工作</h3>
                <div class="empty-state">
                    <i data-lucide="edit-3"></i>
                    <p>等待添加内容...</p>
                </div>
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="loader"></i> 进行中</h2>

            <div class="task-group">
                <h3>重点项目</h3>
                <div class="empty-state">
                    <i data-lucide="edit-3"></i>
                    <p>等待添加内容...</p>
                </div>
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="lightbulb"></i> 学习与思考</h2>

            <div class="idea-item">
                <h3>新技能学习</h3>
                <div class="empty-state">
                    <i data-lucide="edit-3"></i>
                    <p>等待添加内容...</p>
                </div>
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="target"></i> 明日计划</h2>

            <div class="task-list">
                <div class="task-item todo">
                    <span class="priority high">高</span>
                    <span class="task-name">待定</span>
                    <span class="task-time">--</span>
                </div>
            </div>
        </section>

        <section class="report-section">
            <h2><i data-lucide="bar-chart-2"></i> 工作统计</h2>

            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="check-circle"></i>
                    </div>
                    <div class="stat-value">0</div>
                    <div class="stat-label">完成任务</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="loader"></i>
                    </div>
                    <div class="stat-value">0</div>
                    <div class="stat-label">进行中</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="book-open"></i>
                    </div>
                    <div class="stat-value">0</div>
                    <div class="stat-label">学习内容</div>
                </div>
                <div class="stat-card">
                    <div class="stat-icon">
                        <i data-lucide="clock"></i>
                    </div>
                    <div class="stat-value">0</div>
                    <div class="stat-label">工作时长（小时）</div>
                </div>
            </div>
        </section>

        <footer class="report-footer">
            <p>💡 豆豆备注：等待添加...</p>
            <div class="navigation">
                <a href="/blog/YEAR_PLACEHOLDER/MONTH_PLACEHOLDER/" class="nav-link">
                    <i data-lucide="arrow-left"></i>
                    MONTH_PLACEHOLDER月日报
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
</html>
EOF

# 替换占位符
sed -i "s/DATE_PLACEHOLDER/$DATE/g" "$REPORT_FILE"
sed -i "s/YEAR_PLACEHOLDER/$YEAR/g" "$REPORT_FILE"
sed -i "s/MONTH_PLACEHOLDER/$MONTH/g" "$REPORT_FILE"
sed -i "s/DAY_PLACEHOLDER/$DAY/g" "$REPORT_FILE"
sed -i "s/WEEKDAY_PLACEHOLDER/$WEEKDAY/g" "$REPORT_FILE"
sed -i "s/DATES/YEAR_PLACEHOLDER-MONTH_PLACEHOLDER/g" "$REPORT_FILE"

echo "✅ 日报已生成: $REPORT_FILE"
echo "📝 请编辑文件添加内容"
echo "🌐 访问: https://guoleijie.github.io/blog/$YEAR/$MONTH/${DAY}-daily-report.html"
