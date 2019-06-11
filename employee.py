

class Employee():
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)
    @property
    def full_name(self):
        return '{} - {}'.format(self.first, self.last)
    
    @full_name.setter
    def full_name(self, full_name):
        first, last = full_name.split(' ')
        self.first = first
        self.last = last
    @full_name.deleter
    def full_name(self):
        print('Delete Pr')
        self.first = None
        self.last = None

emp_1 = Employee('Jon', 'Doe', 1000)

emp_1.full_name = 'Doan Khue'
del emp_1.full_name
print(emp_1.full_name)
print(emp_1.email)