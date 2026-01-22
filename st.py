import streamlit as st
import pandas as pd
import numpy as np

# 设置页面配置（宽屏模式更适合展示卡片）
st.set_page_config(page_title="Streamlit 函数视觉参考手册", layout="wide")
pages = {
    "欢迎": [
        st.Page("pages/00_home.py", title="首页", icon=":material/home:", default=True),
        st.Page("pages/99_samples.py", title="语法案例", icon=":material/menu:"),
        st.Page("pages/97_test.py", title="test", icon=":material/menu:")
    ]}

pg = st.navigation(pages, position="sidebar")
pg.run()
