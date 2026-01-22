import streamlit as st

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