import argparse
import logging
from deck import Deck


parser = argparse.ArgumentParser()
parser.add_argument("N", help="how many cards to extract", type=int)
# parser.add_argument("-s", action="store_true", help="Shuffle if set")
parser.add_argument("-s", "--shuffle", help="Shuffle for n times", default=0, type=int)
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
deck = Deck()

# in-line if
# daca true if conditie else daca false
# adult = "da" if varsta >= 18 else "NU"

for _ in range(args.shuffle):
    logging.debug("Shuffle the deck")
    deck.shuffle()

logging.info("Here are your cards:")
for i in deck.get_cards(args.N):
    print(i)