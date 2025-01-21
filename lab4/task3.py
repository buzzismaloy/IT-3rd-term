import math


def function1(rng: float, x: float, y: float, z: float, h: float):
    for i in range(rng + 1):
        my_x = begin + i * h
        if (math.exp(-my_x - 2) + 1 / (z ** 2 + 4)) == 0:
            my_x = begin + i * h
            pass
        my_number = (1 + y) * ((my_x + y / (my_x ** 2 + 4)) / (math.exp(-my_x - 2) + 1 / (z ** 2 + 4)))
        print("x: ", my_x, "function_1 is: ", my_number)


def function2(rng: float, x: float, y: float, z: float, h: float):
    for i in range(rng + 1):
        my_x = begin + i * h
        if (my_x ** 2 + math.sin(z) ** 2) == 0:
            my_x = begin + i * h
            pass
        my_number = (1 + math.cos(y - 2)) / (my_x ** 2 + math.sin(z) ** 2)
        print("x: ", my_x, "function_2 is: ", my_number)


begin: float = 1.0
end: float = 3.0
step: float = 0.1
y: int = 12
z: int = 6
my_range = int((end - begin) // step)
print("the function 1:", "\n")
function1(my_range + 1, begin, y, z, step)
print("\nthe function 2:", "\n")
function2(my_range + 1, begin, y, z, step)