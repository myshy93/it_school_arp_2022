import pathlib
import sqlite3


ROOT = pathlib.Path(__file__).parent
DB_FILE = ROOT.joinpath("dev.db")

# 1. conecatarea la baze de date
con = sqlite3.connect(DB_FILE)

# 2. Creare cursor
cur = con.cursor()

# 3. Compunere QUERY (interogare baza de date)

# Creare tabel
cur.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    phone TEXT NOT NULL UNIQUE
)
""")

# Insert
cur.execute("""
INSERT INTO contacts (first_name, last_name, phone)
VALUES
("Andrei", "Mihalcea", "0873744787"),
("Ionut", "Mincu", "0738384839")
""")



# 4. Commit - executarea QUERY
con.commit()