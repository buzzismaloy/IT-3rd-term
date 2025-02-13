'''
вариант 12. Создать словарь А из списка списков В, в котором попарно заданы целые значения 20, 22, 30, 19
для городов: Москва, Тверь, Елец, Новгород соответственно.
a. Объединить все значения из словаря через запятую в одну строку S.
b. Удалить из словаря А значение с ключом «Елец».
c. Проверить наличие в словаре А элемента с ключом «Пермь» и вывести в консоль «0» в случае
его отсутствия.
'''

source_list = [[20, 22, 30, 19], ["Москва", "Тверь", "Елец", "Новгород"]]
for i in range(1, len(source_list)):  # просто вывод списка, чтобы видеть как формируются пары
    for j in range(len(source_list[i])):
        print(source_list[i - 1][j], source_list[i][j])

my_dict = {}  # пустой словарь в который будут записаны пары из списка списков
for i in range(1, len(source_list)):
    for j in range(len(source_list[i])):
        my_dict.setdefault(source_list[i][j], source_list[i - 1][j])  # заполнение словаря
print(my_dict, "\n")  # вывод заполненного словаря

string = str(my_dict)  # объединение всех значений из словаря в мою строку string
string = string[1:len(string)]
string = string[0:len(string) - 1]  # удаление {}
print(string, "\n")

my_dict.pop("Елец")  # удаление из словаря значение с ключом ЕЛЕЦ
print(my_dict)

if my_dict.get("Пермь") is None: print(0) #проверка наличия в словаре элемента с ключом ПЕРМЬ
else: print(my_dict.get("Пермь"))

