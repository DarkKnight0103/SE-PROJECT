import datetime
import re

class StadiumSeatBookingSystem:
    def __init__(self):
        self.logged_in = False
        self.events = []
        self.users = [{'email': 'shiv@gmail.com', 'password': 'Shiv@103'}]

    def create_account(self):
        # email = input("Enter your email address: ")
        # password = input("Enter your password: ")
        
        email = input("Enter your email address: ")
        # check if email is already registered
        for user in self.users:
            if user['email'] == email:
                print("Email already registered.")
                return

        # check if email is valid
        if not self.is_valid_email(email):
            print("Invalid email address.")
            self.create_account()
            
        
        password = input("Enter your password: ")    
        # check if password is valid
        if not self.is_valid_password(password):
            print("Invalid password.")
            self.create_account()

        self.users.append({'email': email, 'password': password})
        print("Account created successfully.")
        
    def is_valid_email(self, email):
        # check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        return True

    def is_valid_password(self, password):
        # check if password is at least 8 characters long and contains at least one uppercase letter, one lowercase letter, and one number
        if not re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password):
            return False
        return True

    def display_user_list(self):
        if len(self.users) == 0:
            print("No users registered.")
            return
        else:
            print("List of users:")
            for user in self.users:
                print(user['email'])
        
    def login(self):
        # assume users are identified by their email addresses
        if self.logged_in:
            print("You are already logged in.")
            return
        elif len(self.users) == 0:
            print("No users registered.")
            print("Create a new user:")
            StadiumSeatBookingSystem.create_account(self)
            return
        else:
            email = input("Enter your email address: ")
            password = input("Enter your password: ")

        # check if email is valid
        if not self.is_valid_email(email):
            print("Invalid email address.")
            return

        # check if password is valid
        if not self.is_valid_password(password):
            print("Invalid password.")
            return

        # check if user is registered
        for user in self.users:
            if user['email'] == email and user['password'] == password:
                self.logged_in = True
                print("Login successful!")
                return

        # if user is not found or password is incorrect
        print("Invalid email or password.")

    def display_event_list(self):
        if not self.logged_in:
            print("Please log in to continue.")
            return

        print("List of events:")
        for i, event in enumerate(self.events):
            print(f"{i+1}. {event['name']}, {event['date']}, {event['location']}, {len(event['seats'])} seats available")

    def add_event(self):
        if not self.logged_in:
            print("Please log in to continue.")
            return

        name = input("Enter event name: ")
        date = input("Enter event date: ")
        location = input("Enter event location: ")
        num_seats = int(input("Enter number of seats: "))

        seats = []
        for i in range(num_seats):
            seats.append({'id': i+1, 'booked': False})

        self.events.append({'name': name, 'date': date, 'location': location, 'seats': seats})
        print("Event added successfully.")

    def remove_event(self):
        if not self.logged_in:
            print("Please log in to continue.")
            return

        event_index = int(input("Enter the index of the event to remove: ")) - 1
        if 0 <= event_index < len(self.events):
            self.events.pop(event_index)
            print("Event removed successfully.")
        else:
            print("Invalid event index.")

    def edit_event_details(self):
        if not self.logged_in:
            print("Please log in to continue.")
            return

        event_index = int(input("Enter the index of the event to edit: ")) - 1
        if 0 <= event_index < len(self.events):
            event = self.events[event_index]
            name = input(f"Enter new name for {event['name']}: ")
            date = input(f"Enter new date for {event['date']}: ")
            location = input(f"Enter new location for {event['location']}: ")
            self.events[event_index] = {'name': name, 'date': date, 'location': location, 'seats': event['seats']}
            print("Event details updated successfully.")
        else:
            print("Invalid event index.")

    def select_seat(self):
        if not self.logged_in:
            print("Please log in to continue.")
            return
        
        
        event_index = int(input("Enter the index of the event to book a seat for: ")) - 1
        if 0 <= event_index < len(self.events):
            event = self.events[event_index]
            available_seats = [seat['id'] for seat in event['seats'] if not seat['booked']]
            if available_seats:
                print(f"Available seats for {event['name']}: {available_seats}")
                seat_id = int(input("Enter the seat number to book: "))
                if seat_id in available_seats:
                    seat_index = seat_id - 1
                    event['seats'][seat_index]['booked'] = True
                    print("Seat booked successfully.")
                else:
                    print("Invalid seat number.")
            else:
                print("No seats available.")
        else:
            print("Invalid event index.")
    
        print("----------------------------Seat receipt------------------------------")
        print("Event name: ", self.events[event_index]['name'])
        print("Event date: ", self.events[event_index]['date'])
        print("Event location: ", self.events[event_index]['location'])
        print("Seat number: ", seat_id)
        print("Booking Date: ", datetime.date.today())
        print("Booking Timing: ", datetime.datetime.now())
        print("---------------------------------------------------------------------")
            
def main():
    # create an instance of the StadiumSeatBookingSystem class
    booking_system = StadiumSeatBookingSystem()
    print("1. User")
    print("2. Event Manager")
    print("0. Exit")
    a= int(input("Select Your Role:"))
    if a==1:
        while True:
            print("\nStadium Seat Booking System")
            print("--------------------------")
            print("1. Login")
            print("2. Display event list")
            print("3. Select seat")
          # print("4. Create account")
            print("0. Go Back To Role Selection")
            
            choice1 = (input("Enter your choice: "))
            
            if choice1 == "1":
                booking_system.login()
            elif choice1 == "2":
                booking_system.display_event_list()
            elif choice1 == "3":
                booking_system.select_seat()
            # elif choice == "4":
            #     booking_system.create_account()
            elif choice1 == "0":
                main()
            else:
                print("Invalid choice. Please try again.")
    elif a==2:            
            while True:
                print("\nStadium Seat Booking System")
                print("--------------------------")
                print("1. Login")
                print("2. Display event list")
                print("3. Add event")
                print("4. Remove event")
                print("5. Edit event details")
                print("6. Select seat")
                print("7. Display user list")
                # print("8. Create account")
                print("0. Go Back to Role Selection")

                choice2 = (input("Enter your choice: "))

                if choice2 == "1":
                    booking_system.login()
                elif choice2 == "2":
                    booking_system.display_event_list()
                elif choice2 == "3":
                    booking_system.add_event()
                elif choice2 == "4":
                    booking_system.remove_event()
                elif choice2 == "5":
                    booking_system.edit_event_details()
                elif choice2 == "6":
                    booking_system.select_seat()
                elif choice2 == "7":
                    booking_system.display_user_list()
                # elif choice == "8":
                #     booking_system.create_account()
                elif choice2 == "0":
                    main()
                else:
                    print("Invalid choice. Please try again.")
    elif a==0:
        print("Thank you for using the Stadium Seat Booking System!")
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

if __name__ == "__main__":
    main()  