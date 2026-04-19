"""
文件名：v1-probability (概率与确定性的 5 维转换)
注解：
本代码用于演示 Twin-G 框架下的“维度塌缩”。
在 5 维中，位置受 1/dist^5 屏障严格锁定，路径是唯一的；
本脚本通过投影模拟，让观察者看到“概率分布”的诞生。
"""
import numpy as np

def run_probability_demo():
    print("--- Twin-G 实验：高维确定性投影模拟 ---")
    
    # 核心常数：相位步长 0.3065
    PHASE_STEP = 0.3065
    
    # 1. 模拟 5 维中的确定性路径 (Deterministic Path)
    # 粒子在 5 维流形中受力平衡，轨迹极其丝滑且固定
    t = np.linspace(0, 10, 1000)
    five_d_core = np.cos(t / PHASE_STEP)
    
    # 2. 模拟 3 维空间的观测投影
    # 当丢失了 r 轴（本征距离 1.37）的约束信息后，投影点开始出现偏差
    projection_noise = np.random.normal(0, 0.15, 1000)
    observed_3d_state = five_d_core + projection_noise
    
    print(f"状态：5 维本征态已计算完成。")
    print(f"观测结论：在 3 维视角下，该粒子表现出 {np.std(observed_3d_state):.4f} 的不确定性分布。")
    print("理论注脚：在高维视角中，这种‘分布’其实是完美的直线/圆周。")

if __name__ == "__main__":
    run_probability_demo()