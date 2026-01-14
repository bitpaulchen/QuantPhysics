import streamlit as st

# ============================================
# 欢迎页 - 主页
# ============================================

st.markdown("""
<style>
    .hero-section {
        text-align: center;
        padding: 3rem 2rem;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        color: #3F3F3A;
        margin-bottom: 0.5rem;
        letter-spacing: -0.02em;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
        color: #6F6F6B;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    .hero-description {
        font-size: 1rem;
        color: #6F6F6B;
        max-width: 600px;
        margin: 0 auto 2rem auto;
        line-height: 1.7;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    @media (max-width: 768px) {
        .feature-grid {
            grid-template-columns: 1fr;
        }
    }
    
    .feature-card {
        background: #F1F1EC;
        border: 1px solid #D6D6D0;
        border-radius: 12px;
        padding: 1.5rem;
        text-align: left;
        transition: all 0.2s ease;
    }
    
    .feature-card:hover {
        border-color: #C87455;
        box-shadow: 0 4px 12px rgba(200, 116, 85, 0.1);
    }
    
    .feature-icon {
        width: 40px;
        height: 40px;
        background: #E9E9E5;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
        color: #C87455;
    }
    
    .feature-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #3F3F3A;
        margin-bottom: 0.5rem;
    }
    
    .feature-desc {
        font-size: 0.9rem;
        color: #6F6F6B;
        line-height: 1.5;
    }
    
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #3F3F3A;
        margin: 3rem 0 1.5rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 2px solid #D6D6D0;
    }
    
    .chapter-list {
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 1rem;
        margin: 1.5rem 0;
    }
    
    @media (max-width: 1024px) {
        .chapter-list {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    
    @media (max-width: 640px) {
        .chapter-list {
            grid-template-columns: 1fr;
        }
    }
    
    .chapter-item {
        background: #F1F1EC;
        border: 1px solid #D6D6D0;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        color: #3F3F3A;
        font-size: 0.95rem;
        font-weight: 500;
        transition: all 0.15s ease;
    }
    
    .chapter-item:hover {
        background: #EDEDEA;
        border-color: #C87455;
    }
    
    .chapter-number {
        color: #C87455;
        font-weight: 600;
        margin-right: 0.5rem;
    }
    
    .footer {
        text-align: center;
        padding: 3rem 0;
        margin-top: 3rem;
        border-top: 1px solid #D6D6D0;
        color: #6F6F6B;
        font-size: 0.875rem;
    }
    
    .stats-row {
        display: flex;
        justify-content: center;
        gap: 4rem;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #C87455;
        line-height: 1;
    }
    
    .stat-label {
        font-size: 0.875rem;
        color: #6F6F6B;
        margin-top: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# Hero 区域
# ============================================
st.markdown("""
<div class="hero-section">
    <div class="hero-title">QuantPhysics</div>
    <div class="hero-subtitle">高中物理可视化学习平台</div>
    <div class="hero-description">
        通过交互式仿真与可视化工具，深入理解物理概念与规律。
        从力学到电磁学，从光学到原子物理，系统化覆盖高中物理全部知识点。
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# 统计数据
# ============================================
st.markdown("""
<div class="stats-row">
    <div class="stat-item">
        <div class="stat-number">16</div>
        <div class="stat-label">章节模块</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">50+</div>
        <div class="stat-label">交互仿真</div>
    </div>
    <div class="stat-item">
        <div class="stat-number">100+</div>
        <div class="stat-label">核心公式</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# 特性介绍
# ============================================
st.markdown("""
<div class="feature-grid">
    <div class="feature-card">
        <div class="feature-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
            </svg>
        </div>
        <div class="feature-title">交互式仿真</div>
        <div class="feature-desc">通过可调参数的动态仿真，直观感受物理规律的作用过程</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/>
            </svg>
        </div>
        <div class="feature-title">数据可视化</div>
        <div class="feature-desc">实时图表展示物理量变化关系，建立定量分析思维</div>
    </div>
    <div class="feature-card">
        <div class="feature-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
            </svg>
        </div>
        <div class="feature-title">系统化知识</div>
        <div class="feature-desc">按教材章节组织，涵盖力学、电磁学、光学、热学等全部内容</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# 章节导航
# ============================================
st.markdown('<div class="section-title">力学</div>', unsafe_allow_html=True)
st.markdown("""
<div class="chapter-list">
    <div class="chapter-item"><span class="chapter-number">01</span>直线运动</div>
    <div class="chapter-item"><span class="chapter-number">02</span>相互作用</div>
    <div class="chapter-item"><span class="chapter-number">03</span>牛顿运动定律</div>
    <div class="chapter-item"><span class="chapter-number">04</span>曲线运动</div>
    <div class="chapter-item"><span class="chapter-number">05</span>万有引力</div>
    <div class="chapter-item"><span class="chapter-number">06</span>机械能守恒定律</div>
    <div class="chapter-item"><span class="chapter-number">07</span>动量</div>
    <div class="chapter-item"><span class="chapter-number">08</span>机械振动</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">电磁学</div>', unsafe_allow_html=True)
st.markdown("""
<div class="chapter-list">
    <div class="chapter-item"><span class="chapter-number">09</span>电场</div>
    <div class="chapter-item"><span class="chapter-number">10</span>电流</div>
    <div class="chapter-item"><span class="chapter-number">11</span>磁场</div>
    <div class="chapter-item"><span class="chapter-number">12</span>电磁感应</div>
    <div class="chapter-item"><span class="chapter-number">13</span>交流电</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-title">其他</div>', unsafe_allow_html=True)
st.markdown("""
<div class="chapter-list">
    <div class="chapter-item"><span class="chapter-number">14</span>光学</div>
    <div class="chapter-item"><span class="chapter-number">15</span>热学</div>
    <div class="chapter-item"><span class="chapter-number">16</span>原子物理</div>
</div>
""", unsafe_allow_html=True)

# ============================================
# 页脚
# ============================================
st.markdown("""
<div class="footer">
    <div>QuantPhysics - 高中物理可视化学习平台</div>
    <div style="margin-top: 0.5rem;">使用 Streamlit 构建</div>
</div>
""", unsafe_allow_html=True)
