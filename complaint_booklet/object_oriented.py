from datetime import datetime

class Complaint:

    __next_id = 0

    def __init__(self, name, text) -> None:
        self.name = name
        self.text = text
        self.date = datetime.now()
        self.resolved = False
        self.id = Complaint.get_next_id()

    @staticmethod
    def get_next_id():
        c_id = Complaint.__next_id
        Complaint.__next_id += 1
        return c_id

    def resolve(self):
        self.resolved = True

    def print(self):
        print(f"{self.date:*^50}")
        print(f"ID: {self.id}")
        print(f"Reclamant: {self.name}")
        print("Text reclamatie:")
        print(self.text)
        print(f"{self.date:*^50}\n")

    def __repr__(self) -> str:
        return f"<Complaint {self.id} by {self.name}>"


class Booklet:

    def __init__(self) -> None:
        self.__complaints = []
        
    def add_complaint(self, complaint):
        self.__complaints.append(complaint)

    def get_unresolved_complaints(self):
        return self.__complaints

    def get_all_complaints(self):
        unres = []
        for i in self.__complaints:
            if not i.resolved:
                unres.append(i)
        return unres

    def resolve_complaint(self, id):
        for i in self.__complaints:
            if i.id == id:
                i.resolve()
    


def add_complaint_flow():
    print_banner("Adauga plangere.")

    name = input("Nume: ")
    complaint_text = input("Text plangere: ")

    complaint_id = add_complaint(name, complaint_text)

    print_message("Reclamatie adaugata! Numar:", complaint_id)

    ret_to_main_menu_prompt()


def view_not_done_complaints_flow():
    print_banner("Vezi reclamatiile nerezolvate.")

    complaints = get_complaints_not_done()

    if len(complaints) == 0:
        print_message("Nici o reclamatie noua.")

    for i in complaints:
        print_complaint(i["id"], i["name"], i["text"], i["date"])

    ret_to_main_menu_prompt()


def mark_as_done_flow():
    print_banner("Rezolva reclamatii.")
    _id = input("\nID plangere:")

    if _id.isnumeric() and mark_as_done(int(_id)):
        print_message("Reclamatia cu ID:", _id, "rezolvata.")
    else:
        print_message("Reclamatia cu ID:", _id, "nu a fost gasita.")

    ret_to_main_menu_prompt()


def get_main_menu_choice():
    """Show main menu items asking the user for a choice.
    Returns the function to call next based on user choice.
    """
    choice_ok = False
    m_menu_entries = {
        1: {"text": "Adauga reclamatie.", "f": add_complaint_flow},
        2: {"text": "Vezi reclamatiile.", "f": view_not_done_complaints_flow},
        3: {"text": "Rezolva reclamatii.", "f": mark_as_done_flow},
        0: {"text": "Inchide program.", "f": sys.exit},
    }

    while not choice_ok:
        for k, v in m_menu_entries.items():
            print(k, ". ", v["text"], sep="")
        choice = input("\nAlege un numar: ")
        if not choice.isnumeric() or int(choice) not in m_menu_entries.keys():
            cls()
            print("EROARE: Te rog sa alegi un numar din lista de mai jos.\n\n")
        else:
            choice_ok = True

    return m_menu_entries[int(choice)]["f"]


def main():
    while True:
        print_banner(sw_name)
        current_flow = get_main_menu_choice()
        # call user choice flow
        current_flow()


if __name__ == "__main__":
    main()
