## Rapoarte/Grafice criptomonede - CLI


### Interfata:
CLI

#### Argumente
Oblicatorii:
1. Simbol criptomoneda
2. Data start

Optionale:
1. Data stop -> default data curenta


### Cerinte:

1. Vreau sa obtin un raport grafic cu evolutia in raport cu EURO a unei criptomonede pe o perioda finita.
2. Alaturi de grafic vreau sa vad si data gand a fost generat.
3. Vreu sa mai am in raport: 
- totalul tranzationat in perioada aleasa
- numarul tranzactiilor
4. Raportul trebuie generat in 2 formate:
 - pdf
 - png

### Cerinte non-functionale
1. Logging
2. Trebuie folosit modulul argparse, pt. argumente
3. Tratarea erorilor cu strictete.