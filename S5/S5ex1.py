# 1. Scrieti o functie care verifica daca unu nr este par.
# Daca este par returneaza True, altfel False. Functia are un singur argument.

def is_even(n):
    """Check if number is even."""
    if n % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    if is_even(i):
        print(i, "este par")
    else:
        print(i, "este impar")