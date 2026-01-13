"""
⚛️ QuantPhysics - 物理计算工具函数
常用物理公式和计算函数
"""

import numpy as np
from typing import Tuple, List, Dict

# ============================================
# 运动学
# ============================================

def projectile_motion(
    v0: float, 
    theta: float, 
    g: float = 9.8, 
    h0: float = 0,
    dt: float = 0.01
) -> Tuple[np.ndarray, np.ndarray, float, float, float]:
    """
    计算抛体运动轨迹
    
    Args:
        v0: 初速度 (m/s)
        theta: 发射角度 (度)
        g: 重力加速度 (m/s²)
        h0: 初始高度 (m)
        dt: 时间步长 (s)
    
    Returns:
        x: x坐标数组
        y: y坐标数组
        t_flight: 飞行时间
        x_max: 水平射程
        h_max: 最大高度
    """
    theta_rad = np.radians(theta)
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)
    
    # 计算飞行时间 (解一元二次方程)
    # h0 + v0y*t - 0.5*g*t^2 = 0
    a = -0.5 * g
    b = v0y
    c = h0
    discriminant = b**2 - 4*a*c
    t_flight = (-b - np.sqrt(discriminant)) / (2*a)
    
    # 生成轨迹
    t = np.arange(0, t_flight, dt)
    x = v0x * t
    y = h0 + v0y * t - 0.5 * g * t**2
    
    # 计算关键参数
    x_max = v0x * t_flight
    h_max = h0 + v0y**2 / (2*g)
    
    return x, y, t_flight, x_max, h_max


def uniform_circular_motion(
    r: float,
    T: float,
    num_points: int = 100
) -> Tuple[np.ndarray, np.ndarray, float, float]:
    """
    计算匀速圆周运动参数
    
    Args:
        r: 圆周半径 (m)
        T: 周期 (s)
        num_points: 轨迹点数
    
    Returns:
        x: x坐标数组
        y: y坐标数组
        omega: 角速度 (rad/s)
        a_c: 向心加速度 (m/s²)
    """
    omega = 2 * np.pi / T
    v = omega * r
    a_c = v**2 / r  # 或 omega**2 * r
    
    theta = np.linspace(0, 2 * np.pi, num_points)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    return x, y, omega, a_c


def charged_particle_in_magnetic_field(
    q: float,
    m: float,
    v: float,
    B: float
) -> Dict[str, float]:
    """
    计算带电粒子在匀强磁场中的运动参数
    
    Args:
        q: 电荷量 (C)
        m: 质量 (kg)
        v: 速度 (m/s)
        B: 磁感应强度 (T)
    
    Returns:
        包含回旋半径、周期、角速度的字典
    """
    r = m * v / (q * B)
    T = 2 * np.pi * m / (q * B)
    omega = q * B / m
    
    return {
        "radius": r,
        "period": T,
        "omega": omega,
        "lorentz_force": q * v * B
    }


# ============================================
# 碰撞与动量
# ============================================

def elastic_collision_1d(
    m1: float, v1: float,
    m2: float, v2: float
) -> Tuple[float, float]:
    """
    一维完全弹性碰撞
    
    Args:
        m1, v1: 物体1的质量和速度
        m2, v2: 物体2的质量和速度
    
    Returns:
        碰撞后两物体的速度 (v1', v2')
    """
    v1_new = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2_new = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)
    return v1_new, v2_new


def inelastic_collision_1d(
    m1: float, v1: float,
    m2: float, v2: float,
    e: float = 0  # 恢复系数，0为完全非弹性
) -> Tuple[float, float]:
    """
    一维非弹性碰撞
    
    Args:
        m1, v1: 物体1的质量和速度
        m2, v2: 物体2的质量和速度
        e: 恢复系数 (0-1)
    
    Returns:
        碰撞后两物体的速度
    """
    # 动量守恒: m1*v1 + m2*v2 = m1*v1' + m2*v2'
    # 恢复系数: e = (v2' - v1') / (v1 - v2)
    
    v1_new = (m1 * v1 + m2 * v2 + m2 * e * (v2 - v1)) / (m1 + m2)
    v2_new = (m1 * v1 + m2 * v2 + m1 * e * (v1 - v2)) / (m1 + m2)
    
    return v1_new, v2_new


def momentum(m: float, v: float) -> float:
    """计算动量 p = mv"""
    return m * v


def kinetic_energy(m: float, v: float) -> float:
    """计算动能 E = 0.5*m*v²"""
    return 0.5 * m * v**2


# ============================================
# 力学分析
# ============================================

def resolve_force(
    F: float, 
    theta: float
) -> Tuple[float, float]:
    """
    力的分解 (正交分解)
    
    Args:
        F: 力的大小 (N)
        theta: 与x轴的夹角 (度)
    
    Returns:
        (Fx, Fy): 分力
    """
    theta_rad = np.radians(theta)
    Fx = F * np.cos(theta_rad)
    Fy = F * np.sin(theta_rad)
    return Fx, Fy


def compose_forces(forces: List[Tuple[float, float]]) -> Tuple[float, float]:
    """
    力的合成
    
    Args:
        forces: 力的列表，每个元素为 (F, theta)
    
    Returns:
        (F_total, theta_total): 合力大小和方向
    """
    Fx_total = sum(F * np.cos(np.radians(theta)) for F, theta in forces)
    Fy_total = sum(F * np.sin(np.radians(theta)) for F, theta in forces)
    
    F_total = np.sqrt(Fx_total**2 + Fy_total**2)
    theta_total = np.degrees(np.arctan2(Fy_total, Fx_total))
    
    return F_total, theta_total


def friction_force(
    mu: float,
    N: float,
    kinetic: bool = True
) -> float:
    """
    计算摩擦力
    
    Args:
        mu: 摩擦系数
        N: 正压力 (N)
        kinetic: True为动摩擦力，False为最大静摩擦力
    
    Returns:
        摩擦力大小 (N)
    """
    return mu * N


# ============================================
# 电磁学
# ============================================

def coulomb_force(
    q1: float,
    q2: float,
    r: float,
    k: float = 8.99e9
) -> float:
    """
    库仑定律计算电场力
    
    Args:
        q1, q2: 电荷量 (C)
        r: 距离 (m)
        k: 库仑常数
    
    Returns:
        电场力大小 (N)
    """
    return k * abs(q1 * q2) / r**2


def electric_field(
    q: float,
    r: float,
    k: float = 8.99e9
) -> float:
    """
    点电荷电场强度
    
    Args:
        q: 电荷量 (C)
        r: 距离 (m)
        k: 库仑常数
    
    Returns:
        电场强度 (N/C 或 V/m)
    """
    return k * abs(q) / r**2


def lorentz_force(
    q: float,
    v: float,
    B: float,
    theta: float = 90
) -> float:
    """
    洛伦兹力
    
    Args:
        q: 电荷量 (C)
        v: 速度 (m/s)
        B: 磁感应强度 (T)
        theta: v与B的夹角 (度)
    
    Returns:
        洛伦兹力大小 (N)
    """
    return abs(q) * v * B * np.sin(np.radians(theta))

