import os

# citeste ultimi 10 bytes
file_descriptor = open('/Users/mihai/dev/it_school/S20/practice.txt')

file_descriptor.seek(0, os.SEEK_END)
end = file_descriptor.tell()

file_descriptor.seek(end - 10, os.SEEK_SET)

print(file_descriptor.read())

file_descriptor.close()