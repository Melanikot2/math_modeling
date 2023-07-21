import time

timer = time.time()
for i in range(10):
    print(i)
    time.sleep(i)

print(f'{time.time() - timer}, seconds')