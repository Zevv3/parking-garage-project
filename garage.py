# class Garage:


# Your parking gargage class should have the following methods:
# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day"
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!"
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# - Update tickets list to increase by 1 (meaning add to the tickets list)

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

import datetime
from random import choice
import ticket

class Garage:
    def __init__(self, garage_name, parking_spaces_total) -> None:
        self.garage_name = garage_name
        self.parking_spaces_total = parking_spaces_total
        self.tickets = [
            {
                'ticket_id': 0, 
                'ticket_cost': None, 
                'ticket_entry_timestamp': None, 
                'ticket_vehicle_license_plate': None, 
                'ticket_exit_timestamp': None, 
                'ticket_paid_status': None,
            },
        ]
        self.tickets_available = parking_spaces_total - len(self.tickets) + 1
        self.parking_spaces_available = parking_spaces_total - len(self.tickets) + 1
        self.ticket_cost_per_hour = {
            "weekday": {
                "business_hours": 10,
                "non-business-hours": 7, 
            },
            "weekend": {
                "any_time": 5,
            }
        }
        self.current_ticket = {}
        

    def take_ticket(self):
        # instantiate a ticket
        # add to self.tickets list
        # ticket id is the index in self.tickets

        

        day_of_week = datetime.datetime.now().strftime("%a")
        hour_of_day = datetime.datetime.now().strftime("%H")       
        
        ticket_cost = None

        if day_of_week not in ('Sat', 'Sun'):
            if int(hour_of_day) >= 9 and int(hour_of_day) <= 18:
                ticket_cost = self.ticket_cost_per_hour['weekday']['business_hours']
            else:
                ticket_cost = self.ticket_cost_per_hour['weekday']['non-business_hours']
        else:
            ticket_cost = self.ticket_cost_per_hour['weekend']['any_time']

        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI",
          "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI",
          "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC",
          "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
          "VT", "VA", "WA", "WV", "WI", "WY"]

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

        license_plate = choice(states) + ' ' + choice(letters).upper() + choice(letters).upper() + choice(letters).upper() + "-" + str(choice(numbers)) + str(choice(numbers)) + str(choice(numbers))
        if self.tickets_available > 0:
            if self.current_ticket == {}:
                self.tickets_available -= 1
                self.parking_spaces_available -= 1
                self.current_ticket = ticket.Ticket(self.tickets[-1]['ticket_id']+1, ticket_cost, datetime.datetime.now().strftime("%H"), license_plate)
                self.current_ticket = self.current_ticket.make_dict()
                self.tickets.append(self.current_ticket)
                self.current_ticket = {}

            # print(f"after taking ticket: {self.tickets}")

        else:
            print("\nYou already have a ticket!  Please choose another option.")

    def check_ticket(self):
        if self.current_ticket != {}:
            return True
        else:
            return False

    # def park_in_available_space(self):
    #     if self.check_ticket():
    #         if self.parking_spaces_available > 0:
    #             self.parking_spaces_available -= 1
    #             self.current_ticket = {}
    #     else:
    #         print("\nYou can only choose this option after taking a ticket!")

    def pay_for_parking(self):
        # returns True/False
        id = ""
        # Active = True
        while True:
            while not isinstance(id, int):
                try:
                    id = int(input("\nWhat is your ticket id? Or enter 0 to quit pay. "))
                except:
                    id = int(input("\nPlease input a numeric entry. Or enter 0 to quit pay. "))
                finally:
                    continue
            if id == 0:
                break
            elif id < 0:
                print("\nPlease enter a valid ticket id. Or enter 0 to quit pay. ")
                while id < 0:
                    try:
                        id = int(input("\nWhat is your ticket id? Or enter 0 to quit pay. "))
                    except:
                        id = int(input("\nPlease input a numeric entry. Or enter 0 to quit pay. "))
                    finally:
                        continue                
            elif id >= 1:
                ticket_id_exists = False
                while not ticket_id_exists:
                    for ticket in self.tickets:
                        if id == ticket['ticket_id']:
                            ticket_id_exists = True
                            break
                        else:                     
                            ticket_id_exists = False
                    if not ticket_id_exists:
                        print("\nPlease enter a valid ticket id. ")
                        id = ''
                        break
                while ticket_id_exists:
                    for ticket in self.tickets:
                        if id == "":
                            break
                        elif id == ticket['ticket_id']:
                            self.current_ticket = ticket
                            hour_of_day = datetime.datetime.now().strftime("%H")
                            # We added an hour to the exit timestamp to avoid $0 ticket cost when testing this app
                            self.current_ticket['ticket_exit_timestamp'] = int(hour_of_day) + 1
                            hours_parked = int(self.current_ticket['ticket_exit_timestamp']) - int(self.current_ticket['ticket_entry_timestamp'])              
                            print(f"\nYou were parked for {hours_parked} hour(s).")
                            balance = hours_parked * int(self.current_ticket['ticket_cost'])
                            pay = input(f"Please confirm your payment of ${balance}). (yes/no) ")
                            if pay in ('yes','y'):
                                self.current_ticket['ticket_paid_status'] = True
                                print("\nThank you for your payment!")
                                print(f"\nThank you for parking in {self.garage_name}! Please visit us again!")
                                # print(f"before payment: {self.tickets}")
                                self.tickets.remove(self.current_ticket)
                                # print(f"after payment: {self.tickets}")
                                
                                self.parking_spaces_available += 1
                                self.tickets_available += 1
                                self.current_ticket = {}
                                return
                            elif pay in ('no','n'):
                                print('\nSecurity is on its way.')
                                break
                            else:
                                print("Please enter a valid response")
                    ticket_id_exists = False

        if self.current_ticket == {}:
            print("\nInvalid ticket id. Please try again.")
        if self.check_ticket():
            pass
        else:
            print("\nYou can only choose this option after taking a ticket!")
