import 模型 as model
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
'''
合作频率随迭代次数变化的图像
'''
#收益参数
k=4
#b=1.2  #r=0.5
#b=3  #r=0.2
#b=3.83 #r=0.15
b=1.3 #0.625
#b=1.125 #r=0.8
c=1
p=0.5
v=0.89
#收益矩阵
equalM=[[b-c/2,b-c],[b,0]]
Kind_strong=[[k*b-c/2,k*b-c],[k*b,0]]
Kind_weak=equalM
Harm_strong=Kind_strong
Harm_weak=[[v*b-c/2,v*b-c],[v*b,0]]

#二维方格网络
G=nx.grid_2d_graph(100,100,periodic=True)
G=model.node_on_grid(G,p)
#BA网络
#G=nx.barabasi_albert_graph(2500, 1)
#ER网络
#G=nx.erdos_renyi_graph(2500, 0.6)
#WS小世界网络
#G=nx.watts_strogatz_graph(2500,4,0.5)
#规则网络
#G=nx.random_graphs.random_regular_graph(4, 1296)
#G=model.nodes(G,p)
#strategies=nx.get_node_attributes(G, 'strategy')
#payoff=nx.get_node_attributes(G, 'payoff')

print(1)
payoff1=model.equal(G,equalM)        #相同地位对称个体
x1,y1=model.Cooperation_frequency_iteration_number_equal(G,payoff1,equalM)
G=model.node_on_grid(G,p)
print(1)
payoff2=model.Kind(G,Kind_strong,Kind_weak,equalM)
x2,y2=model.Cooperation_frequency_iteration_number_K(G,payoff2,Kind_strong,Kind_weak,equalM)
G=model.node_on_grid(G,p)
print(1)
payoff3=model.Harm(G,Harm_strong,Harm_weak,equalM)   #纯有害强势个体
x3,y3=model.Cooperation_frequency_iteration_number_H(G,payoff3,Harm_strong,Harm_weak,equalM)
print("绘图中...")
G=model.node_on_grid(G,p)
save1=pd.DataFrame(y1)
save2=pd.DataFrame(y2)
save3=pd.DataFrame(y3)
#save1.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/合作频率-迭代次数对称 k=2 r=0.2 v=0.89.csv",index=False, header=False)
#save2.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/合作频率-迭代次数K k=2 r=0.2 v=0.89.csv",index=False, header=False)
#save3.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/合作频率-迭代次数H k=2 r=0.2 v=0.89.csv",index=False, header=False)
#plt.xticks(np.arange(0,1300,100))
plt.yticks(np.arange(0,1,0.1))
plt.plot(x1,y1,label="Symmetric group",clip_on=False)
plt.plot(x2,y2,label="Group with kind type strong",clip_on=False)
plt.plot(x3,y3,label="Group with harmful type strong",clip_on=False)
#plt.xscale('log')
plt.legend()
plt.show()