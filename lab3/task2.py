# variant 22.
# Для произвольной строки s из символов кириллицы и цифр произвести следующие операции с использованием сетов:
# a. Определить, сколько неповторяющихся букв в строке s.
# b. Определить есть ли цифры в исходной строке s.
# c. Сформировать из согласных букв строки s кортеж В.
# d. Объединить сет, образованный из строки s, с сетом из латинских символов.
string = "н3изв3стная 1стр0ка1 прив3д3на в5о2т тут 123"
string1 = "THERE ARE NO NUMBERS HERE"  # строка для проверки
lat_my_set = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
              "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
              "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"} # cловарь латинского алфавита, который будет сделан списком
consonants = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t",
              "v", "w", "x", "z", "B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P",
              "Q", "R", "S", "T", "V", "W", "X", "Z", "Б", "В", "Г", "Д", "Ж", "З", "Й", "К",
              "Л", "М", "Н", "П", "Р", "С", "Т", "Ф", "Х", "Ц", "Ч", "Ш", "Щ", "б", "в", "г",
              "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч",
              "ш", "щ"} #словарь согласных букв заглавных и строчных букв латиницы и кириллицы, который будет сделан списком
lat_my_set = set(lat_my_set)
empty_set = set()
my_set = set(string)
consonants = set(consonants)
b_tuple = ()



print("the length of the origin string is: ", len(string), "\n", "and the my_set is:\n", my_set,
      "\nand its length is: ", len(my_set), end=" ")
for i in range(len(string)):
    if string[i].isdigit() and string[i] in my_set:
        my_set.remove(string[i])
        empty_set.add(string[i])
print("\nколичество неповторяющихся букв в моей строке string равно: ", len(my_set), end=" ")
print("\nполученный список: ", my_set, "\nсписок цифр, содержащихся в строке string: ", empty_set, end=" ")

empty_set.update(empty_set, my_set)
empty_set.update(empty_set, lat_my_set)
print("\n", empty_set)

flag: bool = False
for i in range(len(string)):
    if string[i].isdigit():
        flag = True
        break
if flag:
    print("\nЦифры в строке есть")
else:
    print("\nЦифр в строке нет")

b_list = []
for i in range(len(string)):
    if string[i] in consonants:
        b_list.append(string[i])
b_tuple = tuple(b_list)
print("кортеж согласных букв из строки string:\n", b_tuple)
