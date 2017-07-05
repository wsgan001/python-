# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
x= np.linspace(0, 2 * np.pi, 50)
plt.plot(x, np.sin(x), 'r-x', label='Sin(x)')
plt.plot(x, np.cos(x), 'g-*', label='Cos(x)')
plt.legend() # չʾͼ��
plt.xlabel('Rads') # �� x ����ӱ�ǩ
plt.ylabel('Amplitude') # �� y ����ӱ�ǩ
plt.title('Sin and Cos Waves') # ���ͼ�α���
plt.show()