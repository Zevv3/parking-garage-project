from tkinter import Y
import garage
# import ticket

# Build Garage:
# - Name of garage
# - Number of spaces total
# - Ticket cost per time of day:
# -- (1) Weekday business hours
# -- (2) Weekday non-business hours
# -- (3) Weekend any time


def run():

    new_garage = None

    while True and not new_garage:
        response = input("Would you like to build a parking garage? (yes/no) ")
        if response.lower().strip() in ('no', 'n'):
            print("\nFine!")
            break
        elif response.lower().strip() in ('yes', 'y'):
            garage_name = input("\nWhat would you like to name your garage? ")
            parking_spaces_total = int(input("\nHow many spaces would you like your parking garage to have? "))
            while not isinstance(parking_spaces_total, int):
                try:
                    parking_spaces_total = int(input("\nPlease input a numeric entry. "))
                except:
                    parking_spaces_total = int(input("\nPlease input a numeric entry. "))
                finally:
                    continue
            print("\nThank you for building your garage!  It's now open for your customers!")
            new_garage = garage.Garage(garage_name, parking_spaces_total)
    
    while True and new_garage:
        print(f"\nWelcome to {new_garage.garage_name}!")
        
        print(f"\nThere are currently {new_garage.parking_spaces_available} spaces available in our garage.")

        print("""
            \nOptions menu:

            [1] Take Ticket and Park
            [2] Pay Ticket and Leave Garage
            [3] Quit App (....and DESTROY this garage!!)

        """)

        response = input("\nPlease choose from the options above: ")

        if response.strip() == "1":
            if new_garage.tickets_available > 0:
                new_garage.take_ticket()
                print(f"\nYour ticket id is: {new_garage.tickets[-1]['ticket_id']}.  Please remember this id as you will need it when you pay to leave the garage.")
            else:
                print("\nWe apologize, there are currently no available tickets left for parking in our garage!  Please wait for someone to exit and try again.")

        # elif response.strip() == "2":
        #     new_garage.park_in_available_space()
        elif response.strip() == "2":
            new_garage.pay_for_parking()
        elif response.strip() == "3":
            if not new_garage.check_ticket():
                print(f"\nPlease visit us again! ... after we rebuild this garage that was just destroyed!!")
                break
            else:
                print("\nYou currently have an unpaid ticket. Please pay your ticket first!")
        else:
            print("\nInvalid entry, please choose one of the options provided.")   
            
            
        # options menu 
        # enter garage if spaces available
        # check spaces available
        # enter/take ticket
        # options to park or just leave - decrement spaces available if parking
        # 
        # pay ticket - leave garage
        
        # 
run()