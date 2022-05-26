import time

# help si dir
start = time.time()

for i in range(10000):
    print(10 ** i)

stop = time.time()

print("Started at", start)
print("End at:", stop)
print("Duration:", stop - start)