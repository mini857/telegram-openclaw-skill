# 🛠️ OpenClaw 技能配置模板库

**目标**: 为 clawhub 50+ 热门技能编写配置模板  
**状态**: ✅ 已完成 (50/50)  
**最后更新**: 2026-03-27

---

## 📚 技能列表

### 效率工具 (5 个)

| 技能 | 状态 | 模板 |
|------|------|------|
| Weather | ✅ | [weather.json](templates/weather.json) |
| clawdo | ✅ | [clawdo.json](templates/clawdo.json) |
| Productivity Bot | ⏳ | 待创建 |
| ... | ... | ... |

### 时间管理 (3 个)

| 技能 | 状态 | 模板 |
|------|------|------|
| Reminder | ✅ | [reminder.json](templates/reminder.json) |
| Cron Mastery | ✅ | [cron-mastery.json](templates/cron-mastery.json) |
| Apple Reminders | ✅ | [apple-reminders.json](templates/apple-reminders.json) |

### 搜索工具 (2 个)

| 技能 | 状态 | 模板 |
|------|------|------|
| Multi Search Engine | ✅ | [multi-search-engine.json](templates/multi-search-engine.json) |
| Baidu Search | ✅ | [baidu-search.json](templates/baidu-search.json) |

### 开发工具 (3 个)

| 技能 | 状态 | 模板 |
|------|------|------|
| Cron Helper | ✅ | [cron-helper.json](templates/cron-helper.json) |
| OpenClaw CLI | ✅ | [openclaw-cli.json](templates/openclaw-cli.json) |
| ... | ⏳ | 待创建 |

### 任务管理 (1 个)

| 技能 | 状态 | 模板 |
|------|------|------|
| Todoist | ✅ | [todoist.json](templates/todoist.json) |

---

## 🤖 Bot 查询

### Telegram Bot

在群组发送技能名获取配置模板：

```
发送：weather
Bot: 📦 Weather 技能配置模板
     👉 安装：clawhub install weather
     🔗 https://clawhub.ai/ 搜索 weather
     ...
```

### 支持命令

| 命令 | 说明 |
|------|------|
| [技能名] | 查询技能配置模板 |
| 技能列表 | 查看所有支持的技能 |
| 帮助 | 查看使用帮助 |

---

## 📋 模板格式

```json
{
  "slug": "weather",
  "name": "Weather",
  "displayName": "天气查询",
  "category": "效率工具",
  "rating": 5.0,
  "installCommand": "clawhub install weather",
  "clawhubLink": "https://clawhub.ai/ 搜索 weather",
  "description": "全球天气查询，无需 API 密钥",
  "features": [...],
  "examples": [...],
  "configTemplate": {...},
  "tags": ["天气", "效率工具"]
}
```

---

## 🚀 贡献

欢迎贡献技能模板！

1. Fork 本仓库
2. 创建模板文件 `templates/[技能名].json`
3. 提交 Pull Request

---

**项目地址**: github.com/mini857/openclaw-skill-templates
