def reading():
    while True:
        try:
            numb = int(input("Введие целое число в диапазоне от 0 до 100: "))
            if numb > 100 or numb < 0:
                print("Вы вышли за границы диапазона")
                continue
            else: return numb
        except ValueError:
            print("Вы ввели неправильное число, повторите ввод")


number = reading()
print("Ваше число = ", number, "\n", end=" ")

if 76 < number < 100: print("Перелет!")
elif 70 < number < 75: print("Попал!")
elif 50 < number < 69: print("Недолет!")
else: print("Не бить по своим!")
