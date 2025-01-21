import math

'''def reading():
    while True:
        try:
            numb = float(input("Введие вещественное число: "))
            return numb
        except ValueError:
            print("Вы ввели неправильное число, повторите ввод")
'''
b1: float = -1.64587
b2: float = 0.00626
b3: float = 4.6575
c1: float = 172.12865
c2: float = 0.16221
c3: float = -0.00038
T0: float = 175.93506

data = [[87.83, 57.07, 28.14, 16.05, 10.39],
        [89.36, 58.01, 28.55, 16.27, 10.52],
        [96.46, 62.34, 30.44, 17.25, 11.13],
        [106.08, 68.16, 32.95, 18.55, 11.92],
        [128.11, 81.30, 38.51, 21.37, 13.61],
        [154.42, 96.66, 44.83, 24.52, 15.47],
        [185.76, 114.55, 52.00, 28.01, 17.49],
        [223.04, 135.32, 60.09, 31.86, 19.67],
        [267.28, 159.34, 69.17, 36.09, 22.02],
        ]

pressure = [0.1, 1, 5, 10, 20, 30, 40, 50, 60]
temperature = [303.15, 313.15, 333.15, 353.15, 373.15]
print("температура = ", temperature, "\n", "давление = ", pressure, "\n", end=" ")

Eta = []
counter = 0
for i in pressure:
    T_0 = c1 + c2 * i + c3 * i ** 2
    Eta.append([])
    for j in temperature:
        Eta[counter].append(math.exp(b1 + b2 * i + (b3 * T_0) / (j - T_0)))
    counter += 1

for i in range(len(pressure)):
    for j in range(len(temperature)):
        print(Eta[i][j], end=" ")
    print("\n", end=" ")

''' Eta[i].append(exp(b1 + b2 * pressure[i] + D_a * T_0) / (temperature[j] - T_0))'''

raznica = []
for i in range(len(Eta)):
    raznica.append([])
    for j in range(len(Eta[i])):
        raznica[i].append(math.fabs(Eta[i][j] - data[i][j]) / data[i][j] * 100)

my_list = list(zip(temperature, pressure, raznica))
print(my_list)
