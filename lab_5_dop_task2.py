import random

def rand(n, a):
    b = random.randint(0, n - 1)
    i = 0

    while i == 0:
        i = 1
        for j in range(0, len(a), 1):
            if a[j] == b:
                i = 0
                b = random.randint(0, n - 1)

    return b

print('Число:', rand(n, a))