# Create a class Flight
# - flight_number (number)
# - destination (string)
# - deaprture_time (timestamp)
# - passengers (array)
class Flight:
    def __init__(self, flight_number, destination, departure_time):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.passengers = []

    
# add_passenger method - flight_number, name, seat_number
# display_passengers method
# find_passenger method

# Create a class Passenger
# - name
# - seat_number
class Passenger:
    def __init__(self, name, seat_number):
        self.name = name
        self.seat_number = seat_number

# Menu driven program with these options : 
# 1. Add Flight
# 2. Add Passenger to Flight
# 3. Display Passengers in a Flight
# 4. View Bookings
# 5. Book a Flight
# 6. Cancel Booking
# 7. Exit

def main_airport_management():
    flights = []
    
    while True:
        print("\nAirport Management Menu : ")
        print("1. Add Flight")
        print("2. Add Passenger to Flight")
        print("3. Display Passengers in a Flight")
        print("4. View Bookings")
        print("5. Book a Flight")
        print("6. Cancel Booking")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7) : ")
        
        if choice=='1':
            flight_number = input("Enter the flight number : ")
            destination = input("Enter the destination : ")
            departure_time = input("Enter the departure time : ")
            new_flight = Flight(flight_number, destination, departure_time)
            flights.append(new_flight)
            print(f"Flight {flight_number} to {destination} added!")
            
        elif choice=='2':
            print("\nOption 2 selected!")
            
        elif choice=='3':
            print("\nOption 3 selected!")
            
        elif choice=='4':
            print("\nOption 4 selected!")
            
        elif choice=='5':
            print("\nOption 5 selected!")
            
        elif choice=='6':
            print("\nOption 6 selected!")
            
        elif choice=='7':
            print("\nOption 7 selected!")
            break
        
        else:
            print("\nInvalid choice!")
            
    
if __name__ == "__main__":
    main_airport_management()
    
    
        
       


