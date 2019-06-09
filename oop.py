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

emp_1 = Employee('Jon','Doe',500)
emp_2 = Employee('Jon','Smith',800)
emp_1.apply_raise()

print(emp_1.pay)
print(emp_2.email)
print(Employee.num_of_emps)

print(emp_2.full_name())