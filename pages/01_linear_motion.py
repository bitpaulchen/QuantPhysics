import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import json

from utils.components import render_choice_question
from utils.components import embed_p5_sketch

# 加载选择题数据
with open('assets/datas/choice_question.json', 'r') as f:
    question_data = json.load(f)

st.set_page_config(page_title="直线运动 - QuantPhysics", layout="wide")
# apply_global_styles()

# --- 页面内容 ---

st.title("运动的描述")
st.badge("必修一", color="blue")


# --- 1. 质点模型 ---
## 1.1 概念

st.header("质点模型")
st.markdown("##### 概念")
st.markdown("用来代替物体的有质量的点。这是一种**理想化**模型——当物体的形状和大小对研究问题的影响可忽略时，可将其简化为质点。")
st.info("**判断准则**: 能否视为质点，取决于**研究问题**，而非**物体本身的大小**。同一物体在不同情境下结论不同。")

## 1.2案例
st.markdown("##### 案例")
confusion_matrix = pd.DataFrame(
    {
        "对象": ["地球","地球","列车","列车"],
        "情境": ["研究公转轨道","研究自转现象","计算京沪运行时间","计算过桥时间"],
        "分析": [
            "地球直径 1.3×10⁴ km，远小于公转半径 1.5×10⁸ km",
            "赤道与两极运动状态不同，形状不可忽略",
            "车长 400m，远小于总里程 1300km",
            "车长 200m 与桥长 800m 同数量级",
        ],
        "结论": [":green[**可视为质点** ]",":red[**不可视为质点**]",":green[**可视为质点** ]",":red[**不可视为质点**]"],
    }
)
st.table(confusion_matrix)



# 使用 tabs 分块显示三个真题
st.markdown("##### 真题测试")
tab1, tab2, tab3 = st.tabs(["真题一", "真题二", "真题三"])

with tab1:
    key = "zhidian_q1"
    render_choice_question(question_data[key], key)

with tab2:
    key = "zhidian_q2"
    render_choice_question(question_data[key], key)

with tab3:
    key = "zhidian_q3"
    render_choice_question(question_data[key], key)

st.markdown("### 直线运动动画演示")
embed_p5_sketch(
    sketch_path="assets/sketches/linear_motion.js",
    width=800,
    height=400
)
# --- 2. 参考系 ---
st.header("参考系")
st.markdown("##### 概念")
st.markdown("为了描述物体的运动而**假定不动的物体**叫做参考系。描述同一物体的运动时，选择不同的参考系，观察结果可能不同。")
st.info("**关键理解**: 参考系的选择是**任意的**，但通常选择**地面**或**相对地面静止的物体**作为参考系。选择不同的参考系，物体的运动状态描述会不同。")

st.markdown("##### 案例")
reference_frame_cases = pd.DataFrame(
    {
        "情境": ["坐在行驶的火车中看窗外的树", "坐在行驶的火车中看车厢内的乘客", "研究地球公转", "研究飞机在空中的位置"],
        "参考系": ["火车（或地面）", "火车", "太阳", "地面"],
        "观察结果": [
            "树向后运动（以火车为参考系）或火车向前运动（以地面为参考系）",
            "乘客相对静止",
            "地球绕太阳运动",
            "飞机位置不断变化"
        ],
        "说明": [
            ":blue[**运动的相对性**]：同一物体，不同参考系，运动状态不同",
            ":green[**相对静止**]：两物体相对位置不变",
            ":orange[**天体运动**]：通常以恒星为参考系",
            ":purple[**位置描述**]：需要明确参考系才能准确描述"
        ],
    }
)
st.table(reference_frame_cases)

# 使用 tabs 分块显示三个真题
st.markdown("##### 真题测试")
tab1, tab2, tab3 = st.tabs(["真题一", "真题二", "真题三"])

with tab1:
    key = "cankaoxi_q1"
    render_choice_question(question_data[key], key)

with tab2:
    key = "cankaoxi_q2"
    render_choice_question(question_data[key], key)

with tab3:
    key = "cankaoxi_q3"
    render_choice_question(question_data[key], key)





# --- 3. 位移与路程 ---
st.header("位移与路程")
st.markdown("##### 概念对比")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**位移 (Displacement)**
- 定义：从初位置到末位置的**有向线段**
- 性质：**矢量**（有大小、有方向）
- 特点：可正可负，取决于方向
""")

with col2:
    st.markdown("""
**路程 (Distance)**
- 定义：物体运动轨迹的**实际长度**
- 性质：**标量**（只有大小）
- 特点：只能为正，只增不减
""")

st.info("**关键区别**：物体往返运动时，位移可能为零，但路程一直在增加。")

st.markdown("##### 动画演示")
st.caption("点击画面可重置动画")
embed_p5_sketch(
    sketch_path="assets/sketches/displacement_distance.js",
    width=720,
    height=370
)

# --- 4. 速度 ---
st.header("速度")


# --- 5. 加速度 ---
st.header("加速度")
st.markdown("##### 概念")
st.markdown("""
**加速度**：描述速度变化快慢的物理量，定义为速度的变化量与时间的比值。

$$a = \\frac{\\Delta v}{\\Delta t} = \\frac{v - v_0}{t}$$
""")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
**加速（v 与 a 同向）**
- 速度增大
- v-t 图斜率与 v 符号相同
""")

with col2:
    st.markdown("""
**减速（v 与 a 反向）**
- 速度减小
- v-t 图斜率与 v 符号相反
""")

st.info("**关键理解**：加速度的方向由力的方向决定，与速度方向无关。v 与 a 同向则加速，反向则减速。")

st.markdown("##### 动画演示")
st.caption("拖动滑块调整加速度，观察小车运动状态和 v-t 图像变化。点击画面可重置。")
embed_p5_sketch(
    sketch_path="assets/sketches/velocity_acceleration.js",
    width=720,
    height=440
)