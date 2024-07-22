from matplotlib import pyplot as plt

# 定义x轴数据，从2开始，每次增加2，到26结束
x = range(2, 26, 2)
# 定义y轴数据
y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]

# 创建一个图形对象，设置大小和分辨率
fig = plt.figure(figsize=(10, 5), dpi=80)
# 绘制折线图
plt.plot(x, y)
# 设置x轴刻度
plt.xticks(range(0, 31, 2))
# 设置y轴刻度
plt.yticks(range(10, 31, 2))
# 设置x轴标签
plt.xlabel("time")
# 设置y轴标签
plt.ylabel("temperature")
# 设置图像标题
plt.title("temperature change")
# 显示图像
plt.show()
