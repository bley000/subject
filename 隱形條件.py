from sympy import symbols, Eq, nsolve, Float

# 定義未知數
beta_b_hat, alpha_b_hat, alpha_a_hat, beta_a_hat, g_a, c, lambda_2, g_b = symbols('beta_b_hat alpha_b_hat alpha_a_hat beta_a_hat g_a c lambda_2 g_b')

# 讓使用者輸入八個數字，使用 None 表示缺失的數字
input_values = {
    'beta_b_hat': None,
    'alpha_b_hat': 1,
    'alpha_a_hat': 1,
    'beta_a_hat': 1,
    'g_a': 0.3,  # 假設 g_a 是缺失的數字
    'c': 0.5,
    'lambda_2': 0.6,
    'g_b': 0.5  # 給定 g_b 的具體數值
}

# 找出缺失的數字
missing_variable = None
given_values = {}
for key, value in input_values.items():
    if value is None:
        missing_variable = key
    else:
        given_values[symbols(key)] = value

# 構建方程
equation = Eq(
    (2 / (1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) - 1))) * (
        (-1 + 1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) - 1)) / 
        (1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) + 1) - (1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) - 1))) + 
        ((1 + given_values.get(alpha_a_hat, alpha_a_hat)) - (1 + given_values.get(beta_a_hat, beta_a_hat) * (1 + given_values.get(alpha_a_hat, alpha_a_hat))) * given_values.get(g_a, g_a)) / 
        ((1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) + 1)) * ((1 + given_values.get(alpha_a_hat, alpha_a_hat)) + (1 + given_values.get(beta_a_hat, beta_a_hat) * (1 + given_values.get(alpha_a_hat, alpha_a_hat))) * given_values.get(g_a, g_a)) - 
         given_values.get(c, c)**given_values.get(lambda_2, lambda_2) * ((1 + given_values.get(alpha_a_hat, alpha_a_hat)) - (1 + given_values.get(beta_a_hat, beta_a_hat) * (1 + given_values.get(alpha_a_hat, alpha_a_hat))) * given_values.get(g_a, g_a)) * (1 + given_values.get(beta_b_hat, beta_b_hat) * (given_values.get(alpha_b_hat, alpha_b_hat) - 1)))
    ),
    symbols(missing_variable)
)

# 使用數值方法求解方程
initial_guess = 1.0  # 初始猜測值，可以根據實際情況調整
solution = nsolve(equation, symbols(missing_variable), Float(initial_guess))
print(f"The missing variable {missing_variable} is: {solution}")