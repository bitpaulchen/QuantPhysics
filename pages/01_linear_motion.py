import streamlit as st
import plotly.graph_objects as go
from utils import apply_global_styles

st.set_page_config(page_title="直线运动 - QuantPhysics", layout="wide")
apply_global_styles()

# --- 页面内容 ---

st.title("运动的描述")
st.caption("必修一")



# 简单版本
st.info('点击"Save to workspace" 将计划保存到 `.cursor/plans/` 中。这既为你的团队创建文档,也为后续工作提供上下文。',icon=":material/trending_flat:")

# 或者使用 st.markdown 配合 st.code
st.markdown('点击"Save to workspace" 将计划保存到')
st.code('.cursor/plans/', language=None)
st.markdown('中。这既为你的团队创建文档,也为后续工作提供上下文。')

st.success('This is a success message!', icon="✅")
# --- 1. 质点模型 ---
st.markdown("#### 质点模型")

st.markdown("用来代替物体的有质量的点。这是一种**理想化**模型——当物体的形状和大小对研究问题的影响可忽略时，可将其简化为质点。")


st.markdown("### 判断准则")
st.markdown("能否视为质点，取决于**研究问题**，而非**物体本身的大小**。同一物体在不同情境下结论不同：")

# 质点判断表格
st.markdown("""
<table class="comparison-table">
<tr>
    <th style="width:15%">对象</th>
    <th style="width:25%">情境</th>
    <th style="width:40%">分析</th>
    <th style="width:20%">结论</th>
</tr>
<tr>
    <td rowspan="2"><strong>地球</strong></td>
    <td>研究公转轨道</td>
    <td>地球直径 1.3×10⁴ km，远小于公转半径 1.5×10⁸ km</td>
    <td><span class="tag-yes">可视为质点</span></td>
</tr>
<tr>
    <td>研究自转现象</td>
    <td>赤道与两极运动状态不同，形状不可忽略</td>
    <td><span class="tag-no">不可视为质点</span></td>
</tr>
<tr>
    <td rowspan="2"><strong>列车</strong></td>
    <td>计算京沪运行时间</td>
    <td>车长 400m，远小于总里程 1300km</td>
    <td><span class="tag-yes">可视为质点</span></td>
</tr>
<tr>
    <td>计算过桥时间</td>
    <td>车长 200m 与桥长 800m 同数量级</td>
    <td><span class="tag-no">不可视为质点</span></td>
</tr>
</table>
""", unsafe_allow_html=True)

# --- 2. 参考系 ---
st.markdown("## 参考系")

st.markdown("""
描述运动必须指明**相对于什么**。被选作参照标准的物体称为参考系。

- 同一运动，选取不同参考系，描述结果不同（运动的相对性）
- 通常默认选取**地面**作为参考系
- 建立坐标系后，可用坐标定量描述位置
""")

# --- 3. 位移与路程 ---
st.markdown("## 位移与路程")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
| 物理量 | 位移 | 路程 |
|:---|:---|:---|
| 定义 | 初位置→末位置的有向线段 | 运动轨迹的总长度 |
| 类型 | 矢量（有方向） | 标量（无方向） |
| 符号 | Δx 或 s⃗ | s |
    """)
    
    st.markdown("""
<p class="secondary" style="margin-top: 1rem;">
仅在<strong>单向直线运动</strong>中，位移大小等于路程。
</p>
""", unsafe_allow_html=True)

with col2:
    # 简洁的示意图
    fig = go.Figure()
    
    # 曲线轨迹（路程）
    fig.add_trace(go.Scatter(
        x=[0, 1, 2, 3, 4], 
        y=[0, 1.5, 0.8, 2, 0],
        mode='lines',
        line=dict(color='#9E9E9E', width=2, dash='dot'),
        name='路程（轨迹）'
    ))
    
    # 位移（直线）
    fig.add_trace(go.Scatter(
        x=[0, 4], 
        y=[0, 0],
        mode='lines+markers',
        line=dict(color='#C87455', width=2),
        marker=dict(size=8),
        name='位移'
    ))
    
    fig.update_layout(
        height=220,
        margin=dict(l=0, r=0, t=30, b=0),
        template="plotly_white",
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0,
            font=dict(size=11)
        ),
        xaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False
        ),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    st.plotly_chart(fig, use_container_width=True)

# --- 4. 速度 ---
st.markdown("## 速度")

st.markdown("""
<div class="definition">
<strong>速度</strong>：位移与时间的比值，描述物体运动的快慢和方向。<br>
<div class="formula">v = Δx / Δt</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
| 概念 | 定义 | 说明 |
|:---|:---|:---|
| 平均速度 | 总位移 / 总时间 | 粗略描述一段过程 |
| 瞬时速度 | Δt→0 时的速度 | 精确描述某一时刻 |
| 速率 | 速度的大小 | 标量，无方向 |
""")

# --- 5. 加速度 ---
st.markdown("## 加速度")

st.markdown("""
<div class="definition">
<strong>加速度</strong>：速度变化量与时间的比值，描述速度变化的快慢。<br>
<div class="formula">a = Δv / Δt = (v - v₀) / t</div>
</div>
""", unsafe_allow_html=True)

st.markdown("### 概念辨析")
st.markdown("速度大、速度变化大、加速度大，是三个独立的概念：")

st.markdown("""
<div class="concept-row">
    <div class="concept-item">
        <div class="concept-label">速度 v</div>
        <div class="concept-value">运动快慢</div>
        <div class="concept-desc">高速飞行的子弹：v 大，但可能 a = 0</div>
    </div>
    <div class="concept-item">
        <div class="concept-label">速度变化量 Δv</div>
        <div class="concept-value">速度改变了多少</div>
        <div class="concept-desc">汽车 0→100 km/h：Δv 大，但过程可能很慢</div>
    </div>
    <div class="concept-item">
        <div class="concept-label">加速度 a</div>
        <div class="concept-value">速度变化快慢</div>
        <div class="concept-desc">枪膛击发：极短时间内速度剧变，a 极大</div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<p class="secondary" style="margin-top: 1.5rem;">
加速度的方向与速度变化量 Δv 方向一致。当 a 与 v 同向时加速，反向时减速。
</p>
""", unsafe_allow_html=True)
