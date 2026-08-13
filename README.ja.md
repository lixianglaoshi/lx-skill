# lx-skill

<!-- i18n-source-sha256: ad9f8ba3ed13dc867d7bb3f2f152cb3fc07f3af4173fbc3d11d7cfb1eb3114d4 -->

[简体中文](README.md) | [English](README.en.md) | [Español](README.es.md) | [Deutsch](README.de.md) | 日本語 | [한국어](README.ko.md)

`lx-skill` は、AI教育、新時代の教育、デジタル教育、個人の成長を支援する Agent Skills パッケージです。李翔による農村教育の実践、AIを活用した学習支援、階層型組織におけるコミュニケーションの知見を整理しています。Tencent WorkBuddy、Kimi Code、ZCode で利用できるほか、Codex、Claude Code、およびオープンな Agent Skills 仕様に対応するエージェントとも互換性があります。

## 収録している Skills

| Skill | 主な用途 |
| --- | --- |
| `lx-education-diagnosis` | 教育全体の診断と、具体的なしつけ・指導上の選択や出来事の振り返り |
| `lx-parent-learning-environment` | 宿題の催促、比較、端末利用の衝突、曖昧な課題、難易度の不一致、家庭内ルール |
| `lx-ai-learning-coach` | 目標の明確化、一度に一つの問い、段階的なヒント、練習、教え返し、プロジェクト学習 |
| `lx-institutional-social-coach` | 上司への報告、同僚との境界線、非公式な会合、職場政治、階層型組織での対人不安 |
| `lx-open-class-ai-diagnosis` | 公開授業におけるAIの教育的価値、根拠、リスク、具体的な改善を診断 |
| `lx-gamified-learning-design` | ゲームの仕組みを学習の仕組みに変換し、概念、アルゴリズム、空間関係、因果関係、方略を操作・可視化・転移できるようにする |

各 skill は利用者の言語に合わせて回答します。翻訳ごとの差異を防ぐため、skill のロジック自体は一つの版で管理します。

## 基本方針

- 人格ではなく、仕組みと観察可能な行動を診断する。
- 自律性、好奇心、判断力、持続可能な努力を守る。
- AIを質問、ヒント、模擬体験、フィードバックに用い、思考の代行を標準にしない。
- 判断や実験の提案をする前に、事実と経緯を確認する。
- 権力差を現実的に捉えつつ、尊厳、安全、コンプライアンスを守る。
- 心理・医療上の診断を行わず、羞恥、恐怖、レッテルを利用しない。

## 使用例

```text
$lx-education-diagnosis を教育上の選択・出来事振り返りモードで使ってください。
今日、子どもを怒鳴ってしまいました。まず経緯を詳しく確認し、その後で関係修復を手伝ってください。
```

```text
$lx-ai-learning-coach を使い、練習を通してSQLを教えてください。
一度に中心となる質問を一つだけ出し、最終解答をすぐに示さないでください。
```

```text
$lx-institutional-social-coach を使い、上司への進捗報告を準備してください。
事実、解釈、正式なリスク、自分でコントロールできる行動を分け、話し方の例を作ってください。
```

```text
$lx-open-class-ai-diagnosis を使い、私の公開授業を診断してください。まず指導案とスライドを読み、AIが生徒の学びを変えているのか、単なるツール展示なのかを確認してください。
```

## ダウンロード

```bash
git clone https://github.com/lixianglaoshi/lx-skill.git
cd lx-skill
```

公開リポジトリは誰でも閲覧・ダウンロードできます。書き込み権限がない人は元のリポジトリを直接変更できません。fork や Pull Request は、所有者が採用しない限り元の内容を変更しません。

## 中国系 Agent へのインストール

### Kimi Code

```bash
mkdir -p ~/.kimi-code/skills
cp -R skills/lx-* ~/.kimi-code/skills/
```

Kimi Code は `~/.agents/skills/` も読み込みます。新しいセッションを開始し、`/skill:lx-ai-learning-coach` のように明示的に呼び出すか、自動選択を利用します。

### ZCode

```bash
mkdir -p ~/.zcode/skills
cp -R skills/lx-* ~/.zcode/skills/
```

`Settings → Skills` で `Refresh` をクリックし、有効になっていることを確認してから `$lx-ai-learning-coach` などで呼び出します。

### Tencent WorkBuddy

WorkBuddy は Skills パネルからローカル Skill パッケージを読み込みます。6つの Skill を個別にパッケージ化します。

```bash
mkdir -p workbuddy-packages
for d in skills/lx-*; do
  name=$(basename "$d")
  (cd "$d" && zip -r "../../workbuddy-packages/${name}.zip" .)
done
```

WorkBuddy で `Add Skill → Upload Skill` を選び、`workbuddy-packages/` 内の必要な ZIP をアップロードします。第三者の Skill を読み込む前に、指示、スクリプト、権限要求を確認してください。

## Codex へのインストール

```bash
mkdir -p ~/.agents/skills
cp -R skills/lx-* ~/.agents/skills/
```

プロジェクト単位で使う場合は `.agents/skills/` にコピーします。明示的な呼び出し：

```text
$lx-education-diagnosis
$lx-parent-learning-environment
$lx-ai-learning-coach
$lx-institutional-social-coach
$lx-open-class-ai-diagnosis
$lx-gamified-learning-design
```

## Claude Code へのインストール

```bash
mkdir -p ~/.claude/skills
cp -R skills/lx-* ~/.claude/skills/
```

プロジェクト単位で使う場合は `.claude/skills/` にコピーします。明示的な呼び出し：

```text
/lx-education-diagnosis
/lx-parent-learning-environment
/lx-ai-learning-coach
/lx-institutional-social-coach
/lx-open-class-ai-diagnosis
/lx-gamified-learning-design
```

## 翻訳の同期

中国語版 `README.md` を文書の基準とします。変更を6言語すべてに反映した後、次を実行します。

```bash
python3 scripts/check_i18n_sync.py --update-markers
python3 scripts/check_i18n_sync.py
```

検査はローカルで手動実行するだけです。GitHub Action は無効化されているため、翻訳同期による GitHub 通知は発生しません。手順は [docs/i18n-maintenance.md](docs/i18n-maintenance.md) を参照してください。

## 構成と安全上の注意

`skills/` 以下の各フォルダーは個別にインストールでき、標準の `SKILL.md`、任意の Codex メタデータ `agents/openai.yaml`、必要時に読み込む参照資料を含みます。[Agent Skills 仕様](https://agentskills.io/specification) と [ロードマップ](ROADMAP.md) も参照してください。

このプロジェクトは、教育の振り返り、学習支援、コミュニケーション準備、小さな行動実験を提供します。心理、医療、法律、緊急支援の代わりにはなりません。実名、学校・勤務先の詳細、住所、連絡先、機密文書、その他不要な個人情報をAIに送信しないでください。
