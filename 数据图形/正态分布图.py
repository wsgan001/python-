# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
import math
mu = 2  #��ֵ
sigma = 32  #��׼��

                          #����һ��50��Ԫ�ص����飬��β���ֵ���������׼��
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50) 

                            #������̫�ֲ��Ĺ�ʽд��y
y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)

                            #��x��yΪ�������꣬'r-'��ʾ��ɫ�ߣ�'ro-��ʾ��ɫ�߼�ԭ��'��linewidthΪ�ߵĴ�ϸ��
                            #plot.plot(x, y, 'ro-', linewidth=2)

                              #����Ҳ���ԣ���'go'��ʾ��ɫԭ�㣬markersizeΪԭ���С
plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)

                              #�л�ɫ����
plt.grid(True)

                               #�������ɣ����꣡
plt.show()