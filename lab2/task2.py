#eto task 2 voobsche to, variant 2
string1 = "Кафедра информационных компьютерных технологий"
print(len(string1))
string1 = string1[0:7] + string1[8:22] + string1[23:35] + string1[36:len(string1)]
#print(string1)
for i in range(0, len(string1)):
    print(string1[i], end='')
#pozhe peredelat eshe odnim sposobom, on budet nizhe

string1 = "Кафедра информационных компьютерных технологий"
string2 = string1.split()
string2 = ''.join(string2)
print(string2)
