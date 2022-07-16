## Inchirieri auto - CLI


### Interfata:
CLI

#### Meniu
1. Aduga masina
2. Aduga client
3. Adauga rezervare
4. Vezi rezervari
5. Anuleaza rezervare



### Actiuni:
1. Adauga masina
- vreau sa pot adauga o noua masina in baza de date
- se citeste de la consola:
    - marca
    - model
    - an fabricatie
    - tip caroserie
    - serie sa sasiu
    - nr inmatriculare
- se stocheaza in db

2. Adauga client
- vreau sa pot adauga un nou client in db
- se citeste de la tastatura
    - nume
    - prenume
    - cnp
    - adresa
    - nr tel
    - email

3. Adauga rezervare
- vreau sa pot adauga o rezervare pe o masina pentru o anumita perioada
- masina se alege pe baza de id
- clientul se alege pe baza de id
- perioada se introduce de la tastatura
- rezervarea se salveaza in db
- daca exista o rezervare pe masina aleasa in perioada aleasa, trebuie emisa o erorare


4. Vezi rezervari
- vreau sa pot vedea o lista cu toate rezervarile
- vreau sa pot vedea o lista cu rezervarile pentru o masina, aleasa dupa nr de inmatriculare


5. Anuleaza rezervarea
- vreau sa pot anula (sa o marchez anulata) o rezervare
- deci masina devine disponibila



### Cerinte non-functionale
1. Logging
2. Trebuie folosit modulul argparse, pt. argumente
3. Tratarea erorilor cu strictete.
4. datele sunt stocate intr-o baza de dare SQLite