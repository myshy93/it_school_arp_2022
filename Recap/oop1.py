from datetime import datetime

card_number = 38438348438
card_owner = "Ionut"
card_expire_month = 8
card_expire_year = 2023
card_ccv = 345
card_issuer = "Ing"

card1_number = 3464382950353
card1_owner = "Andrei"
card1_expire_month = 9
card1_expire_year = 2021
card1_ccv = 345
card1_issuer = "Ing"


def check_valid(expire_month, expire_year, cn):
    now = datetime.now()

    if not check_card_number(cn):
        return False

    if expire_year < now.year:
        return False
    
    if expire_month < now.month:
        return False

    return True

def check_card_number(cn):
    if str(cn).startswith("38"):
        return True
    return False




print(check_valid(card_expire_month, card_expire_year, card_number))
print(check_valid(card1_expire_month, card1_expire_year, card_number))