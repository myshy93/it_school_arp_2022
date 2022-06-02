from datetime import datetime

calatori = [
    "Otavă Bogdan",
    "Greta Mihaela Geabelea",
    "Iustin Gabriel Manciu",
    "Corina Lungu",
    "Melissa Madalina Haj Abdo",
    "Gabriel Guțui",
    "George Valeanu",
    "Andreea-Simona Telegeanu",
    "Ionuț Alin Preda",
    "Arthur Timbalariu",
    "Cristian Laurentiu Șandor",
    "Alex Raul Bonat-Mihalca",
    "Artsanyo Dennis Kachi",
    "Sergiu Mihai Predel",
    "Marian-Gabriel Tohaneanu-Iatan",
    "Irina Florentina Barbu",
    "Cordos Simona",
]


class AirTrip:
    def __init__(self, depart_airport, arrive_airport, depart_time, 
                arrival_time, price):
        self.__depart_airport = depart_airport
        self.__arrive_airport = arrive_airport
        self.depart_time = depart_time
        self.arrival_time = arrival_time
        self.__price = price

    def get_depart_airport(self):
        return self.__depart_airport

    def get_arrive_airport(self):
        return self.__arrive_airport

    def get_price_tva(self):
        return self.__price + self.__price / 100 * 19


class Ticket:
    def __init__(self, passenger_name, seat, trip):
        self.passenger_name = passenger_name
        self.seat = seat

        # compozitie
        if isinstance(trip, AirTrip):
            self.trip = trip
        else:
            # raise error
            print("EROARE: Nu am primit un obiect de tip AirTrip")

    def print_ticket(self):
        print("+-------------------------+")
        print("Passenger name:", self.passenger_name)
        print("Depart:", self.trip.get_depart_airport(), "-", self.trip.depart_time)
        print("Arrival:", self.trip.get_arrive_airport(), "-", self.trip.arrival_time)
        print()
        print("Seat:", self.seat)
        print("Price (incl. TVA):", self.trip.get_price_tva())
        print("+-------------------------+")

    # scriem o metoda magica
    def __str__(self):
        return f"<Ticket object for {self.passenger_name}>"


d_time = datetime(2022, 6, 2, 12, 30)
a_time = datetime(2022, 6, 2, 13, 10)


trip1 = AirTrip("BUC", "TIM", d_time, a_time, 100)


ticket1 = Ticket("Mihai Dinu", "1A", trip1)

print(ticket1)