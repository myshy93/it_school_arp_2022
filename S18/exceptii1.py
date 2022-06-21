from math import pi
from datetime import datetime

def circle_area(radius):
    """Calculaeaza aria cercului, doar pentru numere pozitive.

    Args:
        * radius int of float: Raza cercului.
    
    Returns:
        float: Aria cercului

    Raises:
        * ValueError: Daca radius este numar negativ.
        * TypeError: Daca radius nu este numar.
    """
    if isinstance(radius, float) or isinstance(radius, int):
        if radius < 0:
            raise ValueError("Nu pot calcula aria pentru un numar negativ.")
        return pi * radius ** 2
    else:
        raise TypeError("Nu pot calcula aria pentru parametru introdus.") # se creeaza on obj nou de tip exceptie

def cylinder_volume(radius, height):
    """Description
    
    Raises:
        * see circle_area
    """
    return circle_area(radius) * height

# height = int(input("Inaltime: "))
# radius = int(input("Raza: "))
# print(f"Volum cilindru: {cylinder_volume(radius, height)}")

# print(circle_area(None))
# print(circle_area("!@#$"))

# try:
#     print(circle_area(-3))
#     print(circle_area(10)) # nu se executa daca ai exceptie
# except (ValueError, TypeError) as err:
#     print(f"{datetime.now()} [ERROR] {err}")

# print(circle_area(2.3))

l1 = [2.3, "re", None, 4, 10, -2, 33]

# for i in l1:
#     try:
#         print(circle_area(i))
#     except TypeError as err:
#         print(f"{datetime.now()} [ERROR] {err}")
#     except ValueError as err:
#         print(f"{datetime.now()} [WARNING] {err}")


# try:
#     print(circle_area(-2))
# except (TypeError, ValueError) as err:
#     print(err)
# finally:
#     print("Closing database connection...")

try:
    vol = cylinder_volume("sdd", 10)
except (TypeError, ValueError) as err:
    print(err)
else:
    try:
        print("Calcul cu success.")
        print(vol)
        open("./tests.pt")
    except OSError as err:
        print(err)


# print(circle_area({}))
# print(circle_area([]))
# print(circle_area(()))
# print(circle_area(print))
