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
plt.barh(x, y, height=0.1, color='orange')
plt.grid(alpha=0.5, linestyle='--', linewidth=0.5)

# 显示图像
plt.show()
