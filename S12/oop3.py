from auto import Car

# polimofism
ford = Car(False)
vw = Car(True, 2)
toyota = Car(False, 2, True)

print("START")
print(toyota.get_gas_level())

print("Alimentam 50 litri")
toyota.refill(50)



# vw.drive(100)

# print(vw.get_gas_level())

# vw.refill_full()

# vw.drive(200)

# print(vw.get_gas_level())

# vw.refill()