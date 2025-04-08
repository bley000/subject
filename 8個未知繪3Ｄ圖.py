import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, lambdify

# 定義符號
alpha_a_hat, beta_a_hat, g_a = symbols('alpha_a_hat beta_a_hat g_a')
alpha_b_hat, beta_b_hat, c, lambda_2 = symbols('alpha_b_hat beta_b_hat c lambda_2')

# 定義方程式
numerator = (1 + alpha_b_hat) * ((1 + alpha_a_hat) + (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a) - \
            c**lambda_2 * (-1 + alpha_b_hat) * ((1 + alpha_a_hat) - (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a)
denominator = (1 + beta_b_hat * (1 + alpha_b_hat)) * ((1 + alpha_a_hat) + (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a) - \
              c**lambda_2 * (1 + beta_b_hat * (1 + alpha_b_hat)) * ((1 + alpha_a_hat) - (1 + beta_a_hat * (1 + alpha_a_hat)) * g_a)
g_b_expr = numerator / denominator

# 固定參數
fixed_params = {
    'alpha_b_hat': 1.0,
    'beta_b_hat': 0.8,
    'c': 0.5,
    'lambda_2': 0.6,
}

# 自由變數
free_vars = ('alpha_a_hat', 'beta_a_hat', 'g_a')
var_ranges = {
    'alpha_a_hat': (0, 5),
    'beta_a_hat': (0, 5),
    'g_a': (-10, 10),
}

# g_b 變化值
g_b_values = [0.1, 1, 10]
colors = ['r', 'g', 'b']

# 數值化函數
g_b_func = lambdify((alpha_a_hat, beta_a_hat, g_a,
                     alpha_b_hat, beta_b_hat, c, lambda_2), g_b_expr, modules='numpy')

# 建立網格
x_vals = np.linspace(*var_ranges['alpha_a_hat'], 100)
y_vals = np.linspace(*var_ranges['beta_a_hat'], 100)
z_range = np.linspace(*var_ranges['g_a'], 300)
X, Y = np.meshgrid(x_vals, y_vals)

def compute_surface(x, y, g_b_target, z_range, g_b_func, fixed_params):
    surface = np.zeros_like(x)
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            g_b_vals = g_b_func(
                x[i, j], y[i, j], z_range,
                fixed_params['alpha_b_hat'], fixed_params['beta_b_hat'],
                fixed_params['c'], fixed_params['lambda_2']
            )
            idx = np.argmin(np.abs(g_b_vals - g_b_target))
            surface[i, j] = z_range[idx]
    return surface

# 繪製 3D 圖
fig = plt.figure(figsize=(6, 4))
ax = fig.add_subplot(111, projection='3d')
for g_b_val, color in zip(g_b_values, colors):
    Z = compute_surface(X, Y, g_b_val, z_range, g_b_func, fixed_params)
    ax.plot_surface(X, Y, Z, color=color, alpha=0.6, label=f'g_b = {g_b_val}')
ax.set_xlabel('alpha_a_hat')
ax.set_ylabel('beta_a_hat')
ax.set_zlabel('g_a')
plt.title("3D Surfaces for Different g_b Values")
plt.legend()
plt.show()

# 繪製 x-z 圖：固定 beta_a_hat = 0
fixed_beta = 0.0
plt.figure(figsize=(5, 4))
for g_b_val, color in zip(g_b_values, colors):
    z_values = []
    for x in x_vals:
        g_b_vals = g_b_func(
            x, fixed_beta, z_range,
            fixed_params['alpha_b_hat'], fixed_params['beta_b_hat'],
            fixed_params['c'], fixed_params['lambda_2']
        )
        idx = np.argmin(np.abs(g_b_vals - g_b_val))
        z_values.append(z_range[idx])
    plt.plot(x_vals, z_values, color=color, label=f'g_b = {g_b_val}')
plt.xlabel('alpha_a_hat')
plt.ylabel('g_a')
plt.title(f'x-z Curve (beta_a_hat={fixed_beta})')
plt.legend()
plt.grid(True)
plt.show()

# 繪製 y-z 圖：固定 alpha_a_hat = 0
fixed_alpha = 0.0
plt.figure(figsize=(5, 4))
for g_b_val, color in zip(g_b_values, colors):
    z_values = []
    for y in y_vals:
        g_b_vals = g_b_func(
            fixed_alpha, y, z_range,
            fixed_params['alpha_b_hat'], fixed_params['beta_b_hat'],
            fixed_params['c'], fixed_params['lambda_2']
        )
        idx = np.argmin(np.abs(g_b_vals - g_b_val))
        z_values.append(z_range[idx])
    plt.plot(y_vals, z_values, color=color, label=f'g_b = {g_b_val}')
plt.xlabel('beta_a_hat')
plt.ylabel('g_a')
plt.title(f'y-z Curve (alpha_a_hat={fixed_alpha})')
plt.legend()
plt.grid(True)
plt.show()
