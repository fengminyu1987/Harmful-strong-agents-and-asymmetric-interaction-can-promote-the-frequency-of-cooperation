import matplotlib.pyplot as plt
import numpy as np
import warnings
import pandas as pd
import 模型 as model
import scipy.stats as st
import seaborn as sns
warnings.filterwarnings('ignore')

'''
#合作频率-迭代次数
num=1000
x=list(range(0,num,1))
font={'family':'Times New Roman',
      'weight':'bold',
      'style':'italic',
      'size':'18'}
font2={'family':'Times New Roman',
      'weight':'normal',
      'style':'italic',
      'size':'13'}
y1=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-time/1/合作频率-迭代次数对称 k=4 r=0.625 v=0.89.csv',header=None)
y2=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-time/1/合作频率-迭代次数K k=4 r=0.625 v=0.89.csv',header=None)
y3=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-time/1/合作频率-迭代次数H k=4 r=0.625 v=0.89.csv',header=None)
y1=y1.values.tolist()
y2=y2.values.tolist()
y3=y3.values.tolist()
y1=sum(y1,[])
y2=sum(y2,[])
y3=sum(y3,[])
#y1=model.smoothly(y1, 4, 3)
#y2=model.smoothly(y2, 4, 3)
#y3=model.smoothly(y3, 4, 3)
plt.tick_params(labelsize=14)
plt.xlabel("Evolution times",fontdict=font)
plt.ylabel("Cooperation density",fontdict=font)
plt.xticks(np.arange(0,1100,100))
#plt.yticks(np.arange(0,0.6,0.1))
#plt.ylim(0,0.6,0.1)
plt.plot(x,y1,label="Symmetric group",clip_on=False,linewidth=3)
plt.plot(x,y2,label="Group with I-type strong agents",clip_on=False,linewidth=3)
plt.plot(x,y3,label="Group with H-type strong agents",clip_on=False,linewidth=3)
#plt.figure(figsize=(400,288))
plt.legend(frameon=False,loc='best',handlelength=2,prop=font2)
#plt.xscale('log')

plt.savefig("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/C-time k=4 r=0.625 c=1 p=0.5 v=0.89.png", dpi=500, bbox_inches='tight')
plt.show()
'''

#合作频率-损益比
num=300
x=list(np.arange(0.2,0.325,0.025))
font={'family':'Times New Roman',
      'weight':'bold',
      'style':'italic',
      'size':'18'}
font2={'family':'Times New Roman',
      'weight':'normal',
      'style':'italic',
      'size':'12.5'}
y1=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/hex/合作频率-r对称 hex part k=4 p=0.5 c=1.csv',header=None)
#y2=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/NW/合作频率-r-K群体 NW k=4 p=0.5 c=1.csv',header=None)
#y3=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-r/NW/合作频率-r-H群体 NW k=4 p=0.5 c=1.csv',header=None)
y1=y1.values.tolist()
#y2=y2.values.tolist()
#y3=y3.values.tolist()
y1=sum(y1,[])
#y2=sum(y2,[])
#y3=sum(y3,[])
#y1=model.smoothly(y1,4,3)
#y2=model.smoothly(y2,7,3)
#y3=model.smoothly(y3,7,3)
plt.tick_params(labelsize=14)
plt.xlabel("Cost-to-benefit ratio r",fontdict=font)
plt.ylabel("Cooperation density",fontdict=font)
plt.xticks(np.arange(0.2,0.325,0.025))
#plt.scatter(x,y2,label="Group with innocuous type strong agents",clip_on=False,s=6)
#plt.scatter(x,y1,label="Symmetric group",clip_on=False,s=6)
#plt.scatter(x,y3,label="Group with harmful type strong agents",clip_on=False,s=6)
#plt.yticks(np.arange(0,0.8,0.1))
plt.plot(x,y1,label="Symmetric group",clip_on=False,linestyle='-',marker='.',markersize=8.0,linewidth=2.5)
#plt.plot(x,y2,label="Group with I-type strong agents",clip_on=False,linestyle='--',marker='.',markersize=8.0,linewidth=2.5)
#plt.plot(x,y3,label="Group with H-type strong agents",clip_on=False,linestyle='--',marker='*',markersize=8.0,linewidth=2.5)
#plt.xscale('log')
#ys1,yl1=st.t.interval(0.95, len(y1) - 1, loc=np.mean(y1, 0),scale=st.sem(y1))
#ys2,yl2=st.t.interval(0.95, len(y2) - 1, loc=np.mean(y2, 0),scale=st.sem(y2))
#ys3,yl3=st.t.interval(0.95, len(y3) - 1, loc=np.mean(y3, 0),scale=st.sem(y3))

#plt.fill_between(x, ys1,yl1,alpha=0.5)
#plt.fill_between(x, ys2,yl2,alpha=0.5)
#plt.fill_between(x, ys3,yl3,alpha=0.5)
plt.legend(frameon=False,loc='best',handlelength=1.5,prop=font2)
#plt.savefig("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/C-r NW k=4 c=1 p=0.5 v=0.89.png", dpi=500, bbox_inches='tight')
plt.show()

'''
#合作频率-不对称度
num=1296
x=list(np.arange(1,10.2,0.2))
font={'family':'Times New Roman',
      'weight':'bold',
      'style':'italic',
      'size':'18'}
font2={'family':'Times New Roman',
      'weight':'normal',
      'style':'italic',
      'size':'12.5'}
y_e=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-k/NW/合作频率-k对称 NW p=0.5 r=0.2 beta=0.15.csv',header=None)
y_s2=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-k/NW/合作频率-k-H强势 NW p=0.5 r=0.2 beta=0.15.csv',header=None)
y_w1=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-k/NW/合作频率-k-K弱势 NW p=0.5 r=0.2 beta=0.15.csv',header=None)
y_w2=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-k/NW/合作频率-k-H弱势 NW p=0.5 r=0.2 beta=0.15.csv',header=None)
y_s1=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-k/NW/合作频率-k-K强势 NW p=0.5 r=0.2 beta=0.15.csv',header=None)
y_e=y_e.values.tolist()
y_s2=y_s2.values.tolist()
y_w1=y_w1.values.tolist()
y_w2=y_w2.values.tolist()
y_s1=y_s1.values.tolist()
y_e=sum(y_e,[])
y_s2=sum(y_s2,[])
y_w1=sum(y_w1,[])
y_w2=sum(y_w2,[])
y_s1=sum(y_s1,[])
y_e=model.smoothly(y_e, 11, 1)
y_s2=model.smoothly(y_s2, 3, 1)
y_w1=model.smoothly(y_w1, 3, 1)
y_w2=model.smoothly(y_w2, 3, 1)
y_s1=model.smoothly(y_s1, 3, 1)
plt.xlabel("Degree of asymmetry k",fontdict=font)
plt.ylabel("Cooperation density",fontdict=font)
plt.tick_params(labelsize=13.5)
plt.xticks(np.arange(1,11,1))
#plt.yticks(np.arange(0.98,1.001,0.005))
#plt.yticks(np.arange(0.9675,1.10075,0.0065))
plt.ylim(0.96, 1.000)
#plt.yticks(np.arange(0.9875,1.10075,0.0025))
#plt.ylim(0.9875, 1.000)
#plt.yticks(np.arange(0.9850,1.10075,0.0025))
#plt.ylim(0.9850, 1.000)
plt.plot(x,y_e,label="Symmetry group",clip_on=False,linestyle='-',marker='.',markersize=8.0,linewidth=2.5)
plt.plot(x,y_s1,label="Strong individuals in I-group",clip_on=False,linestyle='--',marker='^',markersize=8.0,linewidth=2.5)
plt.plot(x,y_w1,label="Weak individuals in I-group",clip_on=False,linestyle='-.',marker='^',markersize=8.0,linewidth=2.5)
plt.plot(x,y_s2,label="Strong individuals in H-group",clip_on=False,linestyle='--',marker='*',markersize=8.0,linewidth=2.5)
plt.plot(x,y_w2,label="Weak individuals in H-group",clip_on=False,linestyle='-.',marker='*',markersize=8.0,linewidth=2.5)
plt.legend(frameon=False,loc='best',handlelength=2,prop=font2,bbox_to_anchor=(0.63,0.47))
#plt.legend(frameon=False,handlelength=2,prop=font2,bbox_to_anchor=(0.42,0.55))
#plt.legend(frameon=False,handlelength=1,prop=font2,bbox_to_anchor=(0.44,0.67))
#plt.legend()
plt.savefig("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/C-k NW k=4 r=0.2 p=0.5 c=1 v=0.89.png", dpi=500, bbox_inches='tight')
plt.show()    
'''
'''
#合作频率-有害度
num=300
font={'family':'Times New Roman',
      'weight':'bold',
      'style':'italic',
      'size':'18'}
font2={'family':'Times New Roman',
      'weight':'normal',
      'style':'italic',
      'size':'12.5'}
#x=list(np.arange(0.35,1.002,0.05))   #r=0.2
#x=list(np.arange(0.8,1.02,0.02))  
x=list(np.arange(0.77,1.001,0.02))  #r=0.625
y1=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-v/NW/合作频率-v对称 NW k=4 r=0.625 beta=0.15.csv',header=None)
y2=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-v/合作频率-v-K群体 NW p=0.5 k=5 r=0.625 beta=0.15.csv',header=None)
y3=pd.read_csv('C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-v/合作频率-v-H群体 NW p=0.5 k=5 r=0.625 beta=0.15.csv',header=None)
y1=y1.values.tolist()
y2=y2.values.tolist()
y3=y3.values.tolist()
y1=sum(y1,[])
y2=sum(y2,[])
y3=sum(y3,[])
y1=model.smoothly(y1,11,2)
y2=model.smoothly(y2,11,2)
#y3=model.smoothly(y3,11,2)
plt.tick_params(labelsize=13.5)
plt.xlabel("Harmful Degree v",fontdict=font)
plt.ylabel("Cooperation density",fontdict=font)
#plt.xticks(np.arange(0.35,1.11,0.1))
#plt.xlim(0.2,1)
plt.xticks(np.arange(0.8,1.051,0.05)) 
#plt.yticks(np.arange(0.9958,1.051,0.0014)) 
#plt.ylim(0.1, 1.05)
#plt.yticks(np.arange(0.9970,1.051,0.0005)) 

plt.plot(x,y1,label="Symmetric group",clip_on=False,linestyle='-',marker='.',markersize=12,linewidth=4)
plt.plot(x,y2,label="Group with I-type strong agents",clip_on=False,linestyle='--',marker='.',color='darkorange',markersize=8.0,linewidth=2.5)
plt.plot(x,y3,label="Group with H-type strong agents",clip_on=False,linestyle='--',marker='*',color='g',markersize=8.0,linewidth=2.5)
#plt.xscale('log')
plt.legend(fontsize=10.5,frameon=False,handlelength=2,prop=font2,loc='best',bbox_to_anchor=(0.32,0.3))
#plt.legend(fontsize=10.5,frameon=False,handlelength=2,prop=font2,bbox_to_anchor=(0.366,0.45))
#ax = sns.regplot(x=x, y=y1, ci=95)
#ax = sns.regplot(x=x, y=y2, ci=95)
#ax = sns.regplot(x=x, y=y3, ci=95)
plt.savefig("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/C-v NW p=0.5 k=5 r=0.625 c=1.png", dpi=500, bbox_inches='tight')
plt.show()
'''