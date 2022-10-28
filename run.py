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
    while True:
        response = input("Would you like to build a parking garage? (yes/no) ")
        if response.lower().strip() in ('no', 'n'):
            print("Fine!")
            break
        elif response.lower().strip() in ('yes', 'y'):
            garage_name = input("What would you like to name your garage? ")
            parking_spaces_total = int(input("How many spaces would you like your parking garage to have? "))
            while not isinstance(parking_spaces_total, int):
                try:
                    parking_spaces_total = int(input("Please input a numeric entry. "))
                except:
                    parking_spaces_total = int(input("Please input a numeric entry. "))
                finally:
                    continue
            print("Thank you for building your garage!  It's now open for your customers!")
            new_garage = garage.Garage(garage_name, parking_spaces_total)
            break
        else:
            print("Invalid entry, please choose one of the options provided.")
            continue
    
    while True:
        print(f"\nWelcome to {new_garage.garage_name}!")

        
        print(f"There are currently {new_garage.parking_spaces_available} spaces available in our garage.")

        print("""
            Options menu:

            [1] Take Ticket
            [2] Park Car
            [3] Pay Ticket
            [4] Exit Space
            [5] Leave Garage

        """)

        response = input("\nPlease choose from the options above: ")

        if response.strip() == "1":
            if new_garage.tickets_available > 0:
                new_garage.take_ticket()
                print(f"new_garage.tickets[-1]: {new_garage.tickets[-1]}")
                print(f"Your ticket id is: {new_garage.tickets[-1]['ticket_id']}.  Please remember this id as you will need it when you pay to leave the garage.")
            else:
                print("We apologize, there are currently no available spaces left in our garage!  Please wait for someone to exit and try again.")

                
           

        
        elif response.strip() == "2":
            new_garage.park_in_available_space()

        elif response.strip() == "4":
            new_garage.exit_parking_space()

        elif response.strip() == "3":
            new_garage.pay_for_parking()

        elif response.strip() == "5":
            new_garage.leave_garage()
            break
        else:
            print("Invalid entry, please choose one of the options provided.")   
            
            
        # options menu 
        # enter garage if spaces available
        # check spaces available
        # enter/take ticket
        # options to park or just leave - decrement spaces available if parking
        # 
        # pay ticket - leave garage
        
        # 
run()
