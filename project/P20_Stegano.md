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