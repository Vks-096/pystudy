import matplotlib.pyplot as plt
import matplotlib

# 设置matplotlib的字体为SimHei，用来正常显示中文标签
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 定义两个列表a和b，分别表示3月和10月的气温
a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
     23]
b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 22, 21, 24, 24, 26, 27, 26, 24, 21, 18, 17, 16, 17, 21, 21, 24, 24, 25, 24,
     23, 24]

# 定义两个列表x1和x2，分别表示3月和10月的日期
x1 = range(len(a))
x2 = range(50, 50+len(b))

# 将x1和x2合并为一个列表x
x = list(x1) + list(x2)

# 创建一个figure对象，设置大小和分辨率
fig = plt.figure(figsize=(10, 5), dpi=80)

# 定义两个列表rq，分别表示3月和10月的日期标签
rq = ['3月{}日'.format(i+1) for i in x1]
rq += ['10月{}日'.format(i-49) for i in x2]

# 设置x轴的刻度标签，并旋转45度
plt.xticks(list(x)[::3], rq[::3], rotation=45)

# 绘制3月和10月的气温散点图
plt.scatter(x1, a, label='3月气温')
plt.scatter(x2, b, label='10月气温')

# 添加图例，并设置位置
plt.legend(loc='upper left')

# 显示图形
plt.show()
