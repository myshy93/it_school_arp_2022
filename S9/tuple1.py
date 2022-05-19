banned_countries = ('Romania', 'Lituania', 'Norvegia')

list_banned = list(banned_countries)
list_banned[2] = "XXXX"

same_elements = True

if len(banned_countries) == len(list_banned):
    for i in range(len(banned_countries)):
        if banned_countries[i] != list_banned[i]:
            same_elements = False
            break

print("Lista nemodificata:", same_elements)