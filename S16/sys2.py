import sys
# argumente

# print(sys.argv[0]) # numele executabilului

name = None
rep = 10

def show_help():
    print("""Usage: script_name.py NAME [REPS]

NAME = nume de afisat
REPS = de cate ori sa afiseze, default 10

Optiuni:
    -h = Arata acest help
""")
    sys.exit(1)

if len(sys.argv) > 1:
    if sys.argv[1] == "-h":
        show_help()
    name = sys.argv[1]
else:
    show_help()

if len(sys.argv) > 2:
    rep = int(sys.argv[2])

for i in range(rep):
    print(name)
