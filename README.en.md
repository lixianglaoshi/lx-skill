# lx-skill

<!-- i18n-source-sha256: 23898433bfaca1bb2cb669bef806c6153d7e73416ac9e62891f2f84958efdbfb -->

[简体中文](README.md) | English | [Español](README.es.md) | [Deutsch](README.de.md) | [日本語](README.ja.md) | [한국어](README.ko.md)

`lx-skill` is a growing Agent Skills collection for AI education, education in the new era, digital education, and personal growth. It distills Li Xiang's experience in rural education, AI-supported teaching, and communication inside hierarchical organizations. It works with Tencent WorkBuddy, Kimi Code, and ZCode, while remaining compatible with Codex, Claude Code, and other agents that support the open Agent Skills specification.

## Included skills

| Skill | Use it for |
| --- | --- |
| `lx-education-diagnosis` | Whole-system education diagnosis and a dedicated decision/event review mode for parenting or teaching choices |
| `lx-parent-learning-environment` | Homework prompting, comparisons, screen conflict, unclear tasks, difficulty mismatch, feedback, and household rules |
| `lx-ai-learning-coach` | Goal clarification, one-question-at-a-time tutoring, graduated hints, practice, teach-back, and project learning |
| `lx-open-class-ai-diagnosis` | Diagnose the teaching value, evidence, risks, and actionable revisions of AI in an open class from plans, slides, reflections, and classroom evidence |
| `lx-gamified-learning-design` | Turn game mechanics into learning mechanics so abstract concepts, algorithms, spatial relations, causality, and strategies become operable, visible, and transferable |
| `lx-interactive-teaching-generator` | Directly deliver a polished, openable, single-file interactive HTML page for any teaching topic, using genuine Three.js 3D, SVG/D3, KaTeX, sliders, and a collapsible check when appropriate |
| `lx-highschool-geometry-chemistry` | Use SymPy-backed exact computation to deliver a single-file interactive page for high-school solid geometry, analytic geometry/conic sections, and chemistry reactions |
| `lx-3d-teaching-animation` | Create a pausable, explorable 3D teaching page for spatial structure, mechanical transmission, forces, motion, and other processes students need to inspect |

All skills follow the user's language and support both English and Simplified Chinese.

## Core principles

- Diagnose systems and observable actions, not personalities.
- Protect autonomy, curiosity, judgment, and sustainable effort.
- Use AI for questions, hints, feedback, and simulation instead of default answer substitution.
- Reconstruct the facts before offering a judgment, script, or reversible experiment.
- Recognize incentives and power differences while preserving dignity, safety, and compliance.
- Do not provide psychological or medical diagnoses or use shame, fear, or labels.

## Download

```bash
git clone https://github.com/lixianglaoshi/lx-skill.git
cd lx-skill
```

Anyone can view and download this public repository. Other users cannot directly change it unless the owner grants them write access. They may modify their own forks or propose a Pull Request, but only the owner or authorized collaborators can merge changes into this repository.

## Install for China-based agents

### Kimi Code

```bash
mkdir -p ~/.kimi-code/skills
cp -R skills/lx-* ~/.kimi-code/skills/
```

Kimi Code also scans `~/.agents/skills/`. Start a new session and invoke a skill with a command such as `/skill:lx-ai-learning-coach`, or let the agent select it automatically.

### ZCode

```bash
mkdir -p ~/.zcode/skills
cp -R skills/lx-* ~/.zcode/skills/
```

Open `Settings → Skills`, select `Refresh`, verify that the skills are enabled, and invoke one with a name such as `$lx-ai-learning-coach`.

### Tencent WorkBuddy

WorkBuddy imports local skill packages through its Skills panel. Package the eight skills separately:

```bash
mkdir -p workbuddy-packages
for d in skills/lx-*; do
  name=$(basename "$d")
  (cd "$d" && zip -r "../../workbuddy-packages/${name}.zip" .)
done
```

In WorkBuddy, choose `Add Skill → Upload Skill` and select the required ZIP files from `workbuddy-packages/`. Review third-party skill instructions, scripts, and permission requests before importing them.

## Install for Codex

```bash
mkdir -p ~/.agents/skills
cp -R skills/lx-* ~/.agents/skills/
```

For a single project, copy them to `.agents/skills/`. Invoke them explicitly with:

```text
$lx-education-diagnosis
$lx-parent-learning-environment
$lx-ai-learning-coach
$lx-open-class-ai-diagnosis
$lx-gamified-learning-design
$lx-interactive-teaching-generator
$lx-highschool-geometry-chemistry
$lx-3d-teaching-animation
```

## Install for Claude Code

```bash
mkdir -p ~/.claude/skills
cp -R skills/lx-* ~/.claude/skills/
```

For a single project, copy them to `.claude/skills/`. Invoke them explicitly with:

```text
/lx-education-diagnosis
/lx-parent-learning-environment
/lx-ai-learning-coach
/lx-open-class-ai-diagnosis
/lx-gamified-learning-design
/lx-interactive-teaching-generator
/lx-highschool-geometry-chemistry
/lx-3d-teaching-animation
```

## Keeping translations in sync

The Chinese `README.md` is the documentation source. After translating a source update into every localized README, run:

```bash
python3 scripts/check_i18n_sync.py --update-markers
python3 scripts/check_i18n_sync.py
```

The first command records the current source fingerprint in all six README files. The second verifies the fingerprint, language navigation, skill names, and installation entry point. This is now a manual local check; the GitHub Action has been disabled, so translation synchronization no longer generates GitHub alerts. See [docs/i18n-maintenance.md](docs/i18n-maintenance.md) for the workflow.

## Examples

```text
Use $lx-education-diagnosis in education decision and event review mode. I yelled at my child today. Ask for the full sequence before judging it, then help me repair it.
```

```text
Use $lx-ai-learning-coach to teach me SQL through guided practice. Ask one core question at a time and do not reveal the final answer immediately.
```

```text
Use $lx-interactive-teaching-generator to make an interactive webpage for linear functions. Let students change slope and intercept, synchronize graph, equation, and real-world meaning, and directly deliver one openable HTML file rather than links or a prompt.
```

```text
Use $lx-open-class-ai-diagnosis to review my open class. Read my lesson plan and slides first, then tell me whether AI changes student learning or merely displays a tool.
```

```text
Use $lx-gamified-learning-design to design a learning game for spatial views.
Ask about grade, learning difficulty, and available devices first; make students build, predict, verify, and explain rather than merely answer a quiz.
```

```text
Use $lx-highschool-geometry-chemistry to solve an ellipse focal-chord range problem. Use exact computation so the result, derivation, draggable line, and graph agree, then deliver one openable HTML file.
```

```text
Use $lx-3d-teaching-animation to make a 3D gear-transmission lesson for elementary science.
Let students pause, rotate, and predict the direction of each gear before seeing a step-by-step explanation.
```

## Repository structure

Each folder under `skills/` is independently installable and includes a standard `SKILL.md`, optional Codex interface metadata in `agents/openai.yaml`, and progressively loaded references. See the [Agent Skills specification](https://agentskills.io/specification), [OpenAI Codex Skills documentation](https://developers.openai.com/codex/skills), and [Claude Code Skills documentation](https://code.claude.com/docs/en/skills).

Use [tests/evaluation-cases.md](tests/evaluation-cases.md) for manual regression testing after changes. Future skills are listed in [ROADMAP.md](ROADMAP.md).

## Safety and privacy

This project offers educational reflection, learning support, communication preparation, and small action experiments. It does not replace mental-health, medical, legal, or emergency services.

Do not send an AI real names, school or employer details, home addresses, contact information, confidential documents, classified information, or other unnecessary personal data.
