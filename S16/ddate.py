from dataclasses import dataclass
from datetime import datetime

# formatare ora
print(datetime.now().strftime("%H:%M:%S"))

# formatare data
print(datetime.now().strftime("%d/%b/%y")) # 14/Jun/22

# 08/29/1993
b_day = datetime(1993, 8, 29)

print(b_day.strftime("%m/%d/%Y"))

