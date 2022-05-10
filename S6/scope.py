# global scope
PI = 3.14

def p_cerc(r):
    #local scope
    return 2 * PI * r

def a_cerc(r):
    # local scope
    return PI * r ** 2

print(a_cerc(10))
print(p_cerc(10))

# def bar():
#     # local scope
#     age = 1
#     age1 = age + 10
#     print(age1)



# bar()

# def reverse(n):
#     rev = 0
#     while n != 0:
#         c = n % 10 # rest
#         n = n // 10 # cat
#         rev = rev * 10 + c

#     return rev



# for i in range(rev):
#     print(i)




