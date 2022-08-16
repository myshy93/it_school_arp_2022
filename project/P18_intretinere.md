## Liste intretinere - CLI


### Interfata:
CLI

#### Meniu
1. Adauga bloc
2. Adauga apartament
3. Editeaza apartament
4. Adauga contract
5. Editeaza contract
6. Adauga index apa rece
7. Print raport

### Tabele db
- contracte
- blocuri
- ap
- index apa


### Actiuni
#### Adauga bloc
- trebuie creat un tabel in baza de date cu urmatoarele coloane
    - id
    - adresa
    - nume_presedinte

- se citesc de la tastatura toate informatiile necesare
- se salveaza in baza de date

#### Adauga apartament
- trebuie creat un tabel in baza de date cu urmatoarele coloane
    - id
    - nr_ap
    - nume_proprietar
    - nr_locatari
    - nr_camere
    - id_bloc FK

#### Editeaza apartament
- trebuie sa poti actualiza
 - nume_propietar
 - nr_locatari


#### Adauga contract
- trebuie sa poti adauga un contract de utilitati, intr-un tabel cu urm. col.
    - id
    - firma
    - valoare pe luna
    - id_bloc FK

#### Editeaza contract
- trebuie sa poti actualiza valoarea contactului


#### Adauga index apa rece
- alegi dintr-o lista de blocuri un bloc, apoi alegi ap.
- introduci index apa rece
- datele se salveaza intr-un tabel cu col.
    - id
    - data citire
    - index
    - id_ap FK

#### Print raport
- genereaza PDF cu tabel-ul ca trebui afisat la avizier
- coloane
    - nr ap
    - persoane
    - cunsum apa rece
    - valoare apa rece
    - plus cate o coloana pentru fiecare contract in blocul respectiv
    - totalul per ap