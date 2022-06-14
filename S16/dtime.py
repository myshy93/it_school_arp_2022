# Ora si data curenta?
from datetime import datetime
current_dt = datetime.now()

# Ziua curenta
current_dt.day

# Luna curenta
current_dt.month

# Anul curent
current_dt.year

# Ora curenta
print("Ora:", current_dt.hour)

# Minute si secunde
print("Minut:", current_dt.minute)
print("Secunda", current_dt.second)