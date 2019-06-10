#  Python OOP

class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last + '@company.com'
        Employee.num_of_emps += 1

    def full_name(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, int(pay))
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday()==6:
            return False
        return True
emp_1 = Employee('Jon','Doe',500)
emp_2 = Employee('Jon','Smith',800)

import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))

# Employee.set_raise_amt(1.05)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.apply_raise()

# print(emp_1.pay)
# print(emp_2.email)
# print(Employee.num_of_emps)

# print(emp_2.full_name())

# emp_str_1 = 'John-Doe-70000'
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(type(new_emp_1.pay))