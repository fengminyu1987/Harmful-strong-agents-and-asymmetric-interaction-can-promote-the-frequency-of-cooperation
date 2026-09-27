# -*- coding: utf-8 -*-
"""
绘图cooperation-v
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import 模型 as model
lx1=pd.read_csv('C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v对称.csv',header=None)
lx2=pd.read_csv('C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v-K群体.csv',header=None)
lx3=pd.read_csv('C:/Users/SongleeH/Desktop/韩松霖的idea/韩松霖的模拟实验/合作频率-v-H群体.csv',header=None)
x1=lx1.values.tolist()
x2=lx2.values.tolist()
x3=lx3.values.tolist()
x1=sum(x1,[])
x2=sum(x2,[])
x3=sum(x3,[])
y=np.arange(0.1,1,0.1)
x1=model.smooth_xy(x1, y)
x2=model.smooth_xy(x2, y)
x3=model.smooth_xy(x3, y)
plt.scatter(y,x1)
plt.scatter(y,x2)
plt.scatter(y,x3)
plt.show()

