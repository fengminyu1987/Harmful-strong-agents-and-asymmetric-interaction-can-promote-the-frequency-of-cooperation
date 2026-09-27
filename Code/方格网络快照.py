'''
方格网络快照
不同实验调整 ①群体类型 ②节点颜色函数 ③b值：损益比r
'''
import networkx as nx
import 模型 as model
import matplotlib.pyplot as plt

#收益参数
k=1.2
#b=1.3  #r=0.625 ok
b=2.0625 #r=0.32 ok
c=1
p=0.5
v=0.89
#收益矩阵
equalM=[[b-c/2,b-c],[b,0]]
Kind_strong=[[k*b-c/2,k*b-c],[k*b,0]]
Kind_weak=equalM
Harm_strong=Kind_strong
Harm_weak=[[v*b-c/2,v*b-c],[v*b,0]]
G=nx.grid_2d_graph(100,100,periodic=True)
G=model.node_on_grid(G,p)
roles=nx.get_node_attributes(G, 'role')
strategies=nx.get_node_attributes(G, 'strategy')
#payoff=model.Kind(G,Kind_strong,Kind_weak,equalM)
payoff=model.Harm(G,Harm_strong,Harm_weak,equalM)   #纯有害强势个体
#payoff=model.equal(G,equalM)        #相同地位对称个体
_,strategies_new=model.simulates_equal(G,payoff, 1000, equalM)
#_,strategies_new=model.simulates_K(G,payoff,1000,Kind_strong,Kind_weak,equalM)
#_,strategies_new=model.simulates_H(G,payoff, 1000,Harm_strong,Harm_weak,equalM)

#print(strategies1)
def node_color(G,strategies):
    node_color=[]
    for node in G.nodes:
        if strategies[node]==1:
            node_color.append('#FFA500')  #orange  合作
        elif strategies[node]==0:
            node_color.append('#00BFFF')  #deepskyblue  背叛
    return node_color
def node_color_add(G,strategies,roles):
    node_color=[]
    for node in G:
        if roles[node]==1 and strategies[node]==1:
            node_color.append('#FF0000')  #red 强势合作
        elif roles[node]==1 and strategies[node]==0:
            node_color.append('#32CD32')  #limegreen 强势背叛
        elif roles[node]==0 and strategies[node]==1:
            node_color.append('#FFA500')  #orange 弱势合作
        elif roles[node]==0 and strategies[node]==0:
            node_color.append('#00BFFF')  #deepskyblue 弱势背叛
    return node_color
n_color=node_color(G,strategies_new)
#n_color=node_color_add(G,strategies_new,roles)
pos=dict((n,n) for n in G.nodes())
nx.draw_networkx_nodes(G,pos=pos,node_color=n_color,node_size=10,node_shape='s')
plt.axis('off')
plt.axis('square')
plt.show()





