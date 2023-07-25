import numpy as np
import time

a = 2
b = 3
c = 4
d = 5
e = 6 



def map_func(x, a=2, b=3, c=4, d=5, e=6):
    y = a * x ** 4 + b * x ** 3 + c * x ** 2 + d * x + e
    return y

x = np.linspace(-5, 5, 10 ** 5)

time_map = time.time()
map_list = list(map(map_func, x))
print(f'time map = {time.time() - time_map} seconds')

time_listcomp = time.time()
listcomp = [map_func(x0) for x0 in x]
print(f'time listcomp = {time.time() - time_listcomp} seconds')

time_cycle = time.time()
cycle = []
for i in range(0, 10 ** 5, 1):
    cycle.append(a * i ** 4 + b * i ** 3 + c * i ** 2 + d * i + e)
print(f'time cycle = {time.time() - time_cycle} seconds')

print('Списковое включение быстрее') 