# in line functions

list1 = [2.45, 4.56, 5.0, 56.6, 99]

# def convert_euro(n):
#     return n * 4.95

# print(convert_euro)

# print([convert_euro(i) for i in list1])

# map1 = map(lambda x: x * 4.95, list1)

# for i in map1:
#     print(i)

convert_euro = lambda n, y: n * 4.95 + y
print(lambda x: x)
print(convert_euro)
print(convert_euro(10, 32))