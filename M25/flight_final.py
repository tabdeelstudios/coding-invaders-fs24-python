class Flight:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []

    def add_passenger(self, passenger):
        self.passengers.append(passenger)
        print(f"Passenger {passenger.name} added to Flight {self.flight_number}.")

    def display_passengers(self):
        if not self.passengers:
            print("No passengers on this flight.")
        else:
            print(f"Passengers on Flight {self.flight_number}:")
            for passenger in self.passengers:
                print(passenger.name)

    def find_passenger(self, passenger_name):
        return next((passenger for passenger in self.passengers if passenger.name == passenger_name), None)

class Passenger:
    def __init__(self, name, seat_number):
        self.name = name
        self.seat_number = seat_number

def main_airport_management():
    flights = []

    while True:
        print("\nAirport Management Menu:")
        print("1. Add Flight")
        print("2. Add Passenger to Flight")
        print("3. Display Passengers in Flight")
        print("4. View Bookings")
        print("5. Book a Flight")
        print("6. Cancel Booking")
        print("7. Quit")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            flight_number = input("Enter the flight number: ")
            destination = input("Enter the destination: ")
            departure_time = input("Enter the departure time: ")
            new_flight = Flight(flight_number, destination, departure_time)
            flights.append(new_flight)
            print(f"Flight {flight_number} to {destination} added.")

        elif choice == '2':
            if not flights:
                print("No flights available. Please add a flight first.")
            else:
                flight_number = input("Enter the flight number: ")
                passenger_name = input("Enter the passenger's name: ")
                seat_number = input("Enter the seat number: ")
                passenger = Passenger(passenger_name, seat_number)

                found_flight = next((flight for flight in flights if flight.flight_number == flight_number), None)
                if found_flight:
                    found_flight.add_passenger(passenger)
                else:
                    print(f"Flight {flight_number} not found.")

        elif choice == '3':
            if not flights:
                print("No flights available.")
            else:
                flight_number = input("Enter the flight number: ")
                found_flight = next((flight for flight in flights if flight.flight_number == flight_number), None)
                if found_flight:
                    found_flight.display_passengers()
                else:
                    print(f"Flight {flight_number} not found.")

        elif choice == '4':
            print("Bookings:")
            for flight in flights:
                for passenger in flight.passengers:
                    print(f"Flight {flight.flight_number} - Passenger: {passenger.name}")

        elif choice == '5':
            if not flights:
                print("No flights available.")
            else:
                flight_number = input("Enter the flight number: ")
                found_flight = next((flight for flight in flights if flight.flight_number == flight_number), None)
                if found_flight:
                    passenger_name = input("Enter your name: ")
                    seat_number = input("Enter your preferred seat number: ")
                    passenger = Passenger(passenger_name, seat_number)
                    found_flight.add_passenger(passenger)
                    print(f"Booking successful for {passenger.name} on Flight {found_flight.flight_number}.")
                else:
                    print(f"Flight {flight_number} not found.")

        elif choice == '6':
            if not flights:
                print("No flights available.")
            else:
                passenger_name = input("Enter your name: ")
                for flight in flights:
                    found_passenger = flight.find_passenger(passenger_name)
                    if found_passenger:
                        flight.passengers.remove(found_passenger)
                        print(f"Booking canceled for {found_passenger.name} on Flight {flight.flight_number}.")
                        break
                else:
                    print(f"Passenger {passenger_name} not found in any bookings.")

        elif choice == '7':
            print("Exiting Airport Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main_airport_management()
