# 🚀 快速部署到 GitHub

**用户名**: mini857  
**仓库名**: openclaw-skill-templates  
**状态**: ⏳ 等待创建仓库

---

## 📋 第一步：在 GitHub 创建仓库

### 1. 访问创建页面

打开浏览器访问：
```
https://github.com/new
```

### 2. 填写信息

| 字段 | 填写内容 |
|------|----------|
| **Repository name** | `openclaw-skill-templates` |
| **Description** | `OpenClaw 技能配置模板库 - 50+ 热门技能配置模板，支持 Telegram Bot 智能查询` |
| **Visibility** | ✅ Public（公开） |
| **Initialize** | ❌ 不要勾选任何初始化选项 |

### 3. 点击创建

点击 **"Create repository"** 按钮

---

## 📋 第二步：推送代码

仓库创建后，在终端执行：

```bash
cd ~/.openclaw/workspace/openclaw-skill-templates

# 确认远程仓库
git remote -v

# 推送代码
git push -u origin main
```

**首次推送会提示认证**：
- 输入 GitHub 用户名：`mini857`
- 输入 Personal Access Token（不是密码！）

---

## 🔑 获取 Personal Access Token

### 1. 访问 Token 页面

```
https://github.com/settings/tokens
```

### 2. 创建 Token

1. 点击 **"Generate new token (classic)"**
2. 填写描述：`OpenClaw Skill Templates`
3. 选择权限：
   - ✅ `repo` (Full control of private repositories)
4. 点击 **"Generate token"**
5. **复制 Token**（只显示一次！）

### 3. 使用 Token

推送代码时：
- 用户名：`mini857`
- 密码：粘贴刚才复制的 Token

---

## ✅ 验证部署

推送成功后，访问：
```
https://github.com/mini857/openclaw-skill-templates
```

检查文件：
- ✅ README.md
- ✅ templates/ (50 个文件)
- ✅ database/skills-db.json
- ✅ bot/ (3 个文件)

---

## 🎯 一键部署脚本（可选）

如果你已经有 Token，可以运行：

```bash
#!/bin/bash
# 保存为 deploy.sh

TOKEN="你的_Token"
USERNAME="mini857"
REPO="openclaw-skill-templates"

cd ~/.openclaw/workspace/openclaw-skill-templates

# 如果仓库不存在，创建它
curl -X POST \
  -H "Authorization: token $TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/user/repos \
  -d "{\"name\":\"$REPO\",\"description\":\"OpenClaw 技能配置模板库\",\"private\":false}"

# 推送代码
git remote set-url origin https://$USERNAME:$TOKEN@github.com/$USERNAME/$REPO.git
git push -u origin main

echo "✅ 部署完成！"
echo "🌐 仓库地址：https://github.com/$USERNAME/$REPO"
```

---

## 📝 快速检查清单

- [ ] 在 GitHub 创建仓库
- [ ] 获取 Personal Access Token
- [ ] 推送代码成功
- [ ] 验证文件已上传
- [ ] 添加 License（可选）
- [ ] 添加 Topics（可选）

---

**现在去创建仓库吧！** 🚀

创建完成后运行 `git push -u origin main` 即可！
