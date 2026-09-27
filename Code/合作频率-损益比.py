import 模型 as model
import networkx as nx
import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np
'''
合作频率随损益比r变化的图像
'''
k=4.0
p=0.5
c=1
b=[]
v=0.89
Junzhi1=[]
Junzhi2=[]
Junzhi3=[]
num=450
evr=20   #evr个数取平均
r=r2=r3=list(np.arange(0.2,0.325,0.025))
Jz1=Jz2=Jz3=[0]*int(len(r))
y1=y2=y3=[]
g=0
for rr in r:
    temp=(c/(2*rr)+c/2)
    b.append(temp)
for i in range(10):
    #二维六边形网络
    G=nx.hexagonal_lattice_graph(100,100,periodic=True)
    #二维方格网络
    #G=nx.grid_2d_graph(100,100,periodic=True)
    #G=model.node_on_grid(G,p)
    #NW小世界网络
    #G=nx.newman_watts_strogatz_graph(10000,4,0.5)
    #BA网络
    #G=nx.barabasi_albert_graph(2500, 1)
    #ER网络
    #G=nx.erdos_renyi_graph(2500, 0.6)
    #WS小世界网络
    #G=nx.watts_strogatz_graph(2500,4,0.5)
    #规则网络
    #G=nx.random_graphs.random_regular_graph(4, 2500)
    G=model.nodes(G,p)
    # 图中所有节点策略，1合作，0背叛
    #strategies = nx.get_node_attributes(G, 'strategy')
    # 图中所有节点累计收益
    #payoff_init = nx.get_node_attributes(G, 'payoff')
    #strategies=nx.get_node_attributes(G, 'strategy')
    for bb in b:    
        #收益矩阵
        equalM=[[bb-c/2,bb-c],[bb,0]]
        Kind_strong=[[k*bb-c/2,k*bb-c],[k*bb,0]]
        Kind_weak=equalM
        Harm_strong=Kind_strong
        Harm_weak=[[v*bb-c/2,v*bb-c],[v*bb,0]]
        #payoff2=model.Kind(G,Kind_strong,Kind_weak,equalM)   #纯友好强势个体
        #payoff3=model.Harm(G,Harm_strong,Harm_weak,equalM)   #纯有害强势个体
        payoff1=model.equal(G,equalM)        #相同地位对称个体
        #print(type(payoff3))
        #cooperation3,_=model.simulates_H(G,payoff3,num,Harm_strong,Harm_weak,equalM)
        #G=model.node_on_grid(G,p)
        #cooperation2,_=model.simulates_K(G,payoff2,num,Kind_strong,Kind_weak,equalM)
        #G=model.node_on_grid(G,p)
        cooperation1,_=model.simulates_equal(G,payoff1,num,equalM)
        G=model.node_on_grid(G,p)
        co1=(sum(cooperation1[-5:])/5)
        #co2=(sum(cooperation2[-5:])/5)
        #co3=(sum(cooperation3[-5:])/5)        
        Junzhi1.append(co1)
        #Junzhi2.append(co2)
        #Junzhi3.append(co3)
  
    y1=[(Jz1[i]+Junzhi1[i])/2 for i in range(len(r))]
    #y2=[(Jz2[i]+Junzhi2[i])/2 for i in range(len(r))]
    #y3=[(Jz3[i]+Junzhi3[i])/2 for i in range(len(r))]
    print(y2)
    Jz1=y1
    #Jz2=y2
    #Jz3=y3
    #y1=[]
    y2=[]
    y3=[]
    #Junzhi1=[]
    Junzhi2=[]
    Junzhi3=[]
        
#print(co1==co2)
#print(y1==y2)
#print(Jz1==Jz2,Jz2==Jz3)  
#print(Jz1==Jz3)
#print(Jz1)
#print(r)

plt.xlabel("Cost to benefit ratio r")
plt.ylabel("Cooperation density")

save1=pd.DataFrame(Jz1)
#save2=pd.DataFrame(Jz2)
#save3=pd.DataFrame(Jz3)
save1.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/hex/合作频率-r对称 hex part k=4 p=0.5 c=1.csv",index=False, header=False)
#save2.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/hex/合作频率-r-K群体 2 k=4 p=0.5 c=1.csv",index=False, header=False)
#save3.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/hex/合作频率-r-H群体 hex k=4 p=0.25 c=1.csv",index=False, header=False)
data1={}
#data2={}
#data3={}
#lx1=model.smoothly(Jz1,9,3)
#lx2=model.smoothly(Jz2,9,3)
#lx3=model.smoothly(Jz3,9,3)
for i,j in zip(r,Jz1):
    data1[i]=j
#for ii,jj in zip(r,Jz2):
#    data2[ii]=jj
#for iii,jjj in zip(r,Jz3):
#    data3[iii]=jjj
#print(x)
#print(y)
x1=[i for i in data1.keys()]
y1=[i for i in data1.values()]
#x2=[i for i in data2.keys()]
#y2=[i for i in data2.values()]
#x3=[i for i in data3.keys()]
#y3=[i for i in data3.values()]
plt.xticks(np.arange(0.2,0.3,0.025))
plt.plot(x1,y1,label="Symmetric group",clip_on=False)
#plt.plot(x2,y2,label="Group with kind type strong",clip_on=False)
#plt.plot(x3,y3,label="Group with harmful type strong",clip_on=False)

plt.legend()
plt.show()
