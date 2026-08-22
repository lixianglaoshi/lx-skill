# Third-party notices

`lx-highschool-geometry-chemistry` routes three retained edulab modules for exact, interactive teaching pages.

| Component | Upstream | License | Location in this skill |
| --- | --- | --- | --- |
| edulab / solid geometry | https://github.com/wy51ai/edulab | Apache-2.0 | `vendor/edulab/edu-solid-geometry/` |
| edulab / analytic geometry | https://github.com/wy51ai/edulab | Apache-2.0 | `vendor/edulab/edu-analytic-geometry/` |
| edulab / chemistry reactions | https://github.com/wy51ai/edulab | Apache-2.0 | `vendor/edulab/edu-chem-reaction/` |

edulab is copyright 2026 WY (@akokoi1). The upstream files were copied without modification from the user-provided local installation on 2026-08-22. The Apache-2.0 license and required notice are retained in `licenses/EDULAB-APACHE-2.0.txt` and `licenses/EDULAB-NOTICE.txt`.

The LX wrapper (`SKILL.md` and `agents/openai.yaml`) adds routing, Chinese teaching adaptation, and single-HTML delivery constraints. It does not claim ownership of upstream source files.
