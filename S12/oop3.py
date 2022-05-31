from auto import Car


ford = Car(4, False, False)
vw = Car(2, True, False)
toyota = Car(4, False, True)

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