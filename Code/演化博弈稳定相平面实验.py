#演化博弈稳定相平面实验1
import random
import matplotlib.pyplot as plt
#plt.rcParams['axes.unicode_minus']=False  #用于解决不能显示负号的问题
#mpl.rcParams['font.sans-serif'] = ['SimHei']
#各博弈主体动态复制方程

b=1.5
c=1
n=1.2
p=0.8
v=0.89
def f(x,y):
    return -x*(x - 1)*(p*(x*(b - c/2) - (b - c)*(x - 1)) + (y*(c/2 - b*n) - (y - 1)*(c - b*n))*(p - 1) - b*p*x + b*n*y*(p - 1))
#K类型
#def g(x,y):
    #return -y*(y - 1)*((p*x - y*(p - 1))*(b - c/2) - b*(p*x - y*(p - 1)) + ((p - 1)*(y - 1) - p*(x - 1))*(b - c))
#H类型
def g(x,y):
    return -y*(y - 1)*(b*y*(p - 1) - y*(b - c/2)*(p - 1) + (b - c)*(p - 1)*(y - 1) - p*x*(c/2 - b*v) + p*(x - 1)*(c - b*v) - b*p*v*x)
#initX-x初始值
#initY-y初始值
#dt-步长
#epoch-迭代次数
def calculateValue(initX, initY, dt, epoch):
    x = []
    y = []

    #演化初始赋值
    x.append(initX)
    y.append(initY)

    #微量计算及append
    for index in range(epoch):
        tempx = x[-1] + (f(x[-1],y[-1])) * dt
        tempy = y[-1] + (g(x[-1],y[-1])) * dt

        x.append(tempx)
        y.append(tempy)
    return (x, y)
plt.figure(figsize=(7,7))

D=[]
#随机生成200个初始点
for index in range(200):
    random_a=random.random()
    random_b=random.random()
    #步长dt为0.001 迭代次数10000
    d=calculateValue(random_a,random_b,0.01,10000)
    D.append(d)

for o,m in D:
    plt.plot(o,m,color='steelblue',zorder=1)
#arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="b")
plt.scatter(0.7,0, color='r',zorder=3)
plt.annotate((0.7,0),xy=(0.7,0),xytext=(0.7,0.05),fontsize=20)
plt.ylabel("$y$",fontsize=18)
plt.xlabel("$x$",fontsize=18)
plt.tick_params(labelsize=20)
plt.axis([0,1,0,1])
plt.grid(linestyle="-",color="none",linewidth=1)
plt.savefig("test",dpi=300,bbox_inches ="tight")

