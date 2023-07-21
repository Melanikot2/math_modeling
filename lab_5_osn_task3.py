M = int(input('Введите М: '))
N = int(input('Введите N: '))

import time

timer = time.time()
for m in range(0, M, 1):
    time.sleep(1)
    print(m)
    for n in range(0, N, 1):
        time.sleep(1)
        print(n)

print('Время: ', time.time() - timer)