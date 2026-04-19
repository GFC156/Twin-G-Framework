"""
文件名：v1_probability.py (初版 - 几何决定论实证)
实验内容：
1. 5D 本征态模拟：受 Twin-G 屏障力锁定的确定性轨道。
2. 3D 观测投影：模拟因维度缺失产生的“概率红云”。
3. 统计真理回归：证明概率分布是由几何路径（正弦波时间权重）精准决定的。
"""
import numpy as np
import matplotlib.pyplot as plt

def run_probability_truth_experiment():
    print("--- Twin-G 实验：几何路径统治下的统计真理 ---")
    
    # 模拟参数
    samples = 20000 
    t = np.linspace(0, 10, samples)
    # 设定极高频本征振荡，模拟微观锁定态
    PHASE_FREQ = 0.05  
    five_d_truth = np.cos(t / PHASE_FREQ) 
    
    # 3D 观测投影（叠加极小观测噪声）
    noise_sigma = 0.2
    observed = five_d_truth + np.random.normal(0, noise_sigma, samples)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # --- 1. 时域视图 (Micro-Path View) ---
    ax1.scatter(t[:500], observed[:500], s=2, color='red', alpha=0.3, label='3D Observation (Cloud)')
    ax1.plot(t[:500], five_d_truth[:500], color='blue', lw=2, label='5D Path (True Reality)')
    ax1.set_title("1. Temporal View: From Path to Cloud")
    ax1.set_xlabel("Time / Phase")
    ax1.set_ylabel("State Value")
    ax1.legend()

    # --- 2. 统计视图 (Geometric Origin of Probability) ---
    # 绘制灰色直方图展现观测频次
    count, bins, ignored = ax2.hist(observed, bins=100, density=True, color='gray', alpha=0.6, label='Statistical Distribution')
    
    # 使用正弦概率密度函数 (Sine PDF) 进行几何拟合
    # 公式：f(x) = 1 / (pi * sqrt(1 - x^2))
    x_range = np.linspace(-0.999, 0.999, 500)
    sine_pdf = 1 / (np.pi * np.sqrt(1 - x_range**2))
    
    ax2.plot(x_range, sine_pdf, 'b--', lw=2, label='Geometric Determinism (Sine PDF)')
    
    ax2.set_ylim(0, 1.5)
    ax2.set_title("2. Statistical View: Emergence of Probability")
    ax2.set_xlabel("Observed Value")
    ax2.set_ylabel("Probability Density")
    ax2.legend()

    plt.tight_layout()
    print("实验图像已生成。")
    plt.show()

if __name__ == "__main__":
    run_probability_truth_experiment()