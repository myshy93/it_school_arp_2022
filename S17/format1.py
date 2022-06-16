from datetime import datetime


toy = "car"
# %s -> aici vine un string
new_string = "This is a %s" % toy

first_name = "Mihai"
last_name = "Dinu"
age = 20

print("Prenume: %s | Nume: %s | Varsta: %d" % (last_name, first_name, age))


class Client:

    def __init__(self, name, address, iban) -> None:
        self.name = name
        self.address = address
        self.iban = iban


class Invoice:

    def __init__(self, client) -> None:
        self.client = client

    def print_invoice(self, title):
        print("{:*^50}".format(title))
        print("Nume client: {:>37}".format(self.client.name))
        print("Adresa: {:>42}".format(self.client.address))
        print("IBAN: {:>44.13}".format(self.client.iban))
        print("{:=^50}".format(str(datetime.now())))
        print()

client = Client("George Pascu", "Bucuresti", "RO76INGB00000000")
client1 = Client("Ion Pascu", "Iasi", "RO76INGB000000124300")

invoice1 = Invoice(client)
invoice2 = Invoice(client1)

invoice1.print_invoice("Factura")
invoice2.print_invoice("Invoice")