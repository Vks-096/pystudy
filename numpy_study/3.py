import numpy as np

# 定义文件路径
file = './3.csv'

# 从文件中读取数据，以逗号分隔，数据类型为字符串，不进行拆分
x1 = np.loadtxt(file, delimiter=',', dtype='str', unpack=True)
# 从文件中读取数据，以逗号分隔，数据类型为字符串，进行拆分
x2 = np.loadtxt(file, delimiter=',', dtype='str', unpack=False)
# 将x1进行转置
x3 = x1.transpose()
# 将x1进行转置
x4 = x1.T
# 将x1的第0轴和第1轴进行交换
x5 = x1.swapaxes(0, 1)

# 打印x3和x4
print(x3, x4)