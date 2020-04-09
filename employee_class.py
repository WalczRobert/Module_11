"""
Robert Walczak
program to get and return employee personal information
:param phone_number - Employee's phone number
:param address_street - Employee's street address
:param last_name - Employee's last name
:param address_city - Employee's city and state
:param first_name - Employee's first name
:return Employee's personal information
"""
class Employee:

    def __init__(self, lname, fname, pnumber, address_street, address_city):
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber
        self.address_1 = address_street
        self.address_2 = address_city

    def display_employee(self):
        return self.last_name + self.first_name + self.phone_number + self.address_1 + self.address_2
