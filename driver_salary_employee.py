"""
Robert Walczak
the salary employee class
:param last_name - Employee's last name
:param phone_number - Employee's phone number
:param address_street - Employee's street address
:param first_name - Employee's first name
:param hourly_rate - Employee's salary
:param address_city - Employee's city and state
:param start_date - Employee's start date
:return Employee's personal information, salary and start date
"""
from module11_classes.topic4.employee_class import Employee
from module11_classes.topic4.salaried_employee_class import SalariedEmployee

new_emp = Employee('Walczak', 'Robert', '5151234567', '1313 First St', 'Ankeny, IA')
new_emp_salaried = SalariedEmployee(new_emp.last_name, new_emp.first_name, new_emp.phone_number, new_emp.address_1, new_emp.address_2, 40000, '04-02-2020')
print(new_emp_salaried.display())
new_emp_salaried.give_raise(45000)
print(new_emp_salaried.display())
del new_emp
