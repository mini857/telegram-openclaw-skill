#!/usr/bin/env python3
"""
OpenClaw 技能模板查询 Bot
功能：用户在群组发送技能名，Bot 自动返回配置模板
"""

import json
import os
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

# 配置
BOT_TOKEN = "8721869397:AAGqjQBbXiEIm7iAGz_GQeWJAV4KT574x0k"
DB_FILE = os.path.expanduser("~/.openclaw/workspace/openclaw-skill-templates/database/skills-db.json")

# 关键词映射（中文名→技能 slug）
KEYWORD_MAP = {
    "天气": "weather",
    "weather": "weather",
    "提醒": "reminder",
    "reminder": "reminder",
    "搜索": "multi-search-engine",
    "search": "multi-search-engine",
    "任务": "clawdo",
    "clawdo": "clawdo",
    "cron": "cron-mastery",
    "定时": "cron-mastery",
    "飞书": "feishu-message",
    "feishu": "feishu-message",
    "slack": "slack-message",
    "github": "github",
    "notion": "notion",
    "obsidian": "obsidian",
    "todo": "todoist",
    "todoist": "todoist",
}

# 加载技能数据库
def load_skills():
    """加载技能数据库"""
    if not os.path.exists(DB_FILE):
        print(f"❌ 数据库文件不存在：{DB_FILE}")
        return []
    
    with open(DB_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# 格式化技能回复
def format_skill(skill):
    """格式化技能信息为回复消息"""
    reply = f"📦 {skill.get('displayName', skill.get('name', ''))} 技能配置模板\n\n"
    
    # 评分
    rating = skill.get('rating', 0)
    stars = skill.get('stars', 0)
    if stars > 0:
        reply += f"⭐ 评分：{rating}/5.0（{stars}星）\n"
    else:
        reply += f"⭐ 评分：{rating}/5.0\n"
    
    # 安装量
    installs = skill.get('installs', 'N/A')
    reply += f"📦 安装：{installs}\n"
    
    # 链接
    reply += f"🔗 {skill.get('clawhubLink', '')}\n\n"
    
    # 描述
    reply += f"📋 {skill.get('description', '')}\n\n"
    
    # 功能
    features = skill.get('features', [])
    if features:
        reply += "✨ 功能：\n"
        for feature in features[:6]:  # 最多显示 6 个
            reply += f"• {feature}\n"
        reply += "\n"
    
    # 使用示例
    examples = skill.get('examples', [])
    if examples:
        reply += "🔧 使用示例：\n"
        for example in examples[:3]:  # 最多显示 3 个
            cmd = example.get('command', '')
            desc = example.get('description', '')
            reply += f"• `{cmd}` - {desc}\n"
        reply += "\n"
    
    # 用户评价
    review = skill.get('userReview', '')
    if review:
        reply += f"💬 用户评价：\n\"{review}\"\n\n"
    
    # 安装命令
    reply += "━━━━━━━━━━━━━━━━━━\n\n"
    reply += f"👉 安装命令：\n`{skill.get('installCommand', '')}`\n\n"
    reply += f"🌐 技能市场：\nhttps://clawhub.ai/\n\n"
    
    # 标签
    tags = skill.get('tags', [])
    if tags:
        reply += "#" + " #".join(tags)
    
    return reply

# 技能列表消息
def get_skills_list():
    """获取技能列表"""
    skills = load_skills()
    
    # 按分类分组
    categories = {}
    for skill in skills:
        cat = skill.get('category', '其他')
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(skill)
    
    message = "📚 OpenClaw 技能配置模板库（50 个技能）\n\n"
    message += "发送技能名获取配置模板\n\n"
    message += "━━━━━━━━━━━━━━━━━━\n\n"
    
    for cat, cat_skills in sorted(categories.items()):
        message += f"📁 {cat} ({len(cat_skills)}个)\n"
        for skill in cat_skills[:5]:  # 每类最多显示 5 个
            name = skill.get('displayName', skill.get('name', ''))
            slug = skill.get('slug', '')
            rating = skill.get('rating', 0)
            message += f"• {name} ({slug}) ⭐{rating}\n"
        if len(cat_skills) > 5:
            message += f"  ... 还有{len(cat_skills) - 5}个\n"
        message += "\n"
    
    message += "━━━━━━━━━━━━━━━━━━\n\n"
    message += "💡 提示：\n"
    message += "• 发送技能名（如：weather）获取模板\n"
    message += "• 发送中文名（如：天气）也可以\n"
    message += "• 发送 技能列表 查看所有技能\n"
    
    return message

# 模糊匹配技能
def fuzzy_match(query, skills):
    """模糊匹配技能"""
    query_lower = query.lower()
    
    # 精确匹配 slug
    for skill in skills:
        if skill.get('slug', '').lower() == query_lower:
            return skill
    
    # 精确匹配名称
    for skill in skills:
        name = skill.get('name', '').lower()
        display_name = skill.get('displayName', '').lower()
        if name == query_lower or display_name == query_lower:
            return skill
    
    # 关键词匹配
    for keyword, slug in KEYWORD_MAP.items():
        if keyword in query_lower:
            for skill in skills:
                if skill.get('slug', '') == slug:
                    return skill
    
    # 标签匹配
    for skill in skills:
        tags = skill.get('tags', [])
        for tag in tags:
            if tag.lower() in query_lower or query_lower in tag.lower():
                return skill
    
    return None

# 处理消息
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """处理用户消息"""
    text = update.message.text.strip()
    
    # 忽略命令
    if text.startswith('/'):
        return
    
    # 加载技能
    skills = load_skills()
    if not skills:
        await update.message.reply_text("❌ 技能数据库加载失败")
        return
    
    # 特殊命令
    if text in ["技能列表", "列表", "list", "skills"]:
        await update.message.reply_text(get_skills_list(), parse_mode='HTML')
        return
    
    if text in ["帮助", "help", "帮助信息"]:
        help_text = """📖 使用帮助

发送技能名获取配置模板：
• weather 或 天气
• reminder 或 提醒
• clawdo 或 任务

查看所有技能：
• 技能列表

支持模糊匹配：
• 发送部分技能名也可以

技能市场：
https://clawhub.ai/
"""
        await update.message.reply_text(help_text)
        return
    
    # 模糊匹配技能
    matched_skill = fuzzy_match(text, skills)
    
    if matched_skill:
        reply = format_skill(matched_skill)
        await update.message.reply_text(reply, parse_mode='HTML')
    else:
        # 未匹配到，显示相似技能
        reply = f"❓ 未找到技能 \"{text}\"\n\n"
        reply += "💡 试试以下技能：\n\n"
        
        # 显示前 5 个热门技能
        top_skills = sorted(skills, key=lambda x: x.get('rating', 0), reverse=True)[:5]
        for skill in top_skills:
            name = skill.get('displayName', skill.get('name', ''))
            slug = skill.get('slug', '')
            rating = skill.get('rating', 0)
            reply += f"• {name} ({slug}) ⭐{rating}\n"
        
        reply += "\n💡 发送 技能列表 查看所有技能"
        await update.message.reply_text(reply)

# 主函数
def main():
    """主函数"""
    print("🤖 OpenClaw 技能查询 Bot 启动中...")
    
    # 创建应用
    application = Application.builder().token(BOT_TOKEN).build()
    
    # 添加消息处理器
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # 启动 Bot
    print("✅ Bot 启动成功！")
    print("   监听群组消息...")
    print("   按 Ctrl+C 停止")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
