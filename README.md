# ⚛️ QuantPhysics (量化物理)

本项目基于人教版高中物理教材体系（必修/选修）， page 每个page涵盖某个专题（比如直线运动）的教案文档、动画视频、可交互动画：
## 🛠️ 技术架构 (Tech Stack)

本项目采用 Streamlit + p5.js + manim 作为底层技术栈：

| 层级 | 技术 | 说明 |
| :--- | :--- | :--- |
| **应用层** | **Streamlit** | 负责网站导航、文字排版、LaTeX公式渲染、用户状态管理。 |
| **交互层** | **p5.js / Plotly** | 嵌入 Streamlit 组件中，负责高帧率(60FPS)的物理仿真。 |
| **视频层** | **Manim** | 离线生成高质量 MP4，嵌入网站进行教学展示。 |

## 📂 目录结构 (Directory Structure)

```text
QuantPhysics/
├── app.py                  # Streamlit 主入口
├── requirements.txt        # Python 依赖
├── assets/                 # 静态资源
│   ├── videos/             # Manim 生成的视频文件
│   └── images/             # 教学插图
├── pages/                  # Streamlit 多页面路由
│   └── ...
├── simulations/            # p5.js 交互代码库
│   ├── templates/          # HTML 模板
│   └── collision.js        # 碰撞逻辑
└── utils/                  # 工具函数

```
## PAGES LIST
|序号|专题|文件名|英文文件名|说明|
|---|---|---|---|---|
|1|直线运动|直线运动.py|linear_motion.py|匀速、匀变速直线运动|
|2|相互作用|相互作用.py|interactions.py|力、力的合成与分解|
|3|牛顿运动定律|牛顿运动定律.py|newtons_laws.py|牛顿三定律及应用|
|4|曲线运动|曲线运动.py|curvilinear_motion.py|平抛、圆周运动|
|5|万有引力|万有引力.py|universal_gravitation.py|万有引力定律、天体运动|
|6|机械能守恒定律|机械能守恒.py|mechanical_energy.py|功、能、机械能守恒|
|7|动量|动量.py|momentum.py|动量、冲量、动量守恒|
|8|机械振动|机械振动.py|mechanical_vibration.py|简谐振动、单摆|
|9|电场|电场.py|electric_field.py|电场强度、电势|
|10|电流|电流.py|electric_current.py|电路、欧姆定律|
|11|磁场|磁场.py|magnetic_field.py|磁场、洛伦兹力|
|12|电磁感应|电磁感应.py|electromagnetic_induction.py|法拉第定律、楞次定律|
|13|交变电流|交变电流.py|alternating_current.py|交流电、变压器|
|14|光学|光学.py|optics.py|几何光学、物理光学|
|15|热学|热学.py|thermodynamics.py|热力学定律、理想气体|
|16|原子物理|原子物理.py|atomic_physics.py|原子结构、核物理|
