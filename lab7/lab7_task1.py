'''
23. Создать трёхдиагональную матрицу 7×7 для x, где главная диагональ равна sqrt(x), значения над
главной диагональю x^3/985, значения под главной диагональю x^(7/8)/467, x выбрать любое.
'''
import numpy as np
from math import sqrt


def reading():
    while True:
        try:
            numb = float(input("Введие целое число: "))
            return numb
        except ValueError:
            print("неправильный тип данных")


size: float = 7
x = reading()
my_array = np.zeros((size, size))
buf_array = my_array.ravel()
buf_array[0::size + 1] = sqrt(x)
buf_array[size::size + 1] = x ** (7 / 8) / 467
buf_array[1::size + 1] = x ** 3 / 985
for i in my_array:
    for j in i:
        print(f'{j:5.4f}', ',', end=' ')
    print()
