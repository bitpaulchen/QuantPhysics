"""
⚛️ QuantPhysics - 可视化工具函数
Plotly 图表模板和样式配置
"""

import plotly.graph_objects as go
import plotly.express as px
from typing import List, Tuple, Optional
import numpy as np

# ============================================
# 主题配置
# ============================================

DARK_THEME = {
    "paper_bgcolor": "rgba(0,0,0,0)",
    "plot_bgcolor": "rgba(30, 41, 59, 0.5)",
    "font_color": "#f1f5f9",
    "grid_color": "rgba(148, 163, 184, 0.1)",
    "primary_color": "#0ea5e9",
    "secondary_color": "#06b6d4",
    "accent_color": "#f59e0b",
    "success_color": "#10b981",
    "danger_color": "#ef4444",
}


def apply_dark_theme(fig: go.Figure) -> go.Figure:
    """
    应用暗色主题到 Plotly 图表
    """
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor=DARK_THEME["paper_bgcolor"],
        plot_bgcolor=DARK_THEME["plot_bgcolor"],
        font=dict(color=DARK_THEME["font_color"]),
    )
    
    fig.update_xaxes(gridcolor=DARK_THEME["grid_color"])
    fig.update_yaxes(gridcolor=DARK_THEME["grid_color"])
    
    return fig


# ============================================
# 预设图表
# ============================================

def create_trajectory_plot(
    x: np.ndarray,
    y: np.ndarray,
    title: str = "运动轨迹",
    x_label: str = "x (m)",
    y_label: str = "y (m)",
    show_points: bool = True,
    height: int = 500
) -> go.Figure:
    """
    创建轨迹图
    """
    fig = go.Figure()
    
    # 添加轨迹线
    fig.add_trace(go.Scatter(
        x=x, y=y,
        mode='lines',
        name='轨迹',
        line=dict(color=DARK_THEME["primary_color"], width=3),
        fill='tozeroy',
        fillcolor=f'rgba(14, 165, 233, 0.1)'
    ))
    
    # 添加起点和终点
    if len(x) > 0:
        fig.add_trace(go.Scatter(
            x=[x[0]], y=[y[0]],
            mode='markers',
            name='起点',
            marker=dict(color=DARK_THEME["success_color"], size=12, symbol='circle')
        ))
        
        fig.add_trace(go.Scatter(
            x=[x[-1]], y=[y[-1]],
            mode='markers',
            name='终点',
            marker=dict(color=DARK_THEME["danger_color"], size=12, symbol='x')
        ))
    
    fig.update_layout(
        title=title,
        xaxis_title=x_label,
        yaxis_title=y_label,
        height=height,
        showlegend=True,
        legend=dict(yanchor="top", y=0.99, xanchor="right", x=0.99)
    )
    
    return apply_dark_theme(fig)


def create_vector_field(
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    vector_func,
    density: int = 15,
    title: str = "向量场",
    height: int = 500
) -> go.Figure:
    """
    创建向量场图 (如电场线、磁场线)
    
    Args:
        x_range: x轴范围 (min, max)
        y_range: y轴范围 (min, max)
        vector_func: 函数 (x, y) -> (vx, vy)
        density: 箭头密度
    """
    x = np.linspace(x_range[0], x_range[1], density)
    y = np.linspace(y_range[0], y_range[1], density)
    X, Y = np.meshgrid(x, y)
    
    U = np.zeros_like(X)
    V = np.zeros_like(Y)
    
    for i in range(density):
        for j in range(density):
            vx, vy = vector_func(X[i, j], Y[i, j])
            U[i, j] = vx
            V[i, j] = vy
    
    fig = go.Figure(data=go.Cone(
        x=X.flatten(),
        y=Y.flatten(),
        z=np.zeros_like(X.flatten()),
        u=U.flatten(),
        v=V.flatten(),
        w=np.zeros_like(U.flatten()),
        colorscale='Blues',
        sizemode="absolute",
        sizeref=0.5
    ))
    
    fig.update_layout(
        title=title,
        height=height,
        scene=dict(
            xaxis_title="x",
            yaxis_title="y",
            zaxis=dict(visible=False)
        )
    )
    
    return apply_dark_theme(fig)


def create_phase_diagram(
    positions: np.ndarray,
    velocities: np.ndarray,
    title: str = "相空间图",
    height: int = 500
) -> go.Figure:
    """
    创建相空间图 (位置-速度)
    """
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=positions,
        y=velocities,
        mode='lines',
        line=dict(color=DARK_THEME["secondary_color"], width=2),
        name='相轨迹'
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title="位置 x",
        yaxis_title="速度 v",
        height=height
    )
    
    return apply_dark_theme(fig)


def create_energy_bar_chart(
    labels: List[str],
    values: List[float],
    colors: Optional[List[str]] = None,
    title: str = "能量分布",
    height: int = 400
) -> go.Figure:
    """
    创建能量条形图
    """
    if colors is None:
        colors = [DARK_THEME["primary_color"]] * len(labels)
    
    fig = go.Figure(data=[
        go.Bar(
            x=labels,
            y=values,
            marker_color=colors,
            text=[f'{v:.2f} J' for v in values],
            textposition='auto'
        )
    ])
    
    fig.update_layout(
        title=title,
        xaxis_title="能量类型",
        yaxis_title="能量 (J)",
        height=height
    )
    
    return apply_dark_theme(fig)


def create_motion_animation(
    x_data: List[np.ndarray],
    y_data: List[np.ndarray],
    frame_duration: int = 50,
    title: str = "运动动画"
) -> go.Figure:
    """
    创建运动动画
    
    Args:
        x_data: 每帧的x坐标列表
        y_data: 每帧的y坐标列表
        frame_duration: 每帧持续时间 (ms)
    """
    fig = go.Figure(
        data=[go.Scatter(x=[x_data[0][0]], y=[y_data[0][0]], 
                        mode='markers', marker=dict(size=15, color=DARK_THEME["accent_color"]))],
        layout=go.Layout(
            title=title,
            updatemenus=[dict(
                type="buttons",
                buttons=[dict(label="播放",
                            method="animate",
                            args=[None, {"frame": {"duration": frame_duration, "redraw": True},
                                        "fromcurrent": True}])]
            )]
        ),
        frames=[go.Frame(data=[go.Scatter(x=[x_data[i][0]], y=[y_data[i][0]])])
                for i in range(len(x_data))]
    )
    
    return apply_dark_theme(fig)

