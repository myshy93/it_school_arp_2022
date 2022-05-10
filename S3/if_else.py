
"""
if conditie:
    bloc de cod
    bloc de cod
else:
    cod
    cod
    cod
"""

# [10, 50]

numar = input("n= ") # citim de la tastatura
numar = int(numar) #cast la int

# if numar >= 10 and numar <= 50:
    # True and True pentru 12


if numar < 10 or numar > 50:
    # False and False pentru 12
    print("numar acceptat")
else:
    print("numar ne-acceptat")

