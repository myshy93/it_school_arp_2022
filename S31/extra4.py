# all()
# any()
# map()
# zip()

from cmath import sqrt


list1 = [10, 24, 3, 45]
[True, False, True, True]
print(all([i % 2 == 1 for i in list1]))

print(any([i % 2 == 0 for i in list1]))

map1 = map(sqrt, list1)

for i in map1:
    print(i)

list2 = [pow(i, 2) for i in list1]

print(list1)
print(list2)

zip1 = zip(list1, list2)

for i in zip1:
    print(i)

