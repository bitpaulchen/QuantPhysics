import streamlit as st
import pandas as pd
import numpy as np

# 设置页面配置（宽屏模式更适合展示卡片）
st.set_page_config(page_title="Streamlit 函数视觉参考手册", layout="wide")

# 自定义一些简单的 CSS 来美化卡片标题和间距
st.markdown("""
    <style>
    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #ff4b4b;
        margin-bottom: 10px;
    }
    .card-description {
        font-size: 0.9rem;
        color: #666;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 Streamlit 函数视觉参考手册")
st.write("点击侧边栏过滤分类，或直接向下滚动查看各组件的实时显示效果。")

# --- 准备示例数据 ---
df_sample = pd.DataFrame(
    np.random.randn(5, 5),
    columns=(f'列 {i}' for i in range(5))
)

map_data = pd.DataFrame(
    np.random.randn(10, 2) / [50, 50] + [31.23, 121.47], # 以某地为中心的随机点
    columns=['lat', 'lon']
)

# --- 定义渲染函数 ---
def function_card(title, func_name, description, render_callback):
    """通用卡片容器"""
    with st.container(border=True):
        st.markdown(f'<div class="card-title">{title}</div>', unsafe_allow_html=True)
        st.markdown(f'代码: `{func_name}`')
        st.markdown(f'<div class="card-description">{description}</div>', unsafe_allow_html=True)
        st.divider()
        # 执行传入的渲染逻辑
        render_callback()

# --- 分类展示 ---

# 1. 文本展示类
st.header("📝 文本与基础写入")
col1, col2, col3 = st.columns(3)

with col1:
    function_card("万能输出", "st.write", "可以处理文字、数据框、图表等几乎所有内容。", 
                  lambda: st.write("你好，Streamlit！", {"key": "value"}, 123))

with col2:
    function_card("Markdown渲染", "st.markdown", "支持加粗、斜体、列表、甚至 HTML。", 
                  lambda: st.markdown("这是 **粗体**，这是 :blue[彩色文字]"))

with col3:
    function_card("代码展示", "st.code", "带语法高亮的显示代码块。", 
                  lambda: st.code("print('Hello World')", language='python'))


# 2. 数据展示类
st.header("📊 数据展示")
col1, col2, col3 = st.columns(3)

with col1:
    function_card("交互式表格", "st.dataframe", "支持排序、筛选、缩放的 DataFrame。", 
                  lambda: st.dataframe(df_sample, height=150))

with col2:
    function_card("静态表格", "st.table", "纯 HTML 渲染的表格，不支持交互。", 
                  lambda: st.table(df_sample.iloc[:3, :2]))

with col3:
    function_card("指标卡片", "st.metric", "常用于展示 KPI 汇总数据。", 
                  lambda: st.metric(label="访问量", value="1,234", delta="12%"))


# 3. 图表与媒体类
st.header("🗺️ 图表与地图")
col1, col2 = st.columns(2)

with col1:
    function_card("简单折线图", "st.line_chart", "快速绘制基于浏览器的交互图表。", 
                  lambda: st.line_chart(np.random.randn(20, 1)))

with col2:
    function_card("内置地图", "st.map", "自动识别 lat/lon 列并在地图上标点。", 
                  lambda: st.map(map_data, zoom=11))


# 4. 交互组件类（示例）
st.header("🖱️ 常用交互组件")
col1, col2, col3 = st.columns(3)

with col1:
    function_card("按钮", "st.button", "触发特定逻辑的操作。", 
                  lambda: st.button("点我试试"))

with col2:
    function_card("选择框", "st.selectbox", "从列表中选择一项。", 
                  lambda: st.selectbox("请选择", ["选项 A", "选项 B", "选项 C"]))

with col3:
    function_card("滑动条", "st.slider", "拖动选择数值范围。", 
                  lambda: st.slider("选择年龄", 0, 100, 25))

st.info("💡 提示：你可以继续向这个脚本添加 `st.status`, `st.tabs`, `st.expander` 等更多高级功能。")