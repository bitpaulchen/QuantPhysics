import streamlit as st
import pandas as pd
import numpy as np
import time
# 设置页面配置（宽屏模式更适合展示卡片）
st.set_page_config(
    page_title="Streamlit 函数视觉参考手册", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义一些简单的 CSS 来美化卡片标题和间距
st.markdown("""
    <style>
    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #C87455;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Streamlit 函数视觉参考手册")
from numpy.random import default_rng as rng
# --- 准备示例数据 ---
df_sample = pd.DataFrame(
    np.random.randn(5, 5),
    columns=(list('ABCDE'))
)

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [31.23, 121.47], # 以某地为中心的随机点
    columns=['lat', 'lon']
)

# --- 定义列管理器 ---
# --- 定义列管理器 ---
class ColumnManager:
    """自动管理3列布局的列管理器"""
    def __init__(self,category,  num_cols=3):
        self.num_cols = num_cols
        self.current_cols = None
        self.current_index = 0
        self.category = category
        self.api_prefix = f"https://docs.streamlit.io/develop/api-reference/{category}"
    def get_column(self):
        """获取下一个可用的列，如果当前行已满则自动创建新行"""
        if self.current_cols is None or self.current_index >= self.num_cols:
            self.current_cols = st.columns(self.num_cols)
            self.current_index = 0
        col = self.current_cols[self.current_index]
        self.current_index += 1
        return col
    
    def card(self, func_name, render_callback):
        """直接在列中渲染卡片，无需手动管理列"""
        with self.get_column():
            with st.container(border=True):
                doc_url = f"{self.api_prefix}/{func_name}"
                st.markdown(f'<div class="card-title"><a href="{doc_url}" target="_blank">{func_name}</a></div>', unsafe_allow_html=True)
                render_callback()




st.header("Text elements")
cols = ColumnManager('text', 3)
# st.title("This is a title")
cols.card("st.title", lambda: st.title("_Streamlit_ is :blue[cool] :sunglasses:"))

cols.card("st.header", lambda: st.header("This is a header with a divider", divider="gray"))
cols.card("st.subheader", lambda: st.subheader("This is a subheader"))
cols.card("st.markdown", lambda: st.markdown("这是 **粗体**，这是 :blue[彩色文字]"))
cols.card("st.badge", lambda: st.badge("Success", icon=":material/check:", color="green"))
cols.card("st.caption", lambda: st.caption("This is a caption"))
cols.card("st.code", lambda: st.code("print('Hello World')", language='python'))
cols.card("st.divider", lambda: st.divider())
cols.card("st.echo", lambda: st.echo("This is a echo"))
cols.card("st.latex", lambda: st.latex(r'''
     a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
)
cols.card("st.text", lambda: st.text("This is a text"))
# cols.card("st.help", lambda: st.help("This is a help"))
cols.card("st.html", lambda: st.html("<h1>This is a html</h1>"))


st.header("Data elements")

cols = ColumnManager('data', 3)
cols.card("st.dataframe", lambda: st.dataframe(df_sample, height=150))
cols.card("st.data_editor", lambda: st.data_editor(df_sample))
cols.card("st.table", lambda: st.table(df_sample.iloc[:3, :2]))
cols.card("st.metric", lambda: st.metric(label="访问量", value="1,234", delta="12%"))
cols.card("st.json", lambda: st.json({"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}))

st.header("Chart elements")
cols = ColumnManager('charts', 2)
cols.card("st.area_chart", lambda: st.area_chart(np.random.randn(20, 1)))
cols.card("st.bar_chart", lambda: st.bar_chart(np.random.randn(20, 1)))
cols.card("st.line_chart", lambda: st.line_chart(np.random.randn(20, 1)))
cols.card("st.map", lambda: st.map(map_data))
df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])
cols.card("st.scatter_chart", lambda: st.scatter_chart(df))

import altair as alt
df = pd.DataFrame(rng(0).standard_normal((60, 3)), columns=["a", "b", "c"])

chart = (
    alt.Chart(df)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

cols.card("st.altair_chart", lambda: st.altair_chart(chart))


import graphviz

cols.card("st.graphviz_chart", lambda: \
st.graphviz_chart('''
    digraph {
        run -> intr
        intr -> runbl
        runbl -> run
        run -> kernel
        kernel -> zombie
        kernel -> sleep
        kernel -> runmem
        sleep -> swap
        swap -> runswap
        runswap -> new
        runswap -> runmem
        new -> runmem
        sleep -> runmem
    }
''')

)


st.header("Input widgets")

cols = ColumnManager('widgets',3)

# 按钮类
cols.card("st.button", lambda: st.button("点我试试"))
cols.card("st.download_button", lambda: st.download_button("下载数据", data=df_sample.to_csv().encode('utf-8'), file_name="data.csv", mime="text/csv"))
cols.card("st.link_button", lambda: st.link_button("访问 Streamlit", "https://streamlit.io"))
cols.card("st.page_link", lambda: st.page_link("pages/00_home.py", label="跳转到首页", icon="🏠"))

# 表单提交按钮（需要在表单中使用）
with cols.get_column():
    with st.container(border=True):
        st.markdown('<div class="card-title">st.form_submit_button</div>', unsafe_allow_html=True)
        with st.form("example_form"):
            st.text_input("输入内容")
            st.form_submit_button("提交表单")

# 选择类
cols.card("st.checkbox", lambda: st.checkbox("我同意条款"))
cols.card("st.radio", lambda: st.radio("选择选项", ["选项 A", "选项 B", "选项 C"]))
cols.card("st.selectbox", lambda: st.selectbox("请选择", ["选项 A", "选项 B", "选项 C"]))
cols.card("st.multiselect", lambda: st.multiselect("多选", ["选项 A", "选项 B", "选项 C", "选项 D"]))
cols.card("st.toggle", lambda: st.toggle("开启/关闭"))
cols.card("st.pills", lambda: st.pills("选择标签", ["标签1", "标签2", "标签3"], default=["标签1"]))
cols.card("st.segmented_control", lambda: st.segmented_control("分段控制", ["选项1", "选项2", "选项3"]))

# 滑块和数值输入
cols.card("st.slider", lambda: st.slider("选择年龄", 0, 100, 25))
cols.card("st.select_slider", lambda: st.select_slider("选择数值", options=[1, 2, 3, 5, 8, 13, 21, 34]))
cols.card("st.number_input", lambda: st.number_input("输入数字", min_value=0, max_value=100, value=50, step=1))

# 颜色选择
cols.card("st.color_picker", lambda: st.color_picker("选择颜色", "#C87455"))

# 日期时间输入
cols.card("st.date_input", lambda: st.date_input("选择日期"))
cols.card("st.time_input", lambda: st.time_input("选择时间"))
cols.card("st.datetime_input", lambda: st.datetime_input("选择日期时间"))

# 文本输入
cols.card("st.text_input", lambda: st.text_input("输入文本", placeholder="请输入..."))
cols.card("st.text_area", lambda: st.text_area("多行文本", placeholder="请输入多行文本..."))

# 反馈
cols.card("st.feedback", lambda: st.feedback("stars"))

# 聊天输入
cols.card("st.chat_input", lambda: st.chat_input("发送消息"))

# 文件上传
cols.card("st.file_uploader", lambda: st.file_uploader("上传文件", type=['csv', 'txt', 'pdf']))

# 媒体输入
cols.card("st.audio_input", lambda: st.audio_input("录制音频"))


st.header("Media elements")
cols = ColumnManager('media',3)
cols.card("st.audio", lambda: st.audio("https://www.soundjay.com/Human/male-laugh-1.wav"))
cols.card("st.image", lambda: st.image("https://picsum.photos/200/300"))
cols.card("st.video", lambda: st.video("https://static.streamlit.io/examples/star.mp4"))


st.header("Layouts and containers")
# cols = ColumnManager('layout',3)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# 容器
with st.container():
    st.write("This is inside the container")

    # You can call any Streamlit command, including custom components:
    st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")

# 空容器
st.sidebar.header("Empty container")
placeholder = st.empty()
placeholder.markdown("Hello")
time.sleep(1)

placeholder.progress(0, "Wait for it...")
time.sleep(0.5)
placeholder.progress(100, "Wait for it...")
time.sleep(1)
placeholder.markdown("success!!!")


# cols.card("st.dialog", lambda: st.dialog())
# cols.card("st.empty", lambda: st.empty())
# cols.card("st.expander", lambda: st.expander("Expand me"))
# cols.card("st.form", lambda: st.form("example_form"))
# cols.card("st.popover", lambda: st.popover("Popover me"))
# cols.card("st.sidebar", lambda: st.sidebar())

# Using object notation
add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )


# cols.card("st.space", lambda: st.space(10))
# cols.card("st.tabs", lambda: st.tabs(["Tab 1", "Tab 2", "Tab 3"]))


st.header("Status elements")      
cols = ColumnManager('status',3)
cols.card("st.success", lambda: st.success("success"))
cols.card("st.info", lambda: st.info("info"))
cols.card("st.warning", lambda: st.warning("warning"))
cols.card("st.error", lambda: st.error("error"))
cols.card("st.exception", lambda: st.exception("exception"))
cols.card("st.progress", lambda: st.progress(0.5))
cols.card("st.spinner", lambda: st.spinner("Spinning..."))
cols.card("st.status", lambda: st.status("status"))
def toast_example():
    if st.button("Three cheers"):
        st.toast("Hip!")
        time.sleep(0.5)
        st.toast("Hip!")
        time.sleep(0.5)
        st.toast("Hooray!", icon="🎉")

cols.card("st.toast", toast_example)
def balloons_example():
    if st.button("balloons cheers"):
        st.balloons()

def snow_example():
    if st.button("snow cheers"):
        st.snow()
cols.card("st.balloons", balloons_example)
cols.card("st.snow", snow_example)