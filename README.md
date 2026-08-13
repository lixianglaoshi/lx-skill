# lx-skill

<!-- i18n-source-sha256: 5e23856151062a9bebdc3905a1667b9b52bae3825a5a9d9bcf9bdb5128dd524d -->

简体中文 | [English](README.en.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`lx-skill` 是一个持续生长的 AI 教育、新时代教育、数字教育与个人成长 Agent Skills 技能包，由李翔老师的乡村教育一线实践、AI赋能教学经验和组织沟通思考提炼而成。它可用于腾讯 WorkBuddy、Kimi Code、ZCode，也兼容 Codex、Claude Code 及其他支持开放 Agent Skills 规范的智能体。

当前包含五个可独立安装的技能：

| Skill | 适用场景 |
| --- | --- |
| `lx-education-diagnosis` | 全局教育诊断；独立的“教育选择与事件复盘模式”，判断一次管教或教学行为是否合适并给出修复方案 |
| `lx-parent-learning-environment` | 家庭催促、比较、电子设备、任务模糊、难度失配、反馈和家庭规则 |
| `lx-ai-learning-coach` | 用户说想学什么后，澄清目标与基础，通过一次一个问题、分级提示、练习和复述循序学习 |
| `lx-institutional-social-coach` | 体制内和层级组织的向上汇报、同事边界、饭局应酬、办公室政治与社交焦虑 |
| `lx-open-class-ai-diagnosis` | 读取教案、PPT、反思和课堂证据，诊断公开课中AI的教学价值、展示证据、风险与可落实修改 |

所有技能会跟随用户语言回答，支持简体中文和 English。

## 设计理念

- 诊断系统和具体行为，不诊断人格。
- 教育保护并唤醒自主性、好奇心、判断力和行动能力。
- AI负责提问、提示、反馈和模拟，不默认替代学习者思考。
- 先还原事实，再给有依据的判断、话术和可逆小实验。
- 现实地理解关系和权力差，同时守住尊严、合规与安全边界。
- 不进行心理或医学诊断，不使用羞辱、恐吓或标签化语言。

## 典型使用场景

```text
使用 $lx-education-diagnosis 进入教育选择与事件复盘模式。
我今天忍不住骂了孩子。请先问清完整经过，再判断哪里不合适、怎样修复。
```

```text
使用 $lx-parent-learning-environment 分析我们家的催促和手机冲突。
请一次只问两三个问题，最后制定一个七天实验。
```

```text
使用 $lx-ai-learning-coach 教我概率。
先弄清我的目标和基础，一次只问一个问题，别马上告诉我最终答案。
```

```text
使用 $lx-institutional-social-coach 帮我准备一次向领导汇报。
请区分事实、我的担心和正式风险，并给我一段可以直接说的话。
```

```text
使用 $lx-open-class-ai-diagnosis 诊断我的公开课。
先阅读我的教案和PPT，告诉我AI是在促进学生学习还是只是在展示工具；再补问必要的评委、学生和设备条件。
```

也可以直接用 English 提问，例如：

```text
Use $lx-ai-learning-coach to teach me SQL through guided practice. Ask one core question at a time.
```

## 下载

```bash
git clone https://github.com/lixianglaoshi/lx-skill.git
cd lx-skill
```

公开仓库允许任何人查看和下载。其他用户不能直接修改本仓库；他们可以在自己的 fork 中修改或提交 Pull Request，但只有仓库所有者或被授予写入权限的协作者才能合并并改变本仓库。这样既方便公开下载，也保留后续持续更新能力。

## 安装到国内 Agent

### Kimi Code

Kimi Code 的个人 skills 目录是 `~/.kimi-code/skills/`，同时也会读取通用目录 `~/.agents/skills/`：

```bash
mkdir -p ~/.kimi-code/skills
cp -R skills/lx-* ~/.kimi-code/skills/
```

重新开启会话后，可以用 `/skill:lx-ai-learning-coach` 等命令显式调用，也可以让 Kimi Code 根据 `description` 自动选择。

### ZCode

```bash
mkdir -p ~/.zcode/skills
cp -R skills/lx-* ~/.zcode/skills/
```

安装后在 ZCode 的 `Settings → Skills` 中点击 `Refresh` 并确认技能已启用；在对话中使用 `$lx-ai-learning-coach` 等名称调用。

### 腾讯 WorkBuddy

WorkBuddy 官方采用技能面板上传本地技能包。下面的命令会把五个技能分别打包：

```bash
mkdir -p workbuddy-packages
for d in skills/lx-*; do
  name=$(basename "$d")
  (cd "$d" && zip -r "../../workbuddy-packages/${name}.zip" .)
done
```

然后进入 WorkBuddy 的“添加技能 → 上传技能”，选择 `workbuddy-packages/` 中需要的 ZIP 文件。导入第三方技能前应先检查其中的说明、脚本和权限请求。

## 安装到 Codex

Codex 的个人 skills 目录是 `~/.agents/skills/`：

```bash
mkdir -p ~/.agents/skills
cp -R skills/lx-* ~/.agents/skills/
```

若只在当前项目使用：

```bash
mkdir -p .agents/skills
cp -R skills/lx-* .agents/skills/
```

显式调用方式：

```text
$lx-education-diagnosis
$lx-parent-learning-environment
$lx-ai-learning-coach
$lx-institutional-social-coach
$lx-open-class-ai-diagnosis
```

也可以直接描述问题，由 Codex 根据各 skill 的 `description` 自动选择。若安装后没有出现，重启 Codex。

## 安装到 Claude Code

Claude Code 的个人 skills 目录是 `~/.claude/skills/`：

```bash
mkdir -p ~/.claude/skills
cp -R skills/lx-* ~/.claude/skills/
```

若只在当前项目使用：

```bash
mkdir -p .claude/skills
cp -R skills/lx-* .claude/skills/
```

显式调用方式：

```text
/lx-education-diagnosis
/lx-parent-learning-environment
/lx-ai-learning-coach
/lx-institutional-social-coach
/lx-open-class-ai-diagnosis
```

## Windows PowerShell

Codex：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills"
Get-ChildItem ".\skills" -Directory -Filter "lx-*" | ForEach-Object {
  Copy-Item -Recurse -Force $_.FullName "$HOME\.agents\skills\"
}
```

Claude Code：

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\skills"
Get-ChildItem ".\skills" -Directory -Filter "lx-*" | ForEach-Object {
  Copy-Item -Recurse -Force $_.FullName "$HOME\.claude\skills\"
}
```

## 更新

```bash
cd lx-skill
git pull
```

更新后重新复制所需 skill 文件夹到个人或项目 skills 目录。

## 多语言维护

中文 `README.md` 是说明文档的内容源。其他语言 README 完成同步翻译后，运行：

```bash
python3 scripts/check_i18n_sync.py --update-markers
python3 scripts/check_i18n_sync.py
```

第一条命令把当前中文源文档的内容指纹写入六份 README；第二条命令检查指纹、语言导航、skill 名称和安装入口。该检查仅在本地手动运行；GitHub 上的自动检查已关闭，不会因翻译同步状态发送提醒。详细流程见 [docs/i18n-maintenance.md](docs/i18n-maintenance.md)。

## 仓库结构

```text
lx-skill/
├── README.md
├── README.en.md
├── README.es.md
├── README.de.md
├── README.ja.md
├── README.ko.md
├── ROADMAP.md
├── scripts/check_i18n_sync.py
├── tests/evaluation-cases.md
└── skills/
    ├── lx-education-diagnosis/
    ├── lx-parent-learning-environment/
    ├── lx-ai-learning-coach/
    ├── lx-institutional-social-coach/
    └── lx-open-class-ai-diagnosis/
```

每个 skill 文件夹都包含标准 `SKILL.md`、Codex 可选界面元数据 `agents/openai.yaml` 和按需加载的 `references/`。规范见 [Agent Skills specification](https://agentskills.io/specification)。平台安装方式参考 [OpenAI Codex Skills 文档](https://developers.openai.com/codex/skills) 与 [Claude Code Skills 文档](https://code.claude.com/docs/en/skills)。

每次修改后可用 [tests/evaluation-cases.md](tests/evaluation-cases.md) 进行人工回归测试。

## 使用边界

本项目提供教育思考、学习教练、沟通准备和行动实验，不替代心理、医疗、法律或紧急危机服务。涉及自伤、伤人、虐待、严重欺凌、违法指令、骚扰报复、失联或明显丧失日常功能时，应优先联系当地专业人员、正式支持渠道和紧急服务。

不要向AI提交真实姓名、学校、单位、住址、联系方式、未公开文件、涉密信息或其他非必要个人资料。

## 后续计划

`lx-skill` 将继续增加游戏化教学、公开课优化、班主任助手、教师AI学习设计等技能。详见 [ROADMAP.md](ROADMAP.md)。
