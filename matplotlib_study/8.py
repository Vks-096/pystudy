import matplotlib.pyplot as plt
import matplotlib

# 设置matplotlib的字体为SimHei，用来正常显示中文标签
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 创建一个大小为10x5，分辨率为80的图形
fig = plt.figure(figsize=(10, 5), dpi=80)

# 定义x轴数据
x = [11, 2, 20, 30, 50, 10, 40, 60, 70, 80, 90, 100, 20, 25, 23, 28, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90,
     95, 100]

# 绘制直方图，将x轴数据分为30个区间
plt.hist(x, 30)
# 设置x轴和y轴的标签
plt.xlabel('数值')

plt.grid()


# 显示图形
plt.show()
