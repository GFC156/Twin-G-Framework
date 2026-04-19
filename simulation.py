import numpy as np

class TwinGSimulator:
    def __init__(self, G=1.0, kappa=0.25):
        self.G = G
        self.kappa = kappa # 5维几何刚性系数

    def compute_accel(self, pos):
        n = len(pos)
        accel = np.zeros_like(pos)
        for i in range(n):
            for j in range(n):
                if i == j: continue
                diff = pos[j] - pos[i]
                dist = np.linalg.norm(diff)
                
                # Twin-G 核心方程实现
                if dist > 0.01:
                    mag = (self.G / dist**2) - (self.kappa / dist**5)
                    accel[i] += mag * (diff / dist)
        return accel

# 初始稳态参数示例 (基于 0.3065 逻辑)
print("Twin-G 仿真引擎已就绪。正在加载本征常数...")