import numpy as np

name = 'M_e_l_a_n_a_'

name_1 = name.upper()
print(name_1)

code_1 = np.zeros(len(name))
n = 0
for symbol in name_1:
    code_1[n] = ord(symbol)
    n += 1
print(code_1)

name_2 = name.lower()
print(name_2)

code_2 = np.zeros(len(name))
n = 0
for symbol in name_2:
    code_2[n] = ord(symbol)
    n += 1
print(code_2)

a = [max(code_1), max(code_2)]
b = [min(code_1), min(code_2)]
print('Наибольшее значение:', max(a))
print('Наименьшее значение:', min(b))