import numpy as np

# 创建一个二维数组t1，包含两行五列
t1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

# 创建一个一维数组t2，包含十个元素
t2 = np.array(range(10))

# 创建一个一维数组t3，包含从4到10，步长为2的元素
t3 = np.arange(4, 10, 2)

# 创建一个一维数组t4，包含24个元素，数据类型为float64
t4 = np.array(range(24), dtype='float64')

# 获取t4的形状
t5 = t4.shape

# 将t4重新塑形为4行6列的二维数组
t6 = t4.reshape((4, 6))

# 将t6重新塑形为一维数组
t7 = t6.reshape((t6.shape[0]*t6.shape[1]))

# 将t6展平为一维数组
t8 = t6.flatten()

# 打印t4的形状
print(t5)
