import csv
import pathlib

root = pathlib.Path(__file__).parent
files_path = root.joinpath("files")

# # citire fisier csv
lista_salarii = []
try:
    with open(files_path.joinpath("salarii.csv")) as fin:
        reader = list(csv.reader(fin)) # csv.reader returneaza un generator, trebuie convertit la lista
        for i in reader:
            lista_salarii.append(float(i[3]))
except OSError:
    print("File error.")

print(f"Total salarii: {sum(lista_salarii)}")

# citire fisier csv cu nume campuri
field_names = [
    "first_name",
    "last_name",
    "id",
    "gros_salary",
    "days_off"
]
try:
    with open(files_path.joinpath("salarii.csv")) as fin:
        # list -> extrage datele din generator
        dict_reader = csv.DictReader(fin, fieldnames=field_names)
        for i in dict_reader:
            lista_salarii.append(float(i['gros_salary']))
except OSError:
    print("File error.")

print(sum(lista_salarii))

# scriere csv
try:
    with open(files_path.joinpath("net_salaries.csv"), "w") as fout:
        csv_writer = csv.writer(fout, lineterminator="\n")
        for i in reader:
            net = float(i[3]) * 0.65
            csv_writer.writerow([i[0], i[1], f"{net:.2f}"])
except OSError:
    print("File write error.")

# # csv.DictWriter - get a dict for each line