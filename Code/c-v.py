# -*- coding: utf-8 -*-
"""
合作频率-有害度v
"""
import networkx as nx
import 模型 as model
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

b=1.3  #r=0.625
#b = 3.83  # r=0.15
c = 1
p = 0.5
k = 1.2
# k=1.25
num = 1296


# 一次模拟，随机选择一个邻居比较累计收益，按费米规则更新策略
def simulate_once(G, payoff, strategies):
    for i in G:
        j = random.sample(list(G.neighbors(i)), 1)[0]
        wi, wj = payoff[i], payoff[j]
        pij = model._fermi_updating_rule(wi, wj, beta=0.8)
        if np.random.random() < pij:
            strategies[i] = strategies[j]
    return strategies


# 迭代num次,得到每一次迭代的合作比例数组
def simulates(G, payoff, strategies, num):
    a = [model.cooperator_density(strategies, G), ]
    for i in range(num):
        s = simulate_once(G, payoff, strategies)
        a.append(model.cooperator_density(s, G))
    return a, s


# 二维方格网络
G = nx.grid_2d_graph(36, 36, periodic=True)
G = model.node_on_grid(G)

# BA网络
# G=nx.barabasi_albert_graph(2500, 1)
# ER网络
# G=nx.erdos_renyi_graph(2500, 0.6)
# WS小世界网络
# G=nx.watts_strogatz_graph(2500,4,0.5)
# 规则网络
# G=nx.random_graphs.random_regular_graph(4, 2500)
# G=model.nodes(G,p)
equalM = [[b - c / 2, b - c], [b, 0]]
Kind_strong = [[k * b - c / 2, k * b - c], [k * b, 0]]
Kind_weak = equalM
Harm_strong = Kind_strong
#v_list = list(np.arange(0.35, 1.1, 0.05))  # r=0.15
v_list=list(np.arange(0.8,1.1,0.05))  #r=0.625
Jz1 = Jz2 = Jz3 = [0] * int(len(v_list))
Junzhi1 = Junzhi2 = Junzhi3 = []
y1 = y2 = y3 = []
for i in range(10):
    for v in range(len(v_list)):
        # 收益矩阵
        Harm_weak = [[v * b - c / 2, v * b - c], [v * b, 0]]
        strategies2, roles2, payoff2 = model.Kind(G, Kind_strong, Kind_weak, equalM)  # 纯友好强势个体
        strategies3, roles3, payoff3 = model.Harm(G, Harm_strong, Harm_weak, equalM)  # 纯有害强势个体
        strategies1, payoff1 = model.equal(G, equalM)  # 相同地位对称个体
        cooperation3, _ = simulates(G, payoff3, strategies3, num)
        cooperation2, _ = simulates(G, payoff2, strategies2, num)
        cooperation1, _ = simulates(G, payoff1, strategies1, num)
        co1 = (sum(cooperation1[-100:]) / 100)
        co2 = (sum(cooperation2[-100:]) / 100)
        co3 = (sum(cooperation3[-100:]) / 100)

        Junzhi1.append(co1)
        Junzhi2.append(co2)
        Junzhi3.append(co3)

    # Junzhi1=[float(sum(cooperation1[i:i+5])/5) for i,num in enumerate(cooperation1) if i%5==0]
    # Junzhi2=[float(sum(cooperation2[i:i+5])/5) for i,num in enumerate(cooperation2) if i%5==0]
    # Junzhi3=[float(sum(cooperation3[i:i+5])/5) for i,num in enumerate(cooperation3) if i%5==0]
    # for l in range(len(Junzhi)):
    #    y.append((Junzhi[l]+Jz[l])/2)
    # print(strategies1==strategies2)
    # print(co2==co3)
    print(Junzhi1 == Junzhi2)
    # print(Junzhi1==Junzhi2)
    y1 = [(Jz1[i] + Junzhi1[i]) / 2 for i in range(len(v_list))]
    y2 = [(Jz2[i] + Junzhi2[i]) / 2 for i in range(len(v_list))]
    y3 = [(Jz3[i] + Junzhi3[i]) / 2 for i in range(len(v_list))]
    print(y1)
    # y=[(Junzhi[l]+Jz[l])/2 for l in range(len(Junzhi))]
    Jz1 = y1
    Jz2 = y2
    Jz3 = y3
    y1 = []
    y2 = []
    y3 = []
    Junzhi1 = []
    Junzhi2 = []
    Junzhi3 = []

# print(co1==co2)
# print(y1==y2)
print(Jz1 == Jz2, Jz2 == Jz3)
# print(Jz1==Jz3)
# print(Jz1)
# print(r)

save1 = pd.DataFrame(Jz1)
save2 = pd.DataFrame(Jz2)
save3 = pd.DataFrame(Jz3)
save1.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v对称r=0.625.csv", index=False,
             header=False)
save2.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v-K群体r=0.625.csv", index=False,
             header=False)
save3.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v-H群体r=0.625.csv", index=False,
             header=False)

plt.xlabel("Harmful Degree v")
plt.ylabel("Cooperation Density")

data1 = {}
data2 = {}
data3 = {}
# lx1=model.smoothly(Jz1,9,3)
# lx2=model.smoothly(Jz2,9,3)
# lx3=model.smoothly(Jz3,9,3)
for i, j in zip(v_list, Jz1):
    data1[i] = j
for ii, jj in zip(v_list, Jz2):
    data2[ii] = jj
for iii, jjj in zip(v_list, Jz3):
    data3[iii] = jjj
# print(x)
# print(y)
x1 = [i for i in data1.keys()]
y1 = [i for i in data1.values()]
x2 = [i for i in data2.keys()]
y2 = [i for i in data2.values()]
x3 = [i for i in data3.keys()]
y3 = [i for i in data3.values()]
plt.xticks(np.arange(0, 1, 0.1))

x1, y1 = model.smooth_xy(x1, y1)
x2, y2 = model.smooth_xy(x2, y2)
x3, y3 = model.smooth_xy(x3, y3)
plt.plot(x1, y1, label="Symmetric group", clip_on=False)
plt.plot(x2, y2, label="Group with kind type strong", clip_on=False)
plt.plot(x3, y3, label="Group with harmful type strong", clip_on=False)
plt.legend()
plt.show()


