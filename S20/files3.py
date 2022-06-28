try:
    f_out = open("ouput.txt", "w")
except OSError:
    print("Nu pot deschide fisierul.")

for i in range(100):
    f_out.write(f"NO: {i ** 100}\n")

f_out.close()

f_out.write("END")

