# context manager
try:
    with open("google_logo1.png", "rb") as f_in:
        content = f_in.read()
except OSError as err:
    print(err)
else:
    print(content)

print("End")