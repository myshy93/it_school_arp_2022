# Parbrize

## Interfata
CLI

## Argumente
1. calea catre fisierul cu date

## Menu


## Cerinte
Identificarea unui anume tip de parbriz se face in baza:
- an fabricatie
- producator (ex: Audi)
- model ( ex: A5)
- apoi trebuie selectat daca este simplu, daca are senzor, camera, incalzire (aceste optiuni ar trebui 
cumva facute ca sa se poata combina intre ele, un parbriz poate avea doar senzor
 dar si senzor si camera sau senzor, camera si incalzire).
- dupa ce sunt selectate optiunile necesare programul ar trebui sa returneze pretul 
acelui parbriz. Fiecare model de masina, pe baza producatorului, modelului, anului 
de fabricatie si optiunilor de echipare are un eurocod unic (ex: 8558AGNGYVZ).
- aceste eurocoduri eu le am stocate intr-un tabel excel care contine si restul
informatiilor despre masina. (denumire, model...etc)
- putem face si un deviz pt fiecare masina (in deviz trebuie trecute date specifice 
despre masina).
- putem face facturi.(date despre client, nume, prenume, adresa.)