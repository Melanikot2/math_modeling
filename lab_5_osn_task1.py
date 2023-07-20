import numpy as np
import random

N = int(input('Введите длину массива: '))
a = np.zeros(N)
b = np.zeros(N)
c = np.zeros(N)

for i in range(0, N, 1):
    a[i] = random.randint(0, 100)
    b[i] = random.randint(0, 100)
    c[i] = random.randint(0, 100)

print(a, b, c)

maximum = [max(a), max(b), max(c)]
print('Наибольший элемент:', max(maximum))

print('Сумма всех элементов:', sum(a) + sum(b) + sum(c))