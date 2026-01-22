"""
 QuantPhysics - Streamlit 组件工具
可复用的 UI 组件
"""

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from typing import Optional


# 交互函数 ：选择题
def render_choice_question(question_data, question_key):
    """
    渲染高度整合的选择题组件
    """
    # 1. 显示题干
    title = question_data.get("title", "")
    content = question_data.get("question", "")
    st.markdown(f"**{title}** {content}")
    
    # 2. 准备选项数据
    opts_dict = question_data["options"]
    keys = list(opts_dict.keys()) # ['A', 'B', 'C', 'D']
    
    # 3. 渲染单选框
    # format_func 负责把 Key 映射为具体显示的文本
    selected_key = st.radio(
        "请选择你的答案：",
        options=keys,
        format_func=lambda x: f"{x}: {opts_dict[x]['content']}",
        index=None,
        key=question_key
    )
    
    # 4. 判定与反馈逻辑
    if selected_key:
        result = opts_dict[selected_key]
        is_correct = result.get("is_correct", False)
        feedback = result.get("feedback", "")
        
        if is_correct:
            st.success(feedback)
            # st.balloons() # 增加互动感
        else:
            st.error("再想想看？")
            with st.expander("查看当前选项解析"):
                st.markdown(feedback)









# ============================================
# 全局样式加载
# ============================================

# 缓存 CSS 内容，避免重复读取文件
@st.cache_resource
def _load_css() -> str:
    """加载全局 CSS 文件内容"""
    css_path = Path(__file__).parent.parent / "assets" / "styles.css"
    if css_path.exists():
        return css_path.read_text(encoding='utf-8')
    return ""


def apply_global_styles() -> None:
    """
    应用全局样式。在每个页面开头调用一次即可。
    
    Usage:
        from utils import apply_global_styles
        apply_global_styles()
    """
    css = _load_css()
    if css:
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)







# ============================================
# p5.js 嵌入组件
# ============================================

def embed_p5_sketch(
    sketch_path: str,
    width: int = 800,
    height: int = 600,
    title: str = "交互仿真"
) -> None:
    """
    嵌入 p5.js 交互草图
    
    Args:
        sketch_path: p5.js 文件路径
        width: 画布宽度
        height: 画布高度
        title: 标题
    """
    # 读取 sketch 代码
    sketch_code = Path(sketch_path).read_text(encoding='utf-8')
    
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.9.0/p5.min.js"></script>
        <style>
            body {{
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                background: transparent;
            }}
            canvas {{
                border-radius: 8px;
            }}
        </style>
    </head>
    <body>
        <script>
        {sketch_code}
        </script>
    </body>
    </html>
    """
    
    components.html(html_content, width=width, height=height)


# ============================================
# 公式卡片
# ============================================

def formula_card(
    title: str,
    formula: str,
    description: str = "",
    variables: Optional[dict] = None
) -> None:
    """
    显示公式卡片
    
    Args:
        title: 公式名称
        formula: LaTeX 公式
        description: 公式说明
        variables: 变量说明字典 {'v': '速度', 't': '时间'}
    """
    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, #1e293b, #334155);
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid #0ea5e9;
    ">
        <h4 style="color: #f1f5f9; margin-bottom: 0.5rem;">{title}</h4>
    </div>
    """, unsafe_allow_html=True)
    
    st.latex(formula)
    
    if description:
        st.markdown(f"*{description}*")
    
    if variables:
        var_text = " | ".join([f"**{k}**: {v}" for k, v in variables.items()])
        st.markdown(f"📝 {var_text}")


# ============================================
# 知识点卡片
# ============================================

def knowledge_card(
    title: str,
    content: str,
    risk_level: str = "normal",
    icon: str = "📌"
) -> None:
    """
    显示知识点卡片
    
    Args:
        title: 知识点标题
        content: 知识点内容
        risk_level: 'high', 'medium', 'normal'
        icon: 图标
    """
    colors = {
        "high": ("#ef4444", "rgba(239, 68, 68, 0.15)"),
        "medium": ("#f59e0b", "rgba(245, 158, 11, 0.15)"),
        "normal": ("#0ea5e9", "rgba(14, 165, 233, 0.15)")
    }
    
    border_color, bg_color = colors.get(risk_level, colors["normal"])
    
    risk_badge = ""
    if risk_level == "high":
        risk_badge = '<span style="background: rgba(239, 68, 68, 0.2); color: #ef4444; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; margin-left: 0.5rem;">🔥 高频考点</span>'
    elif risk_level == "medium":
        risk_badge = '<span style="background: rgba(245, 158, 11, 0.2); color: #f59e0b; padding: 0.2rem 0.6rem; border-radius: 4px; font-size: 0.75rem; margin-left: 0.5rem;">⚠️ 易错点</span>'
    
    st.markdown(f"""
    <div style="
        background: {bg_color};
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 4px solid {border_color};
    ">
        <h4 style="color: #f1f5f9; margin-bottom: 0.5rem;">
            {icon} {title} {risk_badge}
        </h4>
        <p style="color: #94a3b8; line-height: 1.6; margin: 0;">
            {content}
        </p>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# 参数面板
# ============================================

def parameter_panel(title: str = "⚙️ 参数设置"):
    """
    创建参数设置面板的上下文管理器
    """
    st.markdown(f"""
    <div style="
        background: rgba(30, 41, 59, 0.8);
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1rem;
    ">
        <h4 style="color: #f1f5f9; margin: 0;">{title}</h4>
    </div>
    """, unsafe_allow_html=True)


# ============================================
# 结果展示
# ============================================

def result_metrics(metrics: dict, columns: int = 3) -> None:
    """
    展示计算结果指标
    
    Args:
        metrics: {'名称': (值, 单位)} 或 {'名称': 值}
        columns: 列数
    """
    cols = st.columns(columns)
    
    for i, (name, value) in enumerate(metrics.items()):
        with cols[i % columns]:
            if isinstance(value, tuple):
                st.metric(name, f"{value[0]:.2f} {value[1]}")
            else:
                st.metric(name, f"{value:.2f}")


# ============================================
# 提示框
# ============================================

def tip_box(content: str, tip_type: str = "info") -> None:
    """
    显示提示框
    
    Args:
        content: 提示内容
        tip_type: 'info', 'warning', 'success', 'error'
    """
    icons = {
        "info": "💡",
        "warning": "⚠️",
        "success": "✅",
        "error": "❌"
    }
    
    colors = {
        "info": "#0ea5e9",
        "warning": "#f59e0b",
        "success": "#10b981",
        "error": "#ef4444"
    }
    
    icon = icons.get(tip_type, icons["info"])
    color = colors.get(tip_type, colors["info"])
    
    st.markdown(f"""
    <div style="
        background: rgba({int(color[1:3], 16)}, {int(color[3:5], 16)}, {int(color[5:7], 16)}, 0.1);
        border-left: 4px solid {color};
        border-radius: 4px;
        padding: 1rem;
        margin: 1rem 0;
    ">
        <span style="color: {color}; font-weight: 500;">{icon} </span>
        <span style="color: #94a3b8;">{content}</span>
    </div>
    """, unsafe_allow_html=True)

