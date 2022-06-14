import time
from datetime import datetime

while True:
    # suspenda executia pentru o secunda
    time.sleep(1)
    if datetime.now().second == 5:
        print("Jumatate de minut!")