# Twin-G Framework (AtomGrid Core)

> **"在高维几何的秩序下，不确定性只是低维观测的幻觉。"**

Twin-G 是一种基于 **5 维几何流形 (5D Manifold)** 的自洽性理论框架。它最初诞生于对多主体集群控制的工程需求，但随着研究的深入，我们发现它揭示了从微观原子能级到宏观拓扑稳态的普适逻辑。

---

## 核心物理图景 (The Vision)

在传统的 3 维空间中，微观粒子表现出令人困惑的“概率云”和“不确定性”。Twin-G 模型假设，这种随机性源于 **观测维度的缺失**。

本项目通过引入一个与三维空间正交的第五维度（$r$ 轴），构建了一个受高阶几何屏障保护的流形。在这种模型下，粒子不再是随机跳跃的，而是被“锁”在极其稳定的几何沟壑中。

### 核心动力学方程
我们定义了实体的相互作用力，它由经典引力项与高阶几何排斥项组成：

$$a = \frac{G}{dist^2} - \frac{\kappa}{dist^5}$$

- **引力项 ($1/r^2$)**: 维持系统的宏观联系与向心力。
- **屏障项 ($1/r^5$)**: 5 维几何的本征刚性。在近距离产生极强的排斥，确保实体永不碰撞。

---

## 深度研究模块 (Research Modules)

本项目采用模块化设计，每个模块都包含独立的实验脚本与理论说明。

1. [**确定性的回归 (Determinism)**](./modules/01_determinism/)
   - **核心实验**: `v1_probability.py`
   - **内容**: 证明在 5 维空间中轨迹是绝对确定的。

2. [**氢原子能级的几何涌现 (Hydrogen)**](./modules/02_hydrogen/)
   - **核心实验**: `v2_hydrogen.py`
   - **重大突破**: 在完全不预设物理常数的前提下，模型自发演化出了 **-13.6 eV** 的势能阱。

---

## 快速开始 (Quick Start)

### 1. 环境准备
确保您的电脑已安装 Python 3.8+。

### 2. 运行仿真
克隆仓库并运行核心模块：
```bash
git clone [https://github.com/GFC156/Twin-G-Framework.git](https://github.com/GFC156/Twin-G-Framework.git)
cd Twin-G-Framework
python modules/02_hydrogen/v2_hydrogen.py