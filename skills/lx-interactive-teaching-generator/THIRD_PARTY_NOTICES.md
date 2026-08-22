# Third-party notices

`lx-interactive-teaching-generator` uses the original AetherViz Master prompt resource as its interactive-webpage generation engine.

| Component | Upstream | License | Location in this skill |
| --- | --- | --- | --- |
| AetherViz Master | https://github.com/andyhuo520/aetherviz-master | MIT | `vendor/aetherviz-master/` |

The upstream files in `vendor/aetherviz-master/` are retained without modification from the user-provided local installation on 2026-08-22. The upstream MIT license is preserved at `vendor/aetherviz-master/LICENSE` and duplicated at this skill's root as `LICENSE` for package-level visibility.

The LX wrapper (`SKILL.md` and `agents/openai.yaml`) adds delivery, teaching, and routing constraints. It does not claim ownership of the upstream source files.
