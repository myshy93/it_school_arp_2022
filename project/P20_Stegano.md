# Steganografie - API

### Interfata
REST API

### Endoints
#### POST /encrypt
Content type: multipart/form-data
Prin aceasta metoda se trimite imaginea catre server pentru a cripta un mesaj in ea.
Mesajul este trimis in acelasi form-data

#### POST /decrypt
Content type: multipart/form-data
Prin aceasta metoda se trimite imaginea catre server pentru a extrage mesajul din ea.

#### GET /metrics
Returneaza cate imagini a codat/decodat

#### GET /docs
Returneaza documentatia

### Cerinte
1. Metricele sunt retinute intr-o baza de date

### Cerinte non-functionale
1. Logging
2. Trebuie folosit modulul argparse, pt. argumente
3. Tratarea erorilor cu strictete.
4. datele sunt stocate intr-o baza de dare SQLite