import numpy as np

name = 'Melana'

code = [symbol for symbol in name.upper()]
print(code)

code = sum([ord(symbol) for symbol in name.upper()])
print(code)

for i in range(0, len(code_1)):
    sum_1 += ord(code_1[i])
print('Сумма 1:', sum_1)

name_2 = name.lower()
code_2 = [symbol for symbol in name_2]
print(code_2)
sum_2 = 0

for i in range(0, len(code_2)):
    sum_2 += ord(code_2[i])
print('Сумма 2:', sum_2)