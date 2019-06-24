# import pylab
import matplotlib.pyplot as plt

y_List_Init = []
x_List = []


# def plotData(X, y):
#     pylab.figure(1)
#
#     pylab.plot(X, y, 'rx')
#     pylab.xlabel('Population of City in 10,000s')
#     pylab.ylabel('Profit in $10,000s')
#
#     pylab.show()  # 让绘制的图像在屏幕上显示出来


with open('C:/Users/Admin/Desktop/leetcode/100m.txt') as f:
    data = f.readlines()
    for line in f.readlines():
        line.rstrip('\n')
y_List_Init = data[0].split()

# 纵坐标和横坐赋值
y_List = [float(x) for x in y_List_Init]  # 将txt读取的波形值转换为float类型存入数组
x_list = [i for i in range(len(y_List))]  # 横坐标的个数依据纵坐标个数而定

print(y_List)
print(x_list)
print(len(y_List))  # 有多少个Y记录
print(len(x_list))  # 有多少个X记录

plt.plot(x_list, y_List)
plt.show()
