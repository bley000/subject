import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, lambdify

# 定義未知數
beta_b_hat, alpha_b_hat, alpha_a_hat, beta_a_hat, g_a, c, lambda_2, g_b = symbols('beta_b_hat alpha_b_hat alpha_a_hat beta_a_hat g_a c lambda_2 g_b')

# 固定五個變數的值
fixed_values = {
    'beta_b_hat': 0.8,
    'alpha_b_hat': 1,
    'alpha_a_hat': 1,
    'beta_a_hat': 1,
    'c': 0.5,
    'lambda_2': 0.6,
    'g_b': 0.5
}

# 剩下三個變數作為繪圖變數
x_var, y_var, z_var = g_a, beta_b_hat, alpha_b_hat

# 定義方程（簡化自隱形條件.py）
equation = (
    (2 / (1 + beta_b_hat * (alpha_b_hat - 1))) *
    (
        (-1 + 1 + beta_b_hat * (alpha_b_hat - 1)) /
        (1 + beta_b_hat * (alpha_b_hat + 1) - (1 + beta_b_hat * (alpha_b_hat - 1))) +
        ((1 + alpha_a_hat) - (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a) /
        ((1 + beta_b_hat * (alpha_b_hat + 1)) * ((1 + alpha_a_hat) + (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a) -
         c**lambda_2 * ((1 + alpha_a_hat) - (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a) * (1 + beta_b_hat * (alpha_b_hat - 1)))
    )
)

# 替換固定值
for var, value in fixed_values.items():
    equation = equation.subs(symbols(var), value)

# 將方程轉換為數值函數
f = lambdify((x_var, y_var, z_var), equation, 'numpy')

# 創建 x, y 的範圍
x = np.linspace(0.1, 1, 50)  # g_a 的範圍
y = np.linspace(0.1, 1, 50)  # beta_b_hat 的範圍
x, y = np.meshgrid(x, y)

# 計算 z 的值
z = f(x, y, 1)  # alpha_b_hat 固定為 1

# 繪製 3D 圖
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)
ax.set_xlabel('g_a')
ax.set_ylabel('beta_b_hat')
ax.set_zlabel('Equation Value')
plt.title("3D Plot of the Equation")
plt.show()