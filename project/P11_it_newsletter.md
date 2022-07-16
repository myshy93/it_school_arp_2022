## IT Newsletter


### Interfata:
CLI


### Argumente
Vreau sa pot executa scriptul in 2 moduri.
    a. Gestinoare adrese
    `it_newsletter.py user -a test@test.com` = adauga adresa in BD
    `it_newsletter.py user -d test@test.com` = sterge adresa din BD
    b. Trimitere newsletter
    `it_newsletter.py send` = trimite email catre toti abonatii




### Cerinte

1. Vreau sa trimit email-uri catre o lista de abonati.
2. Lista de abonati este extrasa dintr-o baza de date.
3. Vreau sa am posibilitatea de a adauga o adresa noua de email in baza de date.
4. Vreau sa pot sterge o adresa de email din baza de date
5. Email-ul trimis contine cele mai noi stiri din domeniul IT din toata lumea.
6. Se trimit maxim 10 stiri.
7. Continul email-ului trebuie sa fie de forma:

```
Titlul stire
Scurta descriere a stirii
Link catre stire

Titlul stire
Scurta descriere a stirii
Link catre stire

Titlul stire
Scurta descriere a stirii
Link catre stire

...
```
8. Stirile se extrag la fiecare executie dintr-un API.
9. API: https://newsapi.org/
10. Configuratia (parole, email, etc) este stocata intr-un fisier .ini si este citita la executie.
11. Se foloseste un cont de GMAIL pentru trimitere.
12. Pentru fiecare adresa de email din BD se retine cate emailuri au fost trimise care ea.



### Cerinte non-functionale
1. Logging
2. Trebuie folosit modulul argparse, pt. argumente
3. Tratarea erorilor cu strictete.
4. SQLite ca baza de date.