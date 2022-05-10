# 7. Scrie un program care citeste de la tastatura un nr. natural
# si verifica daca acesta este palindrom. 111 121 292 2992 33533


# Functie care returneaza True daca un nr este palindrom.

# Citim de la tst un nr

# Apelam fct.

# 178 == 871 False
# 121 == 121 True

# 178
# 8
# 17
# 7
# 1
# 
# 871
# 87
# 8
# 0

# rev = 1
# rev = 17
# rev = 178

def reverse(n):
    rev = 0
    while n != 0:
        c = n % 10 # rest
        n = n // 10 # cat
        rev = rev * 10 + c

    return rev

def palindrom(n):
    """Check if palindrom."""
     
nr = 
print(reverse(871))

