# -*- coding: cp936 -*-
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10,8))  #����һ����СΪ10*8�Ļ���
ax1 = fig.add_subplot(3,3,1)  #�ڻ��������3*3��������λ���ǵ�1��
ax2 = fig.add_subplot(3,3,2)
ax3 = fig.add_subplot(3,3,3)
ax4 = fig.add_subplot(3,3,4)
ax5 = fig.add_subplot(3,3,5)
ax6 = fig.add_subplot(3,3,6)
ax7 = fig.add_subplot(3,3,7)
ax8 = fig.add_subplot(3,3,8)
ax9 = fig.add_subplot(3,3,9)

ax1.plot(np.random.randn(10))
ax2.scatter(np.random.randn(10),np.arange(10),color='r')  #��ɢ��ͼ
ax3.hist(np.random.randn(20),bins=10,alpha=0.3)  #������ͼ
ax4.bar(np.arange(10),np.random.randn(10))  #��ֱ��ͼ
ax5.pie(np.random.randint(1,15,5),explode=[0,0,0.2,0,0])  #������ͼ

x = np.arange(10)
y = np.random.randn(10)
ax6.plot(x,y,color='green')
ax6.bar(x,y,color='k')

data = DataFrame(np.random.randn(1000,10),
                 columns=['one','two','three','four','five','six','seven','eight','nine','ten'])
data2 = DataFrame(np.random.randint(0,20,(10,2)),columns=['a','b'])
data.plot(x='one',y='two',kind='scatter',ax=ax7)  #���DataFrame��һЩ��ͼ
data2.plot(x='a',y='b',kind='bar',ax=ax8,color='red',legend=False)
data2.plot(x='a',y='b',kind='barh',color='m',ax=ax9)
plt.tight_layout() #������ֵ�Ӱ
plt.show()