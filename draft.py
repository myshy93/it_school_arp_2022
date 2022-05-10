# 4! = 1 * 2 * 3 * 4


def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n


# 1. 1 * 2 * 3 * 4
# 2. 1 * 2 * 3
# 3. 1 * 2
# 4. 1


# 

print(factorial(100))