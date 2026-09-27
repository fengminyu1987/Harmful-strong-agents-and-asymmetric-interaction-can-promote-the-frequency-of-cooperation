import pandas as pd
Jz1=[0.8559138281249999,
0.8598365625,
0.8629069921875,
0.85813796875,
0.8676751171875,
0.867006640625,
0.8600483203125,
0.86198599609375,
0.8658358203125,
0.8672779687500001,
0.8607284374999999,
0.861419765625]
Jz2=[0.8171578906250001,
0.8584110546875,
0.9800348437499999,
0.9985390234375,
0.9988991406250001,
0.999008671875,
0.9988224218749999,
0.99891509765625,
0.9986467578125,
0.9985432421875,
0.9986540234375,
0.98786234375]
#Jz3=[]
save_1=pd.DataFrame(Jz1)
save_2=pd.DataFrame(Jz2)
save_1.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-v/合作频率-v-K群体 p=0.5 k=5 r=0.625 beta=0.15.csv",index=False, header=False)
save_2.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/c-v/合作频率-v-H群体 p=0.5 k=5 r=0.625 beta=0.15.csv",index=False, header=False)
#save_3.to_csv("C:/Users/SongleeH/Desktop/网络博弈/韩松霖的idea/大修实验/合作频率-v-K弱势 p=0.5 k=2 r=0.625 beta=0.15.csv",index=False, header=False)