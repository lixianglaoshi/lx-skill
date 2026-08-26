# 单文件手势教学网页契约

## 交付格式

- 有文件系统时，成品是当前工作目录或用户指定位置的一个 `.html` 文件；不要附带构建项目、临时脚本、截图或多个资源文件。
- 无文件系统时，输出一个从 `<!DOCTYPE html>` 到 `</html>` 的完整 HTML，不加解释文字；不可只给 URL。
- CSS 与业务 JavaScript 内联。可以通过固定版本 CDN 加载 Three.js 与 MediaPipe Tasks Vision 的模块/WASM/模型；这些请求是实现摄像头追踪的公开依赖，不是交付替代品。
- 若用户要求离线，不能假装完整 MediaPipe 能离线工作：交付同一 HTML 的鼠标/键盘模拟模式，并清楚标出“离线无摄像头”。只有用户提供可再分发的本地模型时才可内嵌真实手势模型。

## 页面状态机

初始状态必须是 `camera-off`，并在首屏提供：

1. “开启手势/摄像头”——由用户点击后才调用 `navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' }, audio: false })`。
2. “鼠标/键盘体验”——无需摄像头即可完整使用。
3. “关闭摄像头”——停止 `stream.getTracks().forEach(track => track.stop())`，清空 video `srcObject`，回到替代控制。
4. 状态文案——明确显示未开启、请求权限、识别中、未检测到手、权限被拒绝、兼容性不足、替代模式。

说明：浏览器对摄像头通常要求 HTTPS 或 `localhost`。交付仍然是单 HTML；若用户双击打开后浏览器拒绝摄像头，页面必须仍能用替代控制，并显示如何用可信 HTTPS 或本地开发地址打开，而不是只留下报错。

## 追踪实现

推荐使用官方 MediaPipe Tasks Vision 的 `HandLandmarker`：`FilesetResolver.forVisionTasks()` 加载 Wasm，随后用 `HandLandmarker.createFromOptions()` 指定 `runningMode: 'VIDEO'`、`numHands`、检测/存在/追踪置信度与模型路径。每个视频帧用 `detectForVideo(video, performance.now())` 获取最多两只手的 21 个 landmark。

截至本 Skill 更新日，单 HTML 的已校验固定资源为：

```js
const MEDIAPIPE_VERSION = "1.0.1";
const MEDIAPIPE_MODULE_URL =
  "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@1.0.1/vision_bundle.mjs";
const MEDIAPIPE_WASM_ROOT =
  "https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@1.0.1/wasm";
const HAND_LANDMARKER_MODEL_URL =
  "https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task";
```

`@mediapipe/tasks-vision@0.10.22` 并不是可用的 NPM 发布版本，禁止生成该版本或 `https://cdnjsdelivr.net`（缺少 `cdn.`）这类地址。禁止把状态文案、异常文本或 HTML 字符串拼接到模块 URL；模块 URL 必须是上述独立常量。

“开启手势”必须先显示“正在加载手势引擎”，并按 `加载模块 → 初始化 Wasm/模型 → 申请摄像头 → 开始追踪` 执行。使用 `await import(MEDIAPIPE_MODULE_URL)` 的 `try/catch`；任何加载失败都只在状态区显示清晰中文原因和“继续使用鼠标/键盘”的入口，技术错误放在可展开诊断区，绝不把失败 URL 或异常对象直接塞进主界面。引擎/模型未就绪前不得申请摄像头。

也可在需要现成分类时使用 `GestureRecognizer`，但仍要保留 landmark 级的连续变量（如捏合距离）。渲染循环与手势推理应避免互相阻塞：只有新的 video frame 才推理；低性能设备可把检测降至 20–30 FPS，3D 保持独立动画帧。

## 稳定识别

- 距离阈值以掌宽或腕到中指掌指关节的距离归一化，不能使用所有镜头通用的固定像素阈值。
- 对手腕、食指尖、拇指尖等坐标用指数平滑；连续量用 `lerp`，并保留屏幕数值/刻度。
- 离散手势必须连续稳定约 200–350 ms，再改变状态；形状/主题切换等一次性命令至少 500–800 ms 冷却。
- 区分 `gestureCandidate`、`stableGesture` 和 `lastCommittedGesture`；无手或置信度不足时停止发新命令，保留当前模型状态。
- 摄像头镜像与屏幕坐标需要统一。UI 同时显示正在识别的手势和校准提示，不能用隐蔽手型。

## 手势教学页必备 UI

- 一个低干扰、可关闭的镜像视频和关键点叠层；不能遮挡核心学习模型。
- 摄像头权限说明：本页面不录制、不上传、不保存画面；明确公开 CDN/模型依赖可能联网。
- 手势卡：图标/文字、控制的学科变量、鼠标/键盘等价操作。
- 学习 HUD：当前变量、单位、公式/图表读数、识别状态、暂停/重置/重新校准。
- 每一个核心操作必须有预测或解释提示；小测只在操作后出现且可折叠。

## 直接操控要求

- 摄像头手势必须有对应的空间化视觉工具：抓取环、手势射线、能量束、掌心力场或可见的双手约束线。它要跟随平滑后的手部位置/方向，而不是停在 HUD 旁边。
- 捏合、掌心、手距、掌面方向、挥手等用户选择的动作，必须直接改变模型的变换、结构状态、轨道约束或粒子速度场；HUD 数字、公式和图表只订阅相同的模型状态。
- 为抓取类交互实现 `hover → 选中 → 抓住 → 拖动/约束 → 释放` 的清楚状态；为力场类交互实现明确作用半径、强度衰减和粒子/场线可见响应。不是只让相机跟着手转。
- 鼠标/触摸替代要模拟同一抓取、力场、拆解或组装操作。不能因为有鼠标替代，就把摄像头手势退化为控制数字滑块。
- 摄像头开启后 5 秒内，关闭所有 HUD 仍应能看出手正在作用于什么。若只看见数值在变、物体静止，页面验收失败。

## 验收清单

在至少一种现代 Chromium 浏览器中检查：权限同意、拒绝、关闭、无摄像头、单手、双手、短暂遮挡、手势抖动、窗口缩放、触摸/鼠标替代、重置。验证“一个动作直接作用于它声明的对象/粒子”，再由同一状态推导变量；不能只验证数字改变。
