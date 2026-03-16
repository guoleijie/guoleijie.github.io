# 梦醒的个人主页

> 简洁、现代、专业的个人主页，部署在 GitHub Pages

## 🎨 特点

- ✨ 现代简洁设计
- 📱 响应式布局
- 📊 日报系统 - 自动生成每日工作日志
- 🎯 项目展示
- 🔒 安全优先（不暴露敏感信息）
- ⚡ 纯静态（无需后端）
- 🎭 中文优化（霞鹜文楷字体）

## 📂 文件结构

```
guoleijie.github.io/
├── index.html           # 个人主页
├── blog/                # 博客/日报
│   ├── index.html       # 博客列表
│   └── 2026/03/       # 按年月组织
│       └── 16-daily-report.html
├── assets/              # 静态资源
│   ├── css/            # 样式文件
│   ├── js/             # JavaScript 文件
│   └── images/         # 图片资源
├── generate-daily-report.sh  # 日报生成脚本
└── README.md            # 本文档
```

## 📊 日报系统

### 快速开始

```bash
# 进入项目目录
cd ~/guoleijie.github.io

# 生成今日日报
./generate-daily-report.sh

# 生成指定日期的日报
./generate-daily-report.sh 2026-03-17
```

### 日报格式

生成的日报包含以下部分：

1. **今日完成** - 重点工作、常规工作、突发任务
2. **进行中** - 重点项目、常规任务
3. **遇到的问题** - 技术问题、资源问题
4. **学习与思考** - 新技能学习、经验总结、创意想法
5. **明日计划** - 必须完成、计划完成、机动时间
6. **工作统计** - 完成任务数、进行中数、学习内容数、工作时长

### 编辑日报

生成的日报文件位于：`blog/YYYY/MM/DD-daily-report.html`

编辑日报文件，添加实际内容：

```bash
# 编辑今日日报
vim blog/2026/03/16-daily-report.html
```

### 部署到 GitHub

```bash
# 提交更改
git add .
git commit -m "Add daily report 2026-03-16"

# 推送到 GitHub
git push origin main

# 访问网站
# https://guoleijie.github.io/blog/2026/03/16-daily-report.html
```

## 🚀 本地预览

### 方法 1：使用 Python

```bash
cd ~/guoleijie.github.io
python3 -m http.server 8000

# 浏览器访问
open http://localhost:8000
```

### 方法 2：使用 Node.js

```bash
cd ~/guoleijie.github.io
npx http-server -p 8000

# 浏览器访问
open http://localhost:8000
```

## 📦 部署到 GitHub Pages

### 首次部署

```bash
# 1. 初始化 Git（如果还没有）
cd ~/guoleijie.github.io
git init
git add .
git commit -m "Initial commit"

# 2. 推送到 GitHub
git remote add origin https://github.com/guoleijie/guoleijie.github.io.git
git branch -M main
git push -u origin main

# 3. 访问 https://guoleijie.github.io
```

### 后续更新

```bash
# 1. 生成日报
./generate-daily-report.sh

# 2. 编辑日报内容
vim blog/2026/03/16-daily-report.html

# 3. 提交并推送
git add .
git commit -m "Update daily report 2026-03-16"
git push origin main

# 4. 访问更新后的页面
# https://guoleijie.github.io/blog/2026/03/16-daily-report.html
```

## ✏️ 自定义内容

### 修改个人信息

编辑 `index.html` 中的以下部分：

- 姓名、职业标签
- 个人简介
- 技能卡片
- 项目展示
- 联系方式

### 修改日报样式

编辑 `assets/css/report.css` 中的 CSS 变量：

```css
:root {
  --bg-color: #f8fafc;         /* 背景色 */
  --text-primary: #1e293b;      /* 主文本色 */
  --text-secondary: #64748b;    /* 次要文本色 */
  --accent-color: #3b82f6;       /* 强调色 */
  --success-color: #10b981;      /* 成功色 */
  --warning-color: #f59e0b;      /* 警告色 */
  --danger-color: #ef4444;       /* 危险色 */
}
```

## 🎨 字体

- **中文**：LXGW WenKai（霞鹜文楷） - 清晰易读，开源商用
- **英文**：Noto Sans SC - Google 官方字体

## 🔒 安全提醒

**✅ 推荐做法：**
- 使用 GitHub Issues 作为联系方式
- 只展示公开信息
- 定期检查页面内容
- 不在日报中记录敏感信息

**❌ 避免暴露：**
- 真实邮箱（防爬虫）
- 电话号码
- 具体住址
- 身份证号
- API Keys、密码等敏感信息

## 📊 自动化脚本

### generate-daily-report.sh

**功能：**
- 自动生成日报 HTML 文件
- 自动创建目录结构
- 自动填充日期和星期

**用法：**
```bash
# 生成今日日报
./generate-daily-report.sh

# 生成指定日期的日报
./generate-daily-report.sh 2026-03-17
```

**输出：**
- 文件位置：`blog/YYYY/MM/DD-daily-report.html`
- 访问地址：`https://guoleijie.github.io/blog/YYYY/MM/DD-daily-report.html`

## 🛠️ 技术栈

- **HTML5** - 语义化标签
- **CSS3** - Flexbox, Grid, 动画
- **JavaScript** - ES6+, Intersection Observer
- **Design** - 简洁主题，响应式布局
- **Font** - 霞鹜文楷，Noto Sans SC
- **Icons** - Lucide Icons

## 📄 许可证

MIT License - 自由使用和修改

---

**Built with ❤️ by [梦醒](https://github.com/guoleijie)**

**维护：** 此网站由 AI 助手（豆豆）维护，有问题请提 [Issue](https://github.com/guoleijie/guoleijie.github.io/issues)
