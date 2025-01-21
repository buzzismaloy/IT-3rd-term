from math import exp
from math import fabs


def print_list(my_list: []):
    for i in my_list:
        for j in i:
            print(j, end=' ')
        print()


def make_float(i_list: []):
    temp_list = [float(element) for element in i_list]
    return temp_list


def make_d_float(i_list: []):
    i_list = [[float(element) for element in x.split()] for x in i_list]
    return i_list


def function(b1: float, b2: float, b3: float, c1: float, c2: float, c3: float, pressure: [], temperature: []):
    try:
        try:
            eta = []
            counter: int = 0
            for i in pressure:
                T_0 = c1 + c2 * i + c3 * i ** 2
                eta.append([])
                for j in temperature:
                    eta[counter].append(exp(b1 + b2 * i + (b3 * T_0) / (j - T_0)))
                counter += 1
            return eta
        except ArithmeticError:
            print("арифметическая ошибка")
    except:
        print("неверный тип данных")


def difference(data: [], Eta: [], temperature: [], pressure: []):
    try:
        try:
            stdout = open("C:/python/folder for projects/projects/test run/output.txt", "w")
            raznica = []
            for i in range(len(Eta)):
                raznica.append([])
                for j in range(len(Eta[i])):
                    raznica[i].append(round((fabs(Eta[i][j] - data[i][j]) / data[i][j] * 100), 4))
            my_list = list(zip(temperature, pressure, raznica))
            stdout.write("T/K, p/MPa, difference in %\n")
            for i in my_list:
                for j in i:
                    print(j, end=' ', file=stdout)
                print(file=stdout)
            stdout.close()
        except ArithmeticError:
            print("арифметическая ошибка")
    except:
        print("invalid data type")


try:
    Eta = []
    with open('C:/python/folder for projects/projects/test run/input_lab6.txt') as my_file:
        b1 = my_file.readline()
        my_file.seek(len(b1) + 1)
        b2 = my_file.readline()
        my_file.seek(2 * len(b2) + 3)
        b3 = my_file.readline()
        my_file.seek(len(b3) + 2 * len(b1) + 2)
        c1 = my_file.readline()
        my_file.seek(2 * len(c1) + 2 * len(b1))
        c2 = my_file.readline()
        my_file.seek(2 * len(c2) + 3 * len(b1) + 4)
        c3 = my_file.readline()
        my_file.seek(2 * len(c3) + 4 * len(b1) + 3)
        print(b1, b2, b3, c1, c2, c3, end=" ")
    with open('C:/python/folder for projects/projects/test run/pressure_temp.txt') as temp_p_file:
        pressure = make_float(list(temp_p_file.readline().split()))
        temp_p_file.seek(3 * len(pressure))
        temperature = make_float(list(temp_p_file.readline().split()))
        print(pressure, "\n", temperature)
    with open('C:/python/folder for projects/projects/test run/main_data.txt') as exp_file:
        data = make_d_float(exp_file.readlines())
    print_list(data)
    Eta = function(float(b1), float(b2), float(b3), float(c1), float(c2), float(c3), pressure, temperature)
    print_list(Eta)
    difference(data, Eta, temperature, pressure)
    temp_p_file.close()
    exp_file.close()
    my_file.close()
except:
    print("Пустой файл/Введены неверные данные")
    try:
        Eta = []
        b1 = input("введите константу b1: ")
        b2 = input("введите константу b2: ")
        b3 = input("введите константу b3: ")
        c1 = input("введите константу c1: ")
        c2 = input("введите константу c2: ")
        c3 = input("введите константу c3: ")
        pressure = make_float(input("введите давление: ").split())
        temperature = make_float(input("введите температуру: ").split())
        data = make_d_float(input("введите экспериментальные данные: ").split())
        Eta = function(float(b1), float(b2), float(b3), float(c1), float(c2), float(c3), pressure, temperature)
        difference(data, Eta, temperature, pressure)
    except:
        print("некорректные входные данные")
