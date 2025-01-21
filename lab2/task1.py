#variant 23
temperature_c = float(input())
temperature_f = float(input())
#print(9/5)
t_f = temperature_c * (9/5) + 32.0
t_k = temperature_c + 273.15
print("the farenheit and kelvins: ", t_f, t_k)
t_c =(5/9)*(temperature_f - 32)
t_k = t_c + 273.15
print("the celsius and kelvins: ", t_c, t_k)
