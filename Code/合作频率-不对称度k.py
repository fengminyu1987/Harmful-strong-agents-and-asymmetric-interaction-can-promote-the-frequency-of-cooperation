# -*- coding: utf-8 -*-
"""
合作频率-不对称度k
"""
import networkx as nx
import matplotlib.pyplot as plt
import 模型 as model
import random
import numpy as np
import pandas as pd
#收益参数
#b=1.05  #r=0.909
#b=1.125 #r=0.8

#b=1.3  #r=0.625
#b=3.625 #r=0.16
#b=3.278 #=0.18
#b=5.5  #r=0.1
b=3 #r=0.2
c=1
p=0.5
num=1296
v=0.89

def cooperator_density_by_role(G,strategies,roles):
    strong=0
    strong_all=0
    weak=0
    weak_all=0
    for node in G:
        if roles[node]==1:
            strong_all+=1
            if strategies[node]==1:
                strong+=1
        elif roles[node]==0:
            weak_all+=1
            if strategies[node]==1:
                weak+=1
    density_strong=strong/strong_all
    density_weak=weak/weak_all
    return density_strong,density_weak

def simulate_once(G, payoff):
    for i in G:
        j = random.sample(list(G.neighbors(i)), 1)[0]
        wi, wj = payoff[i], payoff[j]
        pij = model._fermi_updating_rule(wi, wj, beta=0.15)
        if np.random.random() < pij:
            G.nodes[i]['strategy']=G.nodes[j]['strategy']
            #strategies[i] = strategies[j]
    return nx.get_node_attributes(G, 'strategy')
#迭代num次,得到每一次迭代的合作密度

def simulates_add_K(G,payoff,num,Kind_strong,Kind_weak,equalM):
    strategies=nx.get_node_attributes(G, 'strategy')
    roles=nx.get_node_attributes(G, 'role')
    a,b=cooperator_density_by_role(G,strategies,roles)
    strong=[a,]
    weak=[b,]
    for i in range(num):
        s=simulate_once(G,payoff)
        c,d=cooperator_density_by_role(G,s,roles)
        strong.append(c)
        weak.append(d)
        payoff=model.Kind(G,Kind_strong,Kind_weak,equalM)
    return strong,weak

def simulates_add_H(G,payoff,num,Harm_strong,Harm_weak,equalM):
    strategies=nx.get_node_attributes(G, 'strategy')
    roles=nx.get_node_attributes(G, 'role')
    a,b=cooperator_density_by_role(G,strategies,roles)
    strong=[a,]
    weak=[b,]
    for i in range(num):
        s=simulate_once(G,payoff)
        c,d=cooperator_density_by_role(G,s,roles)
        strong.append(c)
        weak.append(d)
        payoff=model.Harm(G,Harm_strong,Harm_weak,equalM)
    return strong,weak
k_list=list(np.arange(1,10.2,0.2))
y_e=[]
y_s1=[]
y_s2=[]
y_w1=[]
y_w2=[]
Jz_s1=Jz_s2=Jz_e=Jz_w1=Jz_w2=[0]*len(k_list)
for i in range(10):
    #二维六边形网络
    #G=nx.hexagonal_lattice_graph(36,36,periodic=True)
    #二维方格网络
    G=nx.grid_2d_graph(36,36,periodic=True)
    G=model.node_on_grid(G,p)
    #BA网络
    #G=nx.barabasi_albert_graph(2500, 1)
    #ER网络
    #G=nx.erdos_renyi_graph(2500, 0.6)
    #WS小世界网络
    #G=nx.watts_strogatz_graph(2500,4,0.5)
    #NW小世界网络
    #G=nx.newman_watts_strogatz_graph(1296,4,0.5)
    #规则网络
    #G=nx.random_graphs.random_regular_graph(4, 2500)
    #G=model.nodes(G,p)
    for k in k_list:  
        #收益矩阵
        equalM=[[b-c/2,b-c],[b,0]]
        Kind_strong=[[k*b-c/2,k*b-c],[k*b,0]]
        Kind_weak=equalM
        Harm_strong=Kind_strong
        Harm_weak=[[v*b-c/2,v*b-c],[v*b,0]]
        payoff2=model.Kind(G,Kind_strong,Kind_weak,equalM)   #纯友好强势个体
        payoff3=model.Harm(G,Harm_strong,Harm_weak,equalM)   #纯有害强势个体
        payoff1=model.equal(G,equalM)        #相同地位对称个体
        strong_density2,weak_density2=simulates_add_H(G,payoff3,num,Harm_strong,Harm_weak,equalM)
        G=model.node_on_grid(G,p)
        strong_density1,weak_density1=simulates_add_K(G,payoff2,num,Kind_strong,Kind_weak,equalM)
        G=model.node_on_grid(G,p)
        density_e,_=model.simulates_equal(G,payoff1,num,equalM)
        G=model.node_on_grid(G,p)
        Junzhi_e=(sum(density_e[-100:])/100)
        Junzhi_s1=(sum(strong_density1[-100:])/100)
        Junzhi_s2=(sum(strong_density2[-100:])/100)
        Junzhi_w1=(sum(weak_density1[-100:])/100)
        Junzhi_w2=(sum(weak_density2[-100:])/100)
        y_s1.append(Junzhi_s1)
        y_s2.append(Junzhi_s2)
        y_e.append(Junzhi_e)
        y_w1.append(Junzhi_w1)
        y_w2.append(Junzhi_w2)
    J1=[(y_s1[j] + Jz_s1[j])/2 for j in range(len(k_list))]
    J2=[(y_s2[j] + Jz_s2[j])/2 for j in range(len(k_list))]
    Je=[(y_e[j] + Jz_e[j])/2 for j in range(len(k_list))]
    J11=[(y_w1[j] + Jz_w1[j])/2 for j in range(len(k_list))]
    J21=[(y_w2[j] + Jz_w2[j])/2 for j in range(len(k_list))]
    Jz_s1=J1
    Jz_s2=J2
    Jz_e=Je
    Jz_w1=J11
    Jz_w2=J21
    print(Je[30],J21[30],J11[30])
    Je=[]
    J1=[]
    J2=[]
    J11=[]
    J21=[]
    y_s1=[]
    y_s2=[]
    y_e=[]
    y_w1=[]
    y_w2=[]
save_e=pd.DataFrame(Jz_e)
save_s1=pd.DataFrame(Jz_s1)
save_s2=pd.DataFrame(Jz_s2)
save_w1=pd.DataFrame(Jz_w1)
save_w2=pd.DataFrame(Jz_w2)
save_e.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/实验/合作频率-k对称 2 p=0.5 r=0.2 beta=0.15.csv",index=False, header=False)
save_s2.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/实验/合作频率-k-H强势 2 p=0.5 r=0.2 beta=0.15.csv",index=False, header=False)
save_w1.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/实验/合作频率-k-K弱势 2 p=0.5 r=0.2 beta=0.15.csv",index=False, header=False)
save_w2.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/实验/合作频率-k-H弱势 2 p=0.5 r=0.2 beta=0.15.csv",index=False, header=False)
save_s1.to_csv("C:/Users/SongleeH/Desktop/韩松霖的idea/实验/合作频率-k-K强势 2 p=0.5 r=0.2 beta=0.15.csv",index=False, header=False)
plt.xlabel("Degree of asymmetry k")
plt.ylabel("Cooperation density")
data_s1={}
data_s2={}
data_e={}
data_w1={}
data_w2={}
for i,j in zip(k_list,Jz_s1):
    data_s1[i]=j
for ii,jj in zip(k_list,Jz_s2):
    data_s2[ii]=jj
for iii,jjj in zip(k_list,Jz_e):
    data_e[iii]=jjj
for iiii,jjjj in zip(k_list,Jz_w1):
    data_w1[iiii]=jjjj
for iiiii,jjjjj in zip(k_list,Jz_w2):
    data_w2[iiiii]=jjjjj
    #lx1=model.smoothly(Jz1,9,3)
    #lx2=model.smoothly(Jz2,9,3)
    #lx3=model.smoothly(Jz3,9,3)
    #print(x)
    #print(y)
print(data_e==data_s1,data_s2==data_w1,data_w1==data_w2)
X_s1=[i for i in data_s1.keys()]
Y_s1=[i for i in data_s1.values()]
X_s2=[i for i in data_s2.keys()]
Y_s2=[i for i in data_s2.values()]
X_w1=[i for i in data_w1.keys()]
Y_w1=[i for i in data_w1.values()]
X_w2=[i for i in data_w2.keys()]
Y_w2=[i for i in data_w2.values()]
X_e=[i for i in data_e.keys()]
Y_e=[i for i in data_e.values()]
plt.xticks(np.arange(0,10,1))
plt.plot(X_e,Y_e,label="Symmetry group",clip_on=False,linestyle='-',marker='.')
plt.plot(X_s1,Y_s1,label="Strong cooperator in K group",clip_on=False,linestyle='--',marker='^')
plt.plot(X_w1,Y_w1,label="Weak cooperator in K group",clip_on=False,linestyle='-.',marker='^')
plt.plot(X_s2,Y_s2,label="Strong cooperator in H group",clip_on=False,linestyle='--',marker='*')
plt.plot(X_w2,Y_w2,label="Weak cooperator in H group",clip_on=False,linestyle='-.',marker='*')
plt.legend()
plt.show()            