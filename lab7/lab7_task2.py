'''6. Задать произвольный строковый массив размерностью 10×10 и разделить его на строки. '''
import numpy as np
from random import choice


size: int = 10
letters = ['aa1', 'bh3', 'cqs', 'dfh', 'eqs', 'fze', 'zxc', 'hhp', 'php', 'c++', '322']
charar = np.chararray((size, size), itemsize=3)
for i in range(size):
    for j in range(size):
        charar[i][j] = choice(letters)
print(charar)
print(np.array2string(charar).split())
