# class Ticket

# Data only class?

# Attributes: 
# - Cost
# - Entry timestamp
# - Exit timestamp
# - Vehicle license plate
# - Paid status: True/False
# -

class Ticket:
    def __init__(self, ticket_id, ticket_cost, ticket_entry_timestamp, ticket_vehicle_license_plate) -> None:
        self.ticket_id = ticket_id
        self.ticket_cost = ticket_cost
        self.ticket_entry_timestamp = ticket_entry_timestamp
        self.ticket_vehicle_license_plate = ticket_vehicle_license_plate
        self.ticket_exit_timestamp = None
        self.ticket_paid_status = None

    def make_dict(self):
        current_ticket_dict = {
            "ticket_id": self.ticket_id,
            "ticket_cost": self.ticket_cost,
            "ticket_entry_timestamp": self.ticket_entry_timestamp,
            "ticket_vehicle_license_plate": self.ticket_vehicle_license_plate,
            "ticket_exit_timestamp": None,
            "ticket_paid_status": False        
    }
        return current_ticket_dict
