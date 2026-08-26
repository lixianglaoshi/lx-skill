# 公开研究笔记与许可边界

本 Skill 于 2026-08-26 调研了如下公开资料，用来学习**高层机制和提示词结构**，不复制其代码、页面、素材、角色设定、品牌或未经明确许可的文字：

| 来源 | 观察到的可迁移机制 | 许可/使用边界 |
| --- | --- | --- |
| [PixelPalm](https://github.com/Niraj-Ramnani/PixelPalm) | 以握拳、张掌、捏合驱动 3D 粒子文字；21 个手部点 → 手势状态 → 物理反馈闭环 | 仓库页面未显示 LICENSE；仅学习机制，不收录源码/素材 |
| [ULTRON Orb UI](https://github.com/SAGAR-TAMANG/ultron-by-sagar-builds) | 单手捏合移动旋转、双手捏合距离缩放；捏合判断采用迟滞，视觉/控制分层 | MIT；本 Skill 仍不复制其代码与设计素材 |
| [threejs-handtracking-101](https://github.com/collidingScopes/threejs-handtracking-101) | 左右手分工、触碰变色、摄像头状态可见、基础 3D 交互 | MIT；只学习高层交互设计 |
| [NEURAL HAND](https://github.com/monish4030/NEURAL-HAND) | 手势状态 HUD、开掌/握拳/指向/捏合/拇指的明确映射与备用控制思路 | MIT；不复制其赛博 UI 或源码 |
| [MediaPipe Tasks Vision 官方文档](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker/web_js) | JavaScript `HandLandmarker`、Wasm、模型路径、视频帧检测与 21 landmark | Apache-2.0；实现时遵循其许可与官方分发方式 |
| [手势粒子单 HTML 提示词示例](https://www.theaicowboys.com/blog/gesture-controlled-particle-system-threejs-mediapipe) | 强提示词应清楚规定：单 HTML、技术栈、摄像头预览、明确映射、HUD、性能和交付形式 | 只学习提示词的结构，避免复制其品牌对象、代码和长段文字 |

MediaPipe 的官方资料说明手部跟踪可在设备端处理输入；但加载 SDK/Wasm/模型通常需要网络。生成页面必须准确说明摄像头数据处理与外部资源请求，不能笼统承诺“完全不联网”。

遇到没有 LICENSE、许可不清或与商业分发不兼容的项目，一律只提取抽象的交互原则，并独立实现；不要 vendor、复刻页面、搬运模型或把灵感项目描述为 LX 原创。
