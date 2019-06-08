#  Python OOP

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+last + '@company.com'
    def full_name(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Jon','Doe',500)
emp_2 = Employee('Jon','Smith',800)

print(emp_1.email)
print(emp_2.email)

print(emp_2.full_name())