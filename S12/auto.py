class Car:

    # constructor
    def __init__(self, doors, transmission, awd):  # dunderscore methods | magic methods
        print("---Constructor apelat---")
        # definire atribute
        # self.xxxxxxx = yyyyyyy

        # modificator de access
        # _xxxx -> protected
        # __xxxxxx -> private


        # private
        # public attribute
        self.__km = 0
        self.__doors = doors
        self.__transmission = transmission  # sau manual
        self.__awd = awd  # AWD = all wheel drive = 4x4
        self.__gas_per = 0
        self.__wipers = False

    # definire metode
    def horn(self):
        print("titititiii")

    def describe(self):
        print("Doors:", self.__doors)
        print("Transmission:", self.__transmission)
        print("AWD:", self.__awd)

    def get_gas(self):
        return self.__gas_per

    def refill(self, g_p):
        if 0 <= g_p <= 100 and g_p > self.__gas_per:
            self.__gas_per = g_p

    def refill_full(self):
        self.refill(100)

    def turn_on_wipers(self):
        self.__wipers = True

    def turn_off_wipers(self):
        self.__wipers = False

    def __del__(self):
        # destructor
        print("Obiect sters")
