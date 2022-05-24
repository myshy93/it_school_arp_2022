user_info = {
    "name": "Alex",
    "age": 28,
    "email": "alex.radu@email.com",
    "gender": "M"
}

china_years = {
    2012: "Iepurelui",
    2011: "Cocosului",
    2010: "Dragonului",
}

# sortare dupa chei
sorted_user_info = sorted(user_info.items())

print("Sortat dupa chei")
for k, v in sorted_user_info:
    print(k, "||",  v)

# sortare dupa valori
print("Sortat dupa valori")

def comparator(t):
    return t[1]

for k, v in sorted(china_years.items(), key=lambda x: x[1]):
    print("Anul", k, "a fost anul", v)

