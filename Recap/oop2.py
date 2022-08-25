import csv
from datetime import datetime
import pathlib
from random import randint, sample
import logging
import sys
from time import sleep



logging.basicConfig(
    filename="log.log",
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s"
    )


class Card:

    def __init__(self, number, owner, exp_month, exp_year, ccv, issuer) -> None:
        self.number = number
        self.owner = owner
        self.expire_month = exp_month
        self.expire_year = exp_year
        self.ccv = ccv
        self.issuer = issuer

    def __str__(self):
        return f"<{self.__class__.__name__} issuer={self.issuer} number={self.number} owner={self.owner}>"

    def __repr__(self):
        return self.__str__()

    def check_number(self):
        pass

    def check_valid(self):
        now = datetime.now()

        if not self.check_number():
            raise Exception("Card number is not valid for this bank.")

        if self.expire_year < now.year:
            return False
        
        if self.expire_month < now.month:
            return False

        return True

class CardIng(Card):

    def __init__(self, number, owner, exp_month, exp_year, ccv) -> None:
        super().__init__(number, owner, exp_month, exp_year, ccv, "Ing")

    def check_number(self):
        if str(self.number).startswith("38"):
            return True
        return False


class CardIngBasic(CardIng):

    def __init__(self, number, owner) -> None:

        super().__init__(number, owner, 12, 2030, randint(100, 999))

class CardRevolut(Card):

    def __init__(self, number, owner, exp_month, exp_year, ccv) -> None:
        super().__init__(number, owner, exp_month, exp_year, ccv, "Revolut")

    def check_number(self):
        if str(self.number).startswith("39") and len(str(self.number)) == 10:
            return True
        return False

class CardRevolutBasic(CardRevolut):

    def __init__(self, owner) -> None:

        super().__init__(f"32{''.join(sample('0123456789', 8))}", owner, 12, 2022, randint(100, 999))

# order_quantity = 100
# order_card_type = "CardRevolutBasic"
# empl_file_path = pathlib.Path("salarii.csv")
# names = []
# cards = []
# logging.info("Starting Card making machine....")

# logging.debug(f"Start to process order. Order: {order_card_type} pcs. {order_quantity}")

# logging.debug(f"Opening {empl_file_path.absolute()} to get names list.")
# try:
#     with empl_file_path.open() as fin:
#         reader = csv.reader(fin)
#         for i in reader:
#             names.append(f"{i[0]} {i[1]}")
# except OSError:
#     logging.critical(f"Could not open {empl_file_path.absolute()}. Exiting...")
#     sys.exit(1)
# else:
#     logging.info(f"Read {len(names)} names from file {empl_file_path.absolute()}.")

# logging.info("Start creating cards...")
# for i in names:
#     logging.info(f"Creating card for {i}.")
#     sleep(0.3)
#     card = CardRevolutBasic(i)
#     cards.append(card)
#     logging.info("Card created.")
#     logging.debug(f"Card info {card}")

# logging.info(f"Created {len(cards)} cards.")
# logging.info("Job successful. Exiting..")

card1  = CardRevolutBasic("ion")

try:
    card1.check_valid()
except Exception as err:
    logging.error(err)