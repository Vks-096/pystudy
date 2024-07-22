import matplotlib.pyplot as plt
import matplotlib

# 设置字体为黑体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 创建一个大小为10x5，分辨率为80的图像
fig = plt.figure(figsize=(10, 5), dpi=80)

# 定义x轴和y轴的数据
x = [1, 2, 3, 4, 5]
y = [10, 12, 13, 15, 20]

# 绘制柱状图
plt.bar(x, y)

# 显示图像
plt.show()
