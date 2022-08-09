# list comprehension
list2 = ["Mihai Dinu", "Andrei George", "Bogdan Balint"]


list3 = []

for i in list2:
    tmp = i.split(" ")[1]
    list3.append(tmp)

# print(list3)

list4 = [item.split(" ")[1] for item in list2]
print(list4)

#dict comprehension
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item.upper(): value*dollar_to_pound for item, value in old_price.items()}
print(new_price)
