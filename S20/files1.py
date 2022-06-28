# TEXT              
# biti pe HD ----> decodare ---> viziualizare
#                    UTF-8

# BINAR
# biti pe HD ----> decodare ----> vizualizare
#                    codec

# Mod de lucru cu text
# w = write
# r = read
# a = append

# Mod de lucru cu binar
# wb = write binary
# rb = read binary
# ab = append binary

# IO = input/output


# SEEK
# din modulul os
# os.SEEK_SET - inceputul fis.
# os.SEEK_CUR - pozitia curenta
# os.SEEK_END - safarsitul fisierului

import os

file_descriptor = open('/Users/mihai/dev/it_school/S20/practice.txt')

# print(type(file_descriptor))
# print(file_descriptor)

# citim poz curenta a cursorului
print(file_descriptor.tell())
print(file_descriptor.read())
print(file_descriptor.tell())


# ne miscam in fisier
# file_descriptor.seek(0, os.SEEK_SET)
print(file_descriptor.read())

# CLOSE THE FILE !!!!!!!!!
file_descriptor.close()

# 1 caracter = 1 byte

# print(f"Fisierul are dimensiunea: {len(content)} bytes")

