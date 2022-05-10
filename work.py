import random
random_number = random.randint(1, 100)


def get_proximity_mesage(number, anchor):
    """Get coresponding message based on how far +/-
    you are from anchor number."""
    offset_msg_map = {
        2: "Arde",
        5: "Frige",
        10: "Cald",
        20: "Caldut",
        30: "Rece",
        40: "Frig",
        50: "Gheata",
    }
    for k, v in offset_msg_map.items():
        if anchor in range(number - k, number + k):
            return v
    return "Tinutul inghtat"

user_number = -1

print("Incepe jocul!")
print("Introduceti un numar intre 1 si 299.")

while user_number != random_number:
    user_number = int(input())
    print(get_proximity_mesage(user_number, random_number))

print("Felicitari!")
print("Ai ghicit numarul:", random_number)