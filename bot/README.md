# 🤖 Telegram 技能查询 Bot

**功能**: 用户在群组发送技能名，Bot 自动返回配置模板  
**状态**: ✅ 已完成  
**最后更新**: 2026-03-27

---

## 🚀 快速启动

### 1. 安装依赖

```bash
pip3 install python-telegram-bot
```

### 2. 启动 Bot

```bash
cd ~/.openclaw/workspace/openclaw-skill-templates/bot
chmod +x start-bot.sh
./start-bot.sh
```

### 3. 添加到群组

```
1. 在 Telegram 搜索 @LuoboClaw_Bot
2. 添加到你的群组
3. 设置为管理员（可选）
4. 开始使用
```

---

## 💡 使用方式

### 群组成员发送

```
天气
```

### Bot 自动回复

```
📦 Weather 技能配置模板

⭐ 评分：5.0/5.0
📦 安装：3000+ 次
🔗 https://clawhub.ai/ 搜索 weather

📋 功能：
• 全球天气查询
• 7 天预报
• 无需 API

🔧 示例：
weather beijing
weather shanghai --days 7

💬 评价：
"用过最满意的天气技能"

👉 安装：clawhub install weather
```

---

## 📋 支持的查询

### 1. 技能名查询

```
用户：weather
Bot: 返回 weather 技能模板
```

### 2. 中文名查询

```
用户：天气
Bot: 返回 weather 技能模板
```

### 3. 关键词查询

```
用户：搜索
Bot: 返回搜索相关技能
```

### 4. 技能列表

```
用户：技能列表
Bot: 返回所有 50 个技能分类列表
```

### 5. 帮助

```
用户：帮助
Bot: 返回使用帮助
```

---

## 🔧 配置说明

### Bot Token

在 `telegram-query-bot.py` 中配置：

```python
BOT_TOKEN = "8721869397:AAGqjQBbXiEIm7iAGz_GQeWJAV4KT574x0k"
```

### 数据库路径

```python
DB_FILE = os.path.expanduser("~/.openclaw/workspace/openclaw-skill-templates/database/skills-db.json")
```

### 关键词映射

在 `KEYWORD_MAP` 中添加：

```python
KEYWORD_MAP = {
    "天气": "weather",
    "提醒": "reminder",
    # 添加更多...
}
```

---

## 📊 技能数据库

**位置**: `~/.openclaw/workspace/openclaw-skill-templates/database/skills-db.json`  
**技能数**: 50 个  
**格式**: JSON

### 更新数据库

```bash
cd ~/.openclaw/workspace/openclaw-skill-hub/scripts
bash generate-db.sh
```

---

## 🛠️ 故障排查

### Bot 无响应

1. 检查 Bot 是否在群组中
2. 检查 Bot 是否有读取消息权限
3. 检查日志输出

### 数据库加载失败

```bash
# 重新生成数据库
cd ~/.openclaw/workspace/openclaw-skill-hub/scripts
bash generate-db.sh
```

### 依赖问题

```bash
# 重新安装依赖
pip3 install python-telegram-bot --upgrade
```

---

## 📝 日志

Bot 启动后会输出：

```
🤖 OpenClaw 技能查询 Bot 启动中...
✅ Bot 启动成功！
   监听群组消息...
   按 Ctrl+C 停止
```

---

## 🎯 下一步优化

- [ ] 添加更多关键词映射
- [ ] 支持模糊匹配优化
- [ ] 添加技能收藏功能
- [ ] 添加技能评分功能
- [ ] 添加使用统计

---

**Bot 已就绪，开始使用吧！** 🚀
