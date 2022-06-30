import pathlib
import xml.etree.ElementTree as ET
import sys

root = pathlib.Path(__file__).parent
files_dir = root.joinpath("files")
contacts_file = files_dir.joinpath("contacts.xml")


class Contact:
    def __init__(self, firs_name, last_name, phone):
        self.first_name = firs_name
        self.last_name = last_name
        self.phone = phone

    def show(self):
        print("=" * 50)
        print(f"Contact: {self.first_name} {self.last_name}")
        print(f"Tel: {self.phone}")
        print("=" * 50)


class PhoneBook:
    def __init__(self) -> None:
        self.contacts = []

    def add(self, contact):
        self.contacts.append(contact)

    def __len__(self):
        return len(self.contacts)


# verficam existenta fisierului
if not contacts_file.is_file():
    print("Error! Contacts file not found.")
    sys.exit(1)

book = PhoneBook()

# parsam xml

# 1. gasim elementul root
xml_root = ET.parse(contacts_file)

# 2. luam lista de elemente de interes
for pers in xml_root.iter("person"):
    contact = Contact(
        pers.findtext("first_name"),
        pers.findtext("last_name"),
        pers.findtext("phone")
    )
    book.add(contact)

for i in book.contacts:
    i.show()