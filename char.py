import numpy as np

np.set_printoptions(suppress=True)  # 抑制科学计数法，让输出更直观

# 1. 定义矩阵
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

print("矩阵 A（形状：{}）：\n".format(A.shape), A)
print("矩阵 B（形状：{}）：\n".format(B.shape), B)
print("-" * 60)  # 加长分隔线，视觉效果更好

# 2. 矩阵基本运算
print("A + A（矩阵加法，形状不变）：\n", A + A)
print("A × 3（数乘矩阵）：\n", A * 3)
# 逐元素相乘：注意维度匹配，这里A是2×3，[10,20,30]会广播为2×3
print("逐元素相乘（A 的每行×[10,20,30]）：\n", A * np.array([10, 20, 30]))
# 矩阵乘法：A(2×3) @ B(3×2) 结果为2×2
print("矩阵乘法 A @ B（矩阵乘积）：\n", A @ B)
print("A 的转置（形状从2×3变为3×2）：\n", A.T)
print("-" * 60)

# 3. 常用内置矩阵生成
print("3×4 全零矩阵（float类型）：\n", np.zeros((3, 4)))
print("3×3 单位矩阵（对角线为1，float类型）：\n", np.eye(3))
# 随机矩阵：rand生成[0,1)的均匀分布随机数，可补充randn（标准正态分布）
print("2×4 均匀分布随机矩阵（[0,1)）：\n", np.random.rand(2, 4))
print("2×4 标准正态分布随机矩阵（均值0，方差1）：\n", np.random.randn(2, 4))
# 补充：整数随机矩阵（指定范围）
print("2×3 1到10的整数随机矩阵：\n", np.random.randint(1, 11, size=(2, 3)))
print("-" * 60)

# 4. 常用数学函数
# 角度数组：补充将弧度转换为角度的输出，更易理解
arr = np.array([0, np.pi/4, np.pi/2, np.pi])
print("弧度数组：", arr)
print("对应的角度：", np.rad2deg(arr))  # 弧度转角度
print("sin值：", np.sin(arr))
print("cos值：", np.cos(arr))
# 指数和对数：补充自然对数、以10为底的对数
print("自然指数 exp：", np.exp([0, 1, 2]))
print("自然对数 log（ln）：", np.log([1, np.e, np.e**2]))
print("以10为底的对数 log10：", np.log10([1, 10, 100]))
print("开方：", np.sqrt([4, 9, 16, 25]))
print("平方：", np.square([2, 3, 4, 5]))  # 补充平方运算
print("-" * 60)

# 5. 统计函数
data = np.array([1, 2, 3, 4, 5, 100])
print("数据：", data)
print("平均值：", np.mean(data))
print("中位数：", np.median(data))  # 补充中位数（抗异常值更优）
print("标准差：", np.std(data))
print("方差：", np.var(data))  # 补充方差
print("最大/最小值：", np.max(data), np.min(data))
print("最大/最小值的索引：", np.argmax(data), np.argmin(data))  # 补充索引
print("求和：", np.sum(data))
# 补充：去除异常值后的统计（例如去掉100）
data_clean = data[data != 100]
print("去除异常值100后的数据：", data_clean)
print("去除异常值后的平均值：", np.mean(data_clean))
print("-" * 60)