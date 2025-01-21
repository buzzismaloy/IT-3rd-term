def reading_list():
    the_test_list = input().split()
    my_list = []
    for element in the_test_list:
        try:
            my_list.append(int(element))
        except ValueError:
            continue
    return my_list


int_list = []
int_list = reading_list()
print(int_list)

my_list = int_list.copy()
arithmetic_mean = sum(int_list) / len(int_list)
for i in range(len(my_list)):
    if my_list[i] < 0 and i % 2 == 0: my_list[i] /= 2
    if my_list[i] == 0: my_list[i] = arithmetic_mean
print(my_list)
minX = min(int_list)
maxX = max(int_list)
my_tuple = ()
temp_list = []

int_list.extend(my_list)
temp_list.extend(int_list)
temp_list.append(minX)
temp_list.append(maxX)
my_tuple = tuple(temp_list)
print(my_tuple)
