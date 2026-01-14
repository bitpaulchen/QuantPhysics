import streamlit as st

st.set_page_config(page_title="原子物理 - QuantPhysics")

st.title("原子物理")


import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. 配置页面与样式 (复用之前的学术风格) ---
st.set_page_config(layout="wide", page_title="运动的描述 | QuantPhysics")

# 自定义 CSS：实现学术风卡片
st.markdown("""
<style>
    /* 全局背景 */
    .stApp { background-color: #F8F9FA; }
    
    /* 学术卡片容器 */
    .academic-card {
        background-color: #FFFFFF;
        border: 1px solid #E6E6EA;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    
    /* 标题样式 */
    h3 { color: #262730; font-family: 'Inter', sans-serif; font-weight: 600; }
    h4 { color: #0068C9; margin-top: 0; }
    
    /* 强调文本 */
    .highlight { background-color: #F0F2F6; padding: 2px 6px; border-radius: 4px; color: #FF4B4B; font-weight: 500; }
</style>
""", unsafe_allow_html=True)

# --- 2. UI 组件封装 (解决维护性问题的关键) ---

def render_card(title, content_func, *args, **kwargs):
    """
    一个通用的卡片容器。
    title: 卡片标题
    content_func: 渲染卡片内部内容的函数
    """
    with st.container():
        st.markdown(f"""<div class="academic-card"><h3>{title}</h3>""", unsafe_allow_html=True)
        content_func(*args, **kwargs)
        st.markdown("</div>", unsafe_allow_html=True)

def render_comparison_table(data_dict):
    """
    渲染对比场景（专门处理地球、高铁这种例子）
    """
    cols = st.columns(len(data_dict))
    for idx, (subject, scenarios) in enumerate(data_dict.items()):
        with cols[idx]:
            st.markdown(f"#### 研究对象：{subject}")
            for scenario in scenarios:
                with st.expander(f"{scenario['情景_title']}", expanded=True):
                    st.caption("研究情景")
                    st.write(scenario['情景_desc'])
                    st.caption("核心分析")
                    st.info(scenario['分析'])
                    
                    # 结论使用 Tag 样式
                    if scenario['结论']:
                        st.markdown(f"**结论：** :white_check_mark: <span class='highlight'>可看作质点</span>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"**结论：** :x: <span class='highlight'>不可看作质点</span>", unsafe_allow_html=True)

# --- 3. 具体的教学模块 (逻辑层) ---

def content_particle_model():
    """质点模型的内容逻辑"""
    st.markdown("""
    **定义**：用来代替物体的有质量的点。
    
    **核心思想**：这是一种**理想化物理模型**。当物体的**形状**和**大小**对研究的问题影响可忽略不计时，可将其简化为质点。
    """)
    
    st.divider()
    
    # 结构化数据，方便维护
    comparison_data = {
        "地球": [
            {
                "情景_title": "研究地球公转",
                "情景_desc": "分析地球绕太阳运行的轨道、周期。",
                "分析": "地球直径(1.3万km) 远小于 公转半径(1.5亿km)。形状大小忽略不计。",
                "结论": True
            },
            {
                "情景_title": "研究地球自转",
                "情景_desc": "分析昼夜交替、不同纬度线速度。",
                "分析": "赤道和两极运动状态不同，形状不可忽略。",
                "结论": False
            }
        ],
        "高铁": [
            {
                "情景_title": "北京 -> 上海",
                "情景_desc": "计算京沪线运行时间。",
                "分析": "车长(400m) 远小于 总里程(1300km)。",
                "结论": True
            },
            {
                "情景_title": "通过大桥",
                "情景_desc": "计算通过800m长的大桥的时间。",
                "分析": "车长(200m) 与 桥长(800m) 同数量级，不可忽略。",
                "结论": False
            }
        ]
    }
    
    render_comparison_table(comparison_data)

def content_displacement_vs_distance():
    """位移与路程的可视化对比"""
    c1, c2 = st.columns([1, 2])
    
    with c1:
        st.markdown("""
        - **路程 (Distance)**: 物体运动轨迹的长度。是**标量**（只有大小）。
        - **位移 (Displacement)**: 从初位置指向末位置的有向线段。是**矢量**（有大小和方向）。
        """)
        st.warning("只有在**单向直线运动**中，位移的大小才等于路程。")
        
    with c2:
        # 使用 Plotly 画一个简单的示意图，比静态图片更高端
        fig = go.Figure()
        # 轨迹 (曲线)
        fig.add_trace(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 2, 1, 3, 0], mode='lines', line=dict(color='gray', dash='dot'), name='路程 (轨迹)'))
        # 位移 (直线)
        fig.add_trace(go.Scatter(x=[0, 4], y=[0, 0], mode='lines+markers', line=dict(color='#FF4B4B', width=4), name='位移 (初末位置)'))
        
        fig.update_layout(
            title="可视化对比",
            xaxis_title="x 位置", yaxis_title="y 位置",
            template="plotly_white", height=300, margin=dict(l=20, r=20, t=40, b=20)
        )
        st.plotly_chart(fig, use_container_width=True)

def content_acceleration():
    """加速度的三兄弟辨析"""
    st.markdown("加速度 $a = \\frac{\\Delta v}{\\Delta t}$ 是描述**速度变化快慢**的物理量。")
    
    # 使用 Streamlit 原生 Metric 组件做对比，非常清晰
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric(label="速度 v", value="大", delta="描述运动快慢")
        st.caption("例子：高速飞行的子弹")
    with c2:
        st.metric(label="速度变化量 Δv", value="大", delta="描述速度改变了多少")
        st.caption("例子：百公里加速")
    with c3:
        st.metric(label="加速度 a", value="大", delta="描述速度改变得有多快")
        st.caption("例子：枪膛中击发的瞬间")

# --- 4. 主程序入口 ---

def main():
    st.title("第一章：运动的描述")
    st.caption("Physics 101: Kinematics Basics")

    # 模块 1：质点模型
    render_card("1. 质点模型 (Idealized Model)", content_particle_model)
    
    # 模块 2：参考系 (简单带过)
    render_card("2. 参考系 (Reference Frame)", lambda: st.markdown("运动具有**相对性**。描述运动必须选取参考系。标准参考系通常选取地面。"))
    
    # 模块 3：位移与路程
    render_card("3. 位移 vs 路程 (Vector vs Scalar)", content_displacement_vs_distance)
    
    # 模块 4：加速度
    render_card("4. 加速度 (Acceleration) - 核心难点", content_acceleration)

if __name__ == "__main__":
    main()