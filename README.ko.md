# lx-skill

<!-- i18n-source-sha256: 1f45c38fb2ae85e00ba6a70c16878533bc13268948db40ff4e6a2ea3aca1615c -->

[简体中文](README.md) | [English](README.en.md) | [Español](README.es.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | 한국어

`lx-skill`은 AI 교육, 새로운 시대의 교육, 디지털 교육과 개인 성장을 위한 Agent Skills 모음입니다. 리샹의 농촌 교육 현장 경험, AI 기반 학습 지원, 위계적 조직에서의 의사소통 관점을 정리했습니다. Tencent WorkBuddy, Kimi Code, ZCode에서 사용할 수 있고, Codex, Claude Code 및 개방형 Agent Skills 규격을 지원하는 다른 에이전트와도 호환됩니다.

## 포함된 Skills

| Skill | 주요 사용 상황 |
| --- | --- |
| `lx-education-diagnosis` | 교육 시스템 전체 진단과 구체적인 양육·수업 선택 또는 사건의 회고 |
| `lx-parent-learning-environment` | 숙제 재촉, 비교, 디지털 기기 갈등, 모호한 과제, 난이도 불일치와 가정 규칙 |
| `lx-ai-learning-coach` | 목표 확인, 한 번에 하나의 질문, 단계별 힌트, 연습, 설명하기와 프로젝트 학습 |
| `lx-institutional-social-coach` | 상사 보고, 동료와의 경계, 비공식 모임, 사내 정치와 위계적 조직에서의 사회적 불안 |

각 skill은 사용자의 언어에 맞춰 답변합니다. 번역본 사이의 불일치를 막기 위해 실제 skill 로직은 하나의 버전으로 유지합니다.

## 기본 원칙

- 사람의 성격이 아니라 시스템과 관찰 가능한 행동을 진단합니다.
- 자율성, 호기심, 판단력과 지속 가능한 노력을 보호합니다.
- AI는 질문, 힌트, 시뮬레이션과 피드백에 활용하고 생각을 대신하는 도구로 기본 설정하지 않습니다.
- 판단이나 실험을 제안하기 전에 사실과 사건의 흐름을 확인합니다.
- 권력 차이를 현실적으로 이해하면서 존엄성, 안전과 규정 준수를 지킵니다.
- 심리·의학적 진단을 내리지 않으며 수치심, 공포 또는 낙인을 이용하지 않습니다.

## 사용 예시

```text
$lx-education-diagnosis를 교육 선택 및 사건 회고 모드로 사용해 주세요.
오늘 아이에게 소리를 질렀습니다. 먼저 전체 상황을 질문한 뒤 관계를 회복할 방법을 도와주세요.
```

```text
$lx-ai-learning-coach를 사용해 연습 중심으로 SQL을 가르쳐 주세요.
한 번에 핵심 질문 하나만 하고 최종 답을 바로 알려주지 마세요.
```

```text
$lx-institutional-social-coach를 사용해 상사에게 진행 상황을 보고할 준비를 해 주세요.
사실, 해석, 공식적 위험과 통제 가능한 행동을 구분하고 실제로 말할 문장을 작성해 주세요.
```

## 다운로드

```bash
git clone https://github.com/lixianglaoshi/lx-skill.git
cd lx-skill
```

누구나 공개 저장소를 보고 다운로드할 수 있습니다. 쓰기 권한이 없는 사용자는 원본 저장소를 직접 변경할 수 없습니다. fork나 Pull Request는 소유자가 병합하지 않는 한 원본에 영향을 주지 않습니다.

## 중국계 Agent에 설치

### Kimi Code

```bash
mkdir -p ~/.kimi-code/skills
cp -R skills/lx-* ~/.kimi-code/skills/
```

Kimi Code는 `~/.agents/skills/`도 검색합니다. 새 세션을 시작한 뒤 `/skill:lx-ai-learning-coach`와 같이 호출하거나 자동 선택을 사용할 수 있습니다.

### ZCode

```bash
mkdir -p ~/.zcode/skills
cp -R skills/lx-* ~/.zcode/skills/
```

`Settings → Skills`에서 `Refresh`를 누르고 스킬이 활성화되었는지 확인한 다음 `$lx-ai-learning-coach`와 같이 호출합니다.

### Tencent WorkBuddy

WorkBuddy는 Skills 패널에서 로컬 Skill 패키지를 가져옵니다. 네 개의 Skill을 각각 패키지로 만듭니다.

```bash
mkdir -p workbuddy-packages
for d in skills/lx-*; do
  name=$(basename "$d")
  (cd "$d" && zip -r "../../workbuddy-packages/${name}.zip" .)
done
```

WorkBuddy에서 `Add Skill → Upload Skill`을 선택하고 `workbuddy-packages/`의 필요한 ZIP 파일을 업로드합니다. 타사 Skill을 가져오기 전에 지침, 스크립트 및 권한 요청을 검토하세요.

## Codex에 설치

```bash
mkdir -p ~/.agents/skills
cp -R skills/lx-* ~/.agents/skills/
```

한 프로젝트에서만 사용할 경우 `.agents/skills/`에 복사합니다. 직접 호출하는 방법:

```text
$lx-education-diagnosis
$lx-parent-learning-environment
$lx-ai-learning-coach
$lx-institutional-social-coach
```

## Claude Code에 설치

```bash
mkdir -p ~/.claude/skills
cp -R skills/lx-* ~/.claude/skills/
```

한 프로젝트에서만 사용할 경우 `.claude/skills/`에 복사합니다. 직접 호출하는 방법:

```text
/lx-education-diagnosis
/lx-parent-learning-environment
/lx-ai-learning-coach
/lx-institutional-social-coach
```

## 번역 동기화

중국어 `README.md`를 문서의 기준으로 사용합니다. 변경 내용을 여섯 개 README에 모두 번역한 뒤 다음 명령을 실행합니다.

```bash
python3 scripts/check_i18n_sync.py --update-markers
python3 scripts/check_i18n_sync.py
```

관련 변경이 있을 때 GitHub Action도 같은 검사를 실행합니다. 자세한 절차는 [docs/i18n-maintenance.md](docs/i18n-maintenance.md)를 참고하세요.

## 구조와 안전

`skills/` 아래의 각 폴더는 독립적으로 설치할 수 있으며 표준 `SKILL.md`, 선택적인 Codex 메타데이터 `agents/openai.yaml`, 필요할 때 읽는 참고 자료를 포함합니다. [Agent Skills 규격](https://agentskills.io/specification)과 [로드맵](ROADMAP.md)을 참고하세요.

이 프로젝트는 교육적 성찰, 학습 지원, 의사소통 준비와 작은 행동 실험을 제공합니다. 심리, 의료, 법률 또는 응급 서비스를 대신하지 않습니다. 실제 이름, 학교·직장 정보, 주소, 연락처, 기밀 문서나 불필요한 개인정보를 AI에 보내지 마세요.
