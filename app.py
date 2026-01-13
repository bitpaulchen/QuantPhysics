"""
⚛️ QuantPhysics - 量化物理
基于人教版高中物理教材的交互式物理学习平台

技术栈: Streamlit + p5.js + Manim
"""

import streamlit as st

# ============================================
# 页面配置
# ============================================
st.set_page_config(
    page_title="⚛️ QuantPhysics | 量化物理",
    page_icon="⚛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 自定义 CSS - 温暖米色风格（参考截图）
# ============================================
st.markdown("""
<style>
    /* 导入字体 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&family=Space+Grotesk:wght@400;500;700&family=Space+Mono&display=swap');
    
    /* 全局样式 */
    .stApp {
        background-color: #FAF8F5;
    }
    
    /* 主内容区域 */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* 侧边栏样式 */
    [data-testid="stSidebar"] {
        background-color: #F5F3F0;
        border-right: 1px solid #E8E4DE;
    }
    
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #5C5C5C;
        font-family: 'Space Grotesk', 'Noto Sans SC', sans-serif;
    }
    
    [data-testid="stSidebar"] .stMarkdown p,
    [data-testid="stSidebar"] .stMarkdown li {
        color: #7A7A7A;
        font-size: 0.9rem;
        line-height: 1.6;
    }
    
    /* 标题样式 */
    h1 {
        color: #3D3D3D !important;
        font-family: 'Space Grotesk', 'Noto Sans SC', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
    }
    
    h2, h3 {
        color: #4A4A4A !important;
        font-family: 'Space Grotesk', 'Noto Sans SC', sans-serif !important;
        font-weight: 500 !important;
    }
    
    p, li {
        color: #5C5C5C;
        font-family: 'Noto Sans SC', sans-serif;
        line-height: 1.7;
    }
    
    /* 卡片容器 */
    .topic-card {
        background: #FFFFFF;
        border: 1px solid #E8E4DE;
        border-radius: 12px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        transition: all 0.2s ease;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    
    .topic-card:hover {
        border-color: #D4A574;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    
    .topic-card h3 {
        color: #3D3D3D !important;
        margin-bottom: 0.5rem;
        font-size: 1.1rem;
    }
    
    .topic-card p {
        color: #7A7A7A;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* 标签样式 */
    .tag {
        display: inline-block;
        background: #F0EBE4;
        color: #8B7355;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.75rem;
        margin-right: 0.5rem;
        margin-top: 0.75rem;
    }
    
    .tag-highlight {
        background: #E8D5C4;
        color: #8B5A2B;
    }
    
    /* 统计卡片 */
    .stat-card {
        background: #FFFFFF;
        border: 1px solid #E8E4DE;
        border-radius: 12px;
        padding: 1.25rem;
        text-align: center;
    }
    
    .stat-number {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        color: #D4A574;
    }
    
    .stat-label {
        color: #7A7A7A;
        font-size: 0.85rem;
        margin-top: 0.25rem;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #D4A574;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-family: 'Space Grotesk', 'Noto Sans SC', sans-serif;
        font-weight: 500;
        transition: all 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #C49464;
        box-shadow: 0 4px 12px rgba(212, 165, 116, 0.3);
    }
    
    /* 分隔线 */
    hr {
        border: none;
        border-top: 1px solid #E8E4DE;
        margin: 2rem 0;
    }
    
    /* 页脚 */
    .footer {
        text-align: center;
        padding: 2rem 0;
        color: #9A9A9A;
        font-size: 0.8rem;
        border-top: 1px solid #E8E4DE;
        margin-top: 3rem;
    }
    
    /* Streamlit 元素覆盖 */
    .stSelectbox > div > div {
        background-color: #FFFFFF;
        border-color: #E8E4DE;
    }
    
    .stSlider > div > div > div {
        background-color: #D4A574;
    }
    
    /* 隐藏 Streamlit 默认页脚 */
    footer {visibility: hidden;}
    
    /* Expander 样式 */
    .streamlit-expanderHeader {
        background-color: #F5F3F0;
        border-radius: 8px;
    }
    
    /* Metric 样式 */
    [data-testid="stMetricValue"] {
        color: #D4A574;
        font-family: 'Space Grotesk', sans-serif;
    }
    
    [data-testid="stMetricLabel"] {
        color: #7A7A7A;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 侧边栏
# ============================================
with st.sidebar:
    st.markdown("## ⚛️ QuantPhysics")
    st.markdown("欢迎来到量化物理！")
    st.markdown("""
    从左侧导航栏选择专题，探索高中物理的精彩世界。
    
    每个专题包含：
    - 📖 教学文档
    - 🎬 动画演示
    - 🎮 交互仿真
    """)
    
    st.markdown("---")
    
    st.markdown("### 📚 专题导航")
    st.markdown("""
    - 力学基础
    - 电磁学
    - 热学与光学
    - 近代物理
    """)
    
    st.markdown("---")
    
    st.markdown("""
    <div style="font-size: 0.8rem; color: #9A9A9A; margin-top: 1rem;">
    本应用使用 <a href="https://fonts.google.com/specimen/Space+Grotesk" style="color: #D4A574;">Space Grotesk</a> 
    和 <a href="https://fonts.google.com/specimen/Noto+Sans+SC" style="color: #D4A574;">Noto Sans SC</a> 字体。
    </div>
    """, unsafe_allow_html=True)

# ============================================
# 主页内容
# ============================================

# 标题
st.markdown("# QuantPhysics 量化物理")
st.markdown("""
本应用展示高中物理各个专题的交互式学习内容，帮助你直观理解物理概念。
""")

st.markdown("---")

# ============================================
# 统计卡片
# ============================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">16</div>
        <div class="stat-label">物理专题</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">50+</div>
        <div class="stat-label">交互仿真</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">100+</div>
        <div class="stat-label">核心公式</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-card">
        <div class="stat-number">∞</div>
        <div class="stat-label">学习乐趣</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# 专题列表
# ============================================

# 专题数据
topics = {
    "力学": [
        {"name": "直线运动", "desc": "匀速、匀变速直线运动", "icon": "🚀", "tags": ["必修一", "运动学"], "page": "01_linear_motion"},
        {"name": "相互作用", "desc": "力、力的合成与分解", "icon": "⚖️", "tags": ["必修一", "静力学"], "page": "02_interactions"},
        {"name": "牛顿运动定律", "desc": "牛顿三定律及应用", "icon": "🍎", "tags": ["必修一", "动力学"], "page": "03_newtons_laws"},
        {"name": "曲线运动", "desc": "平抛、圆周运动", "icon": "🎯", "tags": ["必修二", "运动学"], "page": "04_curvilinear_motion"},
        {"name": "万有引力", "desc": "万有引力定律、天体运动", "icon": "🌍", "tags": ["必修二", "天体"], "page": "05_universal_gravitation"},
        {"name": "机械能守恒", "desc": "功、能、机械能守恒", "icon": "⚡", "tags": ["必修二", "能量"], "page": "06_mechanical_energy"},
        {"name": "动量", "desc": "动量、冲量、动量守恒", "icon": "💥", "tags": ["选择性必修一", "守恒"], "page": "07_momentum"},
        {"name": "机械振动", "desc": "简谐振动、单摆", "icon": "〰️", "tags": ["选择性必修一", "振动"], "page": "08_mechanical_vibration"},
    ],
    "电磁学": [
        {"name": "电场", "desc": "电场强度、电势", "icon": "⚡", "tags": ["必修三", "静电"], "page": "09_electric_field"},
        {"name": "电流", "desc": "电路、欧姆定律", "icon": "🔌", "tags": ["必修三", "电路"], "page": "10_electric_current"},
        {"name": "磁场", "desc": "磁场、洛伦兹力", "icon": "🧲", "tags": ["选择性必修二", "磁学"], "page": "11_magnetic_field"},
        {"name": "电磁感应", "desc": "法拉第定律、楞次定律", "icon": "🔄", "tags": ["选择性必修二", "感应"], "page": "12_electromagnetic_induction"},
        {"name": "交变电流", "desc": "交流电、变压器", "icon": "📊", "tags": ["选择性必修二", "交流"], "page": "13_alternating_current"},
    ],
    "热学与光学": [
        {"name": "光学", "desc": "几何光学、物理光学", "icon": "🌈", "tags": ["选择性必修一", "波动"], "page": "14_optics"},
        {"name": "热学", "desc": "热力学定律、理想气体", "icon": "🌡️", "tags": ["选择性必修三", "热力学"], "page": "15_thermodynamics"},
    ],
    "近代物理": [
        {"name": "原子物理", "desc": "原子结构、核物理", "icon": "⚛️", "tags": ["选择性必修三", "量子"], "page": "16_atomic_physics"},
    ]
}

# 渲染专题列表
for category, items in topics.items():
    st.markdown(f"### 📁 {category}")
    
    cols = st.columns(2)
    for i, topic in enumerate(items):
        with cols[i % 2]:
            # 生成标签 HTML
            tags_html = "".join([f'<span class="tag">{tag}</span>' for tag in topic["tags"]])
            
            st.markdown(f"""
            <div class="topic-card">
                <h3>{topic["icon"]} {topic["name"]}</h3>
                <p>{topic["desc"]}</p>
                {tags_html}
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

# ============================================
# 快速入门
# ============================================
st.markdown("---")
st.markdown("### 🚀 快速入门")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="topic-card">
        <h3>🎮 交互操作指南</h3>
        <p>在物理仿真中，你可以：</p>
        <ul style="color: #7A7A7A; font-size: 0.9rem;">
            <li><b>空格键</b> - 暂停/继续模拟</li>
            <li><b>R 键</b> - 重置场景</li>
            <li><b>鼠标点击</b> - 添加物体或设置参数</li>
            <li><b>方向键</b> - 调整物理参数</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="topic-card">
        <h3>📖 学习建议</h3>
        <p>推荐的学习路径：</p>
        <ol style="color: #7A7A7A; font-size: 0.9rem;">
            <li>先阅读<b>概念讲解</b>，理解物理原理</li>
            <li>观看 <b>Manim 动画</b>，建立直观印象</li>
            <li>动手操作 <b>p5.js 仿真</b>，深入理解</li>
            <li>完成<b>思考题</b>，巩固知识</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# 页脚
# ============================================
st.markdown("""
<div class="footer">
    <p>⚛️ QuantPhysics | 基于人教版高中物理教材</p>
    <p>Powered by Streamlit + p5.js + Manim</p>
</div>
""", unsafe_allow_html=True)
