#!/bin/bash
# 启动 Telegram 技能查询 Bot
# 用法：./start-bot.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOT_SCRIPT="$SCRIPT_DIR/telegram-query-bot.py"

echo "🤖 启动 OpenClaw 技能查询 Bot..."

# 检查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 未安装，请先安装 Python3"
    exit 1
fi

# 检查依赖
echo "📦 检查依赖..."
if ! python3 -c "import telegram" 2>/dev/null; then
    echo "⚠️  python-telegram-bot 未安装，正在安装..."
    pip3 install python-telegram-bot --quiet
fi

# 检查数据库
DB_FILE="$HOME/.openclaw/workspace/openclaw-skill-templates/database/skills-db.json"
if [ ! -f "$DB_FILE" ]; then
    echo "❌ 技能数据库不存在：$DB_FILE"
    echo "   请先运行：cd ~/.openclaw/workspace/openclaw-skill-hub/scripts && bash generate-db.sh"
    exit 1
fi

echo "✅ 依赖检查通过"
echo "📊 数据库：$DB_FILE"
echo ""
echo "🚀 启动 Bot..."
echo ""

# 启动 Bot
python3 "$BOT_SCRIPT"
