import streamlit as st
# from utils import apply_global_styles

# ============================================
# 页面配置
# ============================================
st.set_page_config(
    page_title="QuantPhysics",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# 全局样式
# ============================================
# apply_global_styles()

# ============================================
# 页面定义
# ============================================
pages = {
    "欢迎": [
        st.Page("pages/00_home.py", title="首页", icon=":material/home:", default=True),
        st.Page("pages/99_samples.py", title="语法案例", icon=":material/menu:")
    ],
    "力学": [
        st.Page("pages/01_linear_motion.py", title="直线运动", icon=":material/trending_flat:"),
        st.Page("pages/02_interactions.py", title="相互作用", icon=":material/swap_horiz:"),
        st.Page("pages/03_newtons_laws.py", title="牛顿运动定律", icon=":material/speed:"),
        st.Page("pages/04_curvilinear_motion.py", title="曲线运动", icon=":material/turn_right:"),
        st.Page("pages/05_universal_gravitation.py", title="万有引力", icon=":material/public:"),
        st.Page("pages/06_mechanical_energy.py", title="机械能守恒定律", icon=":material/bolt:"),
        st.Page("pages/07_momentum.py", title="动量", icon=":material/sports_tennis:"),
        st.Page("pages/08_mechanical_vibration.py", title="机械振动", icon=":material/waves:"),
    ],
    "电磁学": [
        st.Page("pages/09_electric_field.py", title="电场", icon=":material/electric_bolt:"),
        st.Page("pages/10_electric_current.py", title="电流", icon=":material/power:"),
        st.Page("pages/11_magnetic_field.py", title="磁场", icon=":material/attractions:"),
        st.Page("pages/12_electromagnetic_induction.py", title="电磁感应", icon=":material/sync_alt:"),
        st.Page("pages/13_alternating_current.py", title="交流电", icon=":material/graphic_eq:"),
    ],
    "其他": [
        st.Page("pages/14_optics.py", title="光学", icon=":material/light_mode:"),
        st.Page("pages/15_thermodynamics.py", title="热学", icon=":material/thermostat:"),
        st.Page("pages/16_atomic_physics.py", title="原子物理", icon=":material/blur_on:"),
    ]
}

# ============================================
# 运行导航
# ============================================
pg = st.navigation(pages, position="sidebar")
pg.run()
