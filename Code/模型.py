import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
import scipy.signal


# p=0.5  #合作者初始比例
# 网络初始合作者比例、强势个体比例
def nodes(G, p):
    for node in G:
        G.add_node(node, strategy=0)
        G.add_node(node, role=0)
        G.add_node(node, payoff=0.0)
    for node in random.sample(G.nodes, k=int(10000*p)):
        G.nodes[node]['role'] = 1
    for node in random.sample(G.nodes, k=int(5000)):
        G.nodes[node]['strategy'] = 1
    return G


def node_on_grid(G,p):
    for node in G:
        G.add_node(node, strategy=0)
        G.add_node(node, role=0)
        G.add_node(node, payoff=0.0)
    for node in random.sample(G.nodes, k=int(5000)):
        G.nodes[node]['strategy'] = 1
    for node in random.sample(G.nodes, k=int(10000*p)):
        G.nodes[node]['role'] = 1
    return G


# 费米规则，输入参数节点与其随机一个邻居总收益
def _fermi_updating_rule(wi, wj, beta):
    """
    Returns the probability of individual i adopting individual j strategy
    Parameters
    ----------
    wi : float
        Payoff of individual i
    wj : float
        Payoff of individual j
    beta : float
        Parameter that models the importance of a payoff difference
    Returns
    -------
    pij : float
        Probability of individual i adopting individual j strategy
    """
    return 1 / (1 + np.power(np.e , ((wi - wj) / beta)))


def cooperator_density(strategies, G):
    cooperator = 0
    m = len(strategies)
    for node in G:
        if strategies[node] == 1:
            cooperator += 1
    return cooperator / m


# print("合作频率为：%.2f" % cooperator_density(strategies))
# print(payoff)
# 一次模拟，随机选择一个邻居比较累计收益，按费米规则更新策略
# print(payoff)
def simulate_once(G, payoff):
    stra=nx.get_node_attributes(G, 'strategy')
    for i in G:
        j = random.sample(list(G.neighbors(i)), 1)[0]
        wi, wj = payoff[i], payoff[j]
        pij = _fermi_updating_rule(wi, wj, beta=0.15)
        if np.random.random() < pij:
            #G.nodes[i]['strategy']=G.nodes[j]['strategy']
            G.nodes[i]['strategy']=stra[j]
    return nx.get_node_attributes(G, 'strategy')

def simulates_equal(G,payoff,num,equalM):
    #pay=payoff
    strategies=nx.get_node_attributes(G, 'strategy')
    a = [0.5, ]
    #print(a)
    for i in range(num):
        s = simulate_once(G, payoff)
        a.append(cooperator_density(s, G))
        payoff=equal(G,equalM)
       
        #print(a)
    return a, s

def simulates_K(G,payoff,num,Kind_strong,Kind_weak,equalM):
    strategies=nx.get_node_attributes(G, 'strategy')
    a = [0.5, ]
    #print(a)
    for i in range(num):
        s = simulate_once(G, payoff)
        a.append(cooperator_density(s, G))
        payoff = Kind(G,Kind_strong,Kind_weak, equalM)
    return a, s

def simulates_H(G,payoff,num,Harm_strong,Harm_weak,equalM):
    strategies=nx.get_node_attributes(G, 'strategy')
    a = [0.5, ]
    #print(a)
    for i in range(num):
        s = simulate_once(G, payoff)
        a.append(cooperator_density(s, G))
        payoff = Harm(G, Harm_strong, Harm_weak, equalM)
    return a, s


def simulate_BD_once(G,payoff,strategies,w):
    '''
    a = []
    for node in G.nodes:
        if sum(payoff.values())==0:
            a.append(0)
        else:
            a.append(payoff[node] / sum(payoff.values()))
    #np.random.seed(0)
    p = np.array(a)
    p = list(item/p.sum() for item in p)
    #print(p)
    Gnodes=list(G)
    nodes=np.arange(0,len(G.nodes))
    if p==0:
        return nx.get_node_attributes(G, 'strategy')
    else:
        index=int(np.random.choice(nodes,size=1,p=p))
        #print(index,len(strategies),type(strategies))
        s = strategies.get(index)
        #print(Gnodes[index])
        neighbor = random.sample(list(G.neighbors(Gnodes[index])), 1)[0]
        G.nodes[neighbor]['strategy'] = s
        # a.append(cooperator_density(nx.get_node_attributes(G,'strategy'),G))
        return nx.get_node_attributes(G, 'strategy')
    '''
    n=m=i=0
    nodes={}
    neignbor={}
    pay=list(payoff.values())
    p=[0]*len(pay)
    for i in range(0,len(pay)):
        p[i]=1.0-w+w*pay[i]
       # p.append(f/sum(f))
    for node in G.nodes:
        nodes[n]=node
        n+=1
    p=np.array(p)
    p/=p.sum()
    #print(p)
    birth=np.random.choice(list(nodes.keys()),size=1,replace=False,p=p)
    #print(nodes[int(birth)])
    #print(birth)
    #print(strategies)
    neign=(G.neighbors(nodes[int(birth)]))
    for node in neign:
        neignbor[m]=node
        m+=1
    death=np.random.choice(list(neignbor.keys()),size=1,replace=False)
    strategies[neignbor[int(death)]]=strategies[nodes[int(birth)]]
    #G.nodes[neignbor[int(death)]]['strategy']=G.nodes[nodes[int(birth)]]['strategy']
    return strategies

def simulate_BD(G, payoff, strategies, num):
    a = [cooperator_density(strategies, G), ]
    for i in range(num):
        a.append(cooperator_density(simulate_BD_once(G, payoff, strategies,0.1), G))
    return a


# 对称群体的铲雪博弈
def equal(G,equalM=[]):
    #    for node in G:
    #        G.add_node(node,strategy=0)
    #        G.add_node(node,payoff=0.0)
    #    for node in random.choices(G.nodes,k=1250):
    #        node['strategy']=1
    # 图中所有节点策略，1合作，0背叛
    strategies = nx.get_node_attributes(G, 'strategy')
    # 图中所有节点累计收益
    payoff = nx.get_node_attributes(G, 'payoff')
    payoff=dict.fromkeys(payoff,0)
    # print(strategies)
    # nx.draw_networkx(G,pos=nx.random_layout(G))
    # plt.show()
    # 节点与邻居博弈，累计收益
    #payoff=payoff_init
    for node in G:
        for neighbor in G.neighbors(node):
            if strategies[node] == 1 and strategies[neighbor] == 1:
                payoff[node] += equalM[0][0]
                #payoff[neighbor] += equalM[0][0]
            elif strategies[node] == 1 and strategies[neighbor] == 0:
                payoff[node] += equalM[0][1]
                #payoff[neighbor] += equalM[1][0]
            elif strategies[node] == 0 and strategies[neighbor] == 0:
                payoff[node] += equalM[1][1]
                #payoff[neighbor] += equalM[1][1]
            elif strategies[node] == 0 and strategies[neighbor] == 1:
                payoff[node] += equalM[1][0]
                #payoff[neighbor] += equalM[0][1]
    return payoff


# 纯友好型强势个体的非对称铲雪博弈，返回策略，地位，收益
def Kind(G, Kind_strong=[], Kind_weak=[], equalM=[]):
    #    for node in G:
    #        G.add_node(node,strategy=random.choice([0,1]))
    #        G.add_node(node,role=0)
    #        G.add_node(node,payoff=0.0)
    #    for node in random.choices(G.nodes,k=int(p*2500)):
    #        node['role']=1
    #    for node in random.choices(G.nodes,k=1250):
    #        node['strategy']=1
    # 图中所有节点策略，1合作，0背叛
    strategies = nx.get_node_attributes(G, 'strategy')
    # 图中所有节点地位，1强势，0弱势
    roles = nx.get_node_attributes(G, 'role')
    # 图中所有节点累计收益
    payoff = nx.get_node_attributes(G, 'payoff')
    payoff=dict.fromkeys(payoff,0)
    # print(strategies)
    # nx.draw_networkx(G,pos=nx.random_layout(G))
    # plt.show()
    # 节点与邻居博弈，累计收益
    for node in G:
        for neighbor in G.neighbors(node):
            if roles[node] == roles[neighbor]:
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += equalM[0][0]
                    #payoff[neighbor] += equalM[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += equalM[0][1]
                    #payoff[neighbor] += equalM[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += equalM[1][1]
                    #payoff[neighbor] += equalM[1][1]
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += equalM[1][0]
                    #payoff[neighbor] += equalM[0][1]
            elif roles[neighbor] == 1 and roles[node] == 0:  # 我弱它强
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += Kind_weak[0][0]
                    #payoff[neighbor] += Kind_strong[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += Kind_weak[0][1]
                    #payoff[neighbor] += Kind_strong[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += 0
                    #payoff[neighbor] += 0
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += Kind_weak[1][0]
                    #payoff[neighbor] += Kind_strong[0][1]
            elif roles[neighbor] == 0 and roles[node] == 1:  # 我强它弱
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += Kind_strong[0][0]
                    #payoff[neighbor] += Kind_weak[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += Kind_strong[0][1]
                    #payoff[neighbor] += Kind_weak[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += 0
                    #payoff[neighbor] += 0
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += Kind_strong[1][0]
                    #payoff[neighbor] += Kind_weak[0][1]
    return payoff


# 纯有害型强势个体的非对称铲雪博弈，返回策略，地位，收益
def Harm(G, Harm_strong=[], Harm_weak=[], equalM=[]):
    #    for node in G:
    #        G.add_node(node,strategy=random.choice([0,1]))
    #        G.add_node(node,role=0)
    #        G.add_node(node,payoff=0.0)
    #    for node in random.choices(G.nodes,k=int(p*2500)):
    #        node['role']=1
    #    for node in random.choices(G.nodes,k=1250):
    #        node['strategy']=1
    # 图中所有节点策略，1合作，0背叛
    strategies = nx.get_node_attributes(G, 'strategy')
    # 图中所有节点地位，1强势，0弱势
    roles = nx.get_node_attributes(G, 'role')
    # 图中所有节点累计收益
    payoff = nx.get_node_attributes(G, 'payoff')
    payoff=dict.fromkeys(payoff,0)
    # print(strategies)
    # nx.draw_networkx(G,pos=nx.random_layout(G))
    # plt.show()
    # 节点与邻居博弈，累计收益
    for node in G:
        for neighbor in G.neighbors(node):
            if roles[neighbor] == roles[node]:
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += equalM[0][0]
                    #payoff[neighbor] += equalM[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += equalM[0][1]
                    #payoff[neighbor] += equalM[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += equalM[1][1]
                    #payoff[neighbor] += equalM[1][1]
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += equalM[1][0]
                    #payoff[neighbor] += equalM[0][1]
            elif roles[neighbor] == 1 and roles[node] == 0:  # 我弱它强
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += Harm_weak[0][0]
                    #payoff[neighbor] += Harm_strong[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += Harm_weak[0][1]
                    #payoff[neighbor] += Harm_strong[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += 0
                    #payoff[neighbor] += 0
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += Harm_weak[1][0]
                    #payoff[neighbor] += Harm_strong[0][1]
            elif roles[neighbor] == 0 and roles[node] == 1:  # 我强它弱
                if strategies[node] == 1 and strategies[neighbor] == 1:
                    payoff[node] += Harm_strong[0][0]
                    #payoff[neighbor] += Harm_weak[0][0]
                elif strategies[node] == 1 and strategies[neighbor] == 0:
                    payoff[node] += Harm_strong[0][1]
                    #payoff[neighbor] += Harm_weak[1][0]
                elif strategies[node] == 0 and strategies[neighbor] == 0:
                    payoff[node] += 0
                    #payoff[neighbor] += 0
                elif strategies[node] == 0 and strategies[neighbor] == 1:
                    payoff[node] += Harm_strong[1][0]
                    #payoff[neighbor] += Harm_weak[0][1]
    return payoff


# 绘图：合作频率与迭代次数的函数
def Cooperation_frequency_iteration_number_equal(G,payoff,equalM):
    num = 2000
    iteration = list(range(0, num, 1))
    # cooperation=simulate_BD(G,payoff,strategies,num)  #生灭规则更新
    cooperation, _ = simulates_equal(G,payoff, num, equalM)  # 费米更新
    #co = [(sum(cooperation[i:i + 5]) / 5) for i, num in enumerate(cooperation) if i % 5 == 0]
    # print(len(co))
    # print(len(cooperation))
    data_dict = {}
    for i, j in zip(iteration, cooperation):
        data_dict[i] = j
    # print(data_dict)
    # plt.title("Changes in cooperation frequency during evolution")
    plt.xlabel("Evolution times")
    plt.ylabel("Cooperation density")
    #y = smoothly([i for i in data_dict.values()], 20, 2)
    # print(x)
    # print(y)
    return iteration, data_dict.values()

def Cooperation_frequency_iteration_number_K(G,payoff,Kind_strong,Kind_weak,equalM):
    num = 2000
    iteration = list(range(0, num, 1))
    # cooperation=simulate_BD(G,payoff,strategies,num)  #生灭规则更新
    cooperation, _ = simulates_K(G,payoff, num,Kind_strong,Kind_weak,equalM)  # 费米更新
    #co = [(sum(cooperation[i:i + 5]) / 5) for i, num in enumerate(cooperation) if i % 5 == 0]
    # print(len(co))
    # print(len(cooperation))
    data_dict = {}
    for i, j in zip(iteration, cooperation):
        data_dict[i] = j
    # print(data_dict)
    # plt.title("Changes in cooperation frequency during evolution")
    plt.xlabel("Evolution times")
    plt.ylabel("Cooperation density")
    #y = smoothly([i for i in data_dict.values()], 20, 2)
    return iteration, data_dict.values()

def Cooperation_frequency_iteration_number_H(G,payoff,Harm_strong,Harm_weak,equalM):
    num = 2000
    iteration = list(range(0, num, 1))
    # cooperation=simulate_BD(G,payoff,strategies,num)  #生灭规则更新
    cooperation, _ = simulates_H(G, payoff, num,Harm_strong,Harm_weak,equalM)  # 费米更新
    #co = [(sum(cooperation[i:i + 5]) / 5) for i, num in enumerate(cooperation) if i % 5 == 0]
    # print(len(co))
    # print(len(cooperation))
    data_dict = {}
    for i, j in zip(iteration, cooperation):
        data_dict[i] = j
    # print(data_dict)
    # plt.title("Changes in cooperation frequency during evolution")
    plt.xlabel("Evolution times")
    plt.ylabel("Cooperation density")
    #y = smoothly([i for i in data_dict.values()], 20, 2)
    return iteration, data_dict.values()

def smooth(lx, ly):
    '''
    数据平滑处理
    '''
    x = np.array(lx)
    y = np.array(ly)
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    return [x_smooth, y_smooth]


def smoothly(lx, lenth, poly):  # lenth滤波器窗口长度越大越平滑越小越接近原曲线，应小于lx；poly用于拟合样本的多项式的阶数，越小越平滑越大越接近原曲线。
    x = scipy.signal.savgol_filter(lx, lenth, poly)
    return x


def smooth_xy(lx, ly):
    """数据平滑处理,插值法

    :param lx: x轴数据，数组
    :param ly: y轴数据，数组
    :return: 平滑后的x、y轴数据，数组 [slx, sly]
    """
    x = np.array(lx)
    y = np.array(ly)
    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = make_interp_spline(x, y)(x_smooth)
    return [x_smooth, y_smooth]


