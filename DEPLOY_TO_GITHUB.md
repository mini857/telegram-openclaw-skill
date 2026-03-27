# 🚀 部署到 GitHub 指南

**项目**: OpenClaw 技能配置模板库  
**状态**: ✅ 本地 Git 已初始化  
**下一步**: 推送到 GitHub

---

## 📋 方法一：使用 GitHub CLI（推荐）

### 1. 安装 GitHub CLI

**macOS**:
```bash
brew install gh
```

**Linux**:
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh
```

### 2. 登录 GitHub

```bash
gh auth login
```

按提示操作：
1. 选择 GitHub.com
2. 选择 HTTPS
3. 登录浏览器
4. 授权 CLI

### 3. 创建仓库

```bash
cd ~/.openclaw/workspace/openclaw-skill-templates
gh repo create openclaw-skill-templates --public --source=. --remote=origin --push
```

**选项说明**:
- `--public`: 公开仓库（任何人可见）
- `--private`: 私有仓库（仅你可访问）
- `--source=.`: 使用当前目录
- `--push`: 自动推送代码

---

## 📋 方法二：手动创建（无需 CLI）

### 1. 在 GitHub 创建仓库

1. 访问 https://github.com/new
2. 仓库名：`openclaw-skill-templates`
3. 描述：`OpenClaw 技能配置模板库 - 50+ 热门技能配置模板，支持 Telegram Bot 智能查询`
4. 选择 **Public**（公开）
5. **不要** 勾选 "Initialize this repository with a README"
6. 点击 "Create repository"

### 2. 关联远程仓库

```bash
cd ~/.openclaw/workspace/openclaw-skill-templates
git remote add origin https://github.com/YOUR_USERNAME/openclaw-skill-templates.git
```

**替换**: `YOUR_USERNAME` 为你的 GitHub 用户名

### 3. 推送代码

```bash
git branch -M main
git push -u origin main
```

---

## 📋 方法三：使用 Git 凭证管理器

### 1. 配置 Git 凭证

```bash
git config --global credential.helper store
```

### 2. 推送代码

```bash
cd ~/.openclaw/workspace/openclaw-skill-templates
git remote add origin https://github.com/YOUR_USERNAME/openclaw-skill-templates.git
git push -u origin main
```

首次推送会提示输入 GitHub 用户名和密码（或 Personal Access Token）。

---

## 🔑 使用 Personal Access Token

GitHub 已不再支持使用密码推送代码，需要使用 Personal Access Token：

### 1. 创建 Token

1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 描述：`OpenClaw Skill Templates`
4. 选择权限：
   - ✅ `repo` (Full control of private repositories)
5. 点击 "Generate token"
6. **复制并保存 Token**（只显示一次！）

### 2. 使用 Token 推送

```bash
git push -u origin main
```

- 用户名：你的 GitHub 用户名
- 密码：粘贴刚才复制的 Token

---

## ✅ 推送后检查

### 1. 访问仓库

```
https://github.com/YOUR_USERNAME/openclaw-skill-templates
```

### 2. 检查文件

确保以下文件已上传：
- ✅ README.md
- ✅ templates/ (50 个 JSON 文件)
- ✅ database/skills-db.json
- ✅ bot/telegram-query-bot.py
- ✅ bot/start-bot.sh
- ✅ bot/README.md

### 3. 更新 README

在 GitHub 仓库页面，可以编辑 README.md 添加：

```markdown
## 🌟 在线演示

- 技能市场：https://clawhub.ai/
- Telegram 群组：https://t.me/openclaw_chat
- 频道：https://t.me/openclaw_skills
```

---

## 🔄 后续更新

### 添加新技能模板

```bash
# 1. 创建模板
cd ~/.openclaw/workspace/openclaw-skill-templates/templates
vim new-skill.json

# 2. 重新生成数据库
cd ~/.openclaw/workspace/openclaw-skill-hub/scripts
bash generate-db.sh

# 3. 提交并推送
cd ~/.openclaw/workspace/openclaw-skill-templates
git add .
git commit -m "feat: 添加 [技能名] 模板"
git push
```

### 批量更新

```bash
git add .
git commit -m "update: 更新技能数据库"
git push
```

---

## 📊 仓库统计

推送后 GitHub 会自动显示：
- 📁 文件数量
- 💾 代码行数
- 📊 贡献图表
- 🏷️ 主题标签

---

## 🎯 推荐配置

### 1. 添加主题标签

在仓库页面 → Settings → Topics，添加：
```
openclaw
skill-templates
ai-agents
telegram-bot
clawhub
productivity
automation
```

### 2. 添加 License

推荐 MIT License：
```bash
cd ~/.openclaw/workspace/openclaw-skill-templates
curl -O https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/mit-0.txt
mv mit-0.txt LICENSE
git add LICENSE
git commit -m "docs: 添加 MIT-0 许可证"
git push
```

### 3. 添加贡献指南

创建 `CONTRIBUTING.md`：
```markdown
# 贡献指南

欢迎贡献技能模板！

## 如何贡献

1. Fork 本仓库
2. 创建技能模板 `templates/[技能名].json`
3. 提交 Pull Request

## 模板格式

参考现有模板格式，包含：
- slug, name, displayName
- rating, installCommand, clawhubLink
- features, examples
- tags
```

---

## 🎉 完成！

推送成功后，你的技能模板库将：

✅ 全球可访问  
✅ 可被其他人 Fork 和贡献  
✅ 支持 Issue 追踪  
✅ 支持 Pull Request  
✅ 自动代码统计  
✅ 支持 GitHub Pages（可选）  

---

## 📝 快速命令参考

```bash
# 查看远程仓库
git remote -v

# 推送更新
git push

# 拉取更新
git pull

# 查看状态
git status

# 查看日志
git log --oneline
```

---

**开始部署吧！** 🚀

选择适合你的方法，10 分钟内完成部署！
