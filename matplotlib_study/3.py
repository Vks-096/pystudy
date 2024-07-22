# 导入matplotlib.pyplot模块
import matplotlib.pyplot as plt
# 导入matplotlib模块
import matplotlib

# 设置matplotlib的字体为SimHei
matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# 创建一个9x6的图形，分辨率为80
fig = plt.figure(figsize=(9, 6), dpi=80)
# 定义一个列表a，包含1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1
a = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
# 定义一个列表b，包含11到30的整数
b = list(range(11, 31, 1))
c = [1, 2, 3, 1, 2, 1, 1, 2, 1, 2, 4, 3, 1, 2, 2, 3, 2, 3, 1, 2]

# 定义一个列表nl，包含11岁到30岁的字符串
nl = ['{}岁'.format(i) for i in b]
# 定义一个列表ny，包含1个到6个的字符串
ny = ['{}个'.format(i) for i in a]

# 绘制折线图，x轴为b，y轴为a
plt.plot(b, a, label='自己')
# 设置x轴刻度为nl，旋转45度
plt.xticks(b, nl, rotation=45)
# 设置y轴刻度为ny
plt.yticks(a, ny)
# 设置x轴标签为年龄
plt.xlabel('年龄')
# 设置y轴标签为男朋友个数
plt.ylabel('男朋友个数')

plt.plot(b, c, label='同桌')
# 添加图例
plt.grid(True)
plt.legend()

# 显示图形
plt.show()
