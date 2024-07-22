import matplotlib.pyplot as plt
import random
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

# 创建一个图形对象，设置大小和分辨率
fig = plt.figure(figsize=(10, 5), dpi=100)

# 生成120个随机数，范围在20到35之间
a = [random.randint(20, 35) for i in range(120)]

# 生成120个整数，作为x轴的坐标
b = range(120)

# 绘制折线图，设置颜色、线宽、线型
plt.plot(b, a)

# 设置x轴的刻度标签，每隔15个点设置一个标签，标签格式为'10点{}分'或'11点{}分'
x = list(b)
# 创建一个列表xl，包含10点到11点的所有分钟数
xl = ['10点{}分'.format(i) for i in range(60)]
# 将11点到12点的分钟数添加到xl列表中
xl += ['11点{}分'.format(i) for i in range(60)]
# 设置x轴的刻度标签，每隔15个刻度显示一个标签，标签内容为xl列表中的对应元素，标签旋转45度
plt.xticks(x[::15], xl[::15], rotation=45)
plt.xlabel('时间')
plt.ylabel('温度')
plt.title('温度变化图')

# 显示图形
plt.show()
