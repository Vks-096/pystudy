import matplotlib.pyplot as plt
import matplotlib

# 设置字体为黑体
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
# 创建一个大小为10x5，分辨率为80的图像
fig = plt.figure(figsize=(10, 5), dpi=80)

# 定义x轴和y轴的数据
x = ['猩球崛起3：终极之战', '敦刻尔克', '蜘蛛侠：英雄归来', '战狼2']
x1 = list(range(len(x)))
x2 = [i + 0.2 for i in x1]
x3 = [i + 0.4 for i in x1]

y1 = [15746, 312, 4497, 319]
y2 = [12357, 150, 334, 165]
y3 = [2358, 399, 264, 362]

# 绘制柱状图
plt.bar(x1, y1, width=0.2, color='orange', label='1')
plt.bar(x2, y2, width=0.2, color='green', label='2')
plt.bar(x3, y3, width=0.2, color='blue', label='3')
plt.xticks(x2, x)

plt.legend(loc='upper right')
plt.grid(alpha=0.5, linestyle='--', linewidth=0.5)

# 显示图像
plt.show()
