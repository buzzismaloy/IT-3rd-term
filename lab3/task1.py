# variant 23
# В одномерном числовом списке D длиной N:
# a. вычислить сумму элементов с нечетными индексами.
# b. Заменить все элементы списка D меньшие 15 их удвоенными значениями.
# c. Записать преобразованный список D в обратном порядке
import random

N_size = 6
d_list = [0] * N_size
odd_sum = 0
for i in range(N_size):
    d_list[i] = random.randint(-10,50)
    print(d_list[i], "[", i, "]", end=" ")
print("\n")

#print(sum(d_list[1::2])) питоновский вариант
#t=d_list.copy()
#d_list = [i*2 if i<15 else i for i in t]
#print(1, d_list)

for i in range(N_size): # сишный вариант
    if i % 2 != 0: odd_sum += d_list[i]
    if d_list[i] < 15: d_list[i] *= 2
    print(d_list[i], "[", i, "]", end=" ")


print("\n")
print("the required odd_sum is:", odd_sum, "\n")
print(d_list[::-1])
