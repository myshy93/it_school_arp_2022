
class Pen:

    #atribut de clasa
    brand = 'NOKI'

    def __init__(self, color):
        self.color = color
        self.is_empty = False


pen = Pen('red')
pen2 = Pen('black')

print(pen.brand)
print(pen2.brand)

# pen2.owner = "Mihai"

# print(pen2.owner)
pen2.brand = "pen2-brand" # creaza un atribut de instanta pt ca nu are voie sa modifice atributul static

Pen.brand = "test"
print(Pen.brand)

# print(pen.brand)
# print(pen2.brand)

# print(pen.color)
# print(pen2.color)



