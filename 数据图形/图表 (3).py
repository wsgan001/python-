# -*- coding: cp936 -*-
import matplotlib.pyplot as plt
import numpy as np
# ��ɫӳ��ɢ��ͼ
x = np.random.rand(1000)
y = np.random.rand(1000)
size = np.random.rand(1000) * 5
colour = np.random.rand(1000)
plt.scatter(x, y, size, colour)
plt.colorbar()
plt.show()
