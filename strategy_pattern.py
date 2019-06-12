
#Not use design pattern
# class Vehicle:
#     def go(self):
#         print('Now I\'m driving.' )

# class Car(Vehicle):
#     pass

# class motobike(Vehicle):
#     pass

# class airplan(Vehicle):
#     def go(self):
#         print('Now I\'m Flying.')

# class jet(airplan):
#     def go(self):
#         print("Now I'm flying very fast")

# car_1 = Car()
# moto_1 = motobike()
# airplan_1 = airplan()
# jet_1 = jet()

# car_1.go()
# moto_1.go()
# airplan_1.go()
# jet_1.go()

#Use design pattern
class Vehicle:
    def go(self, callback):
        callback()
def going():
    print("Now I'm going")
def flying():
    print("Now I'm flying")
def flying_fast():
    print("Now I'm flying fast")
car_1 = Vehicle()
moto_1 = Vehicle()
airplan_1 = Vehicle()
jet_1 = Vehicle()
car_1.go(going)
moto_1.go(going)
airplan_1.go(flying)
jet_1.go(flying_fast)


# class Vehicle:
#     def __init__(self, message):
#         self.message = message
#     def go(self):
#         print(self.message)

# class Car(Vehicle):
#     pass
# class Motobike(Vehicle):
#     pass
# class Airplan(Vehicle):
#     pass
# class Jet(Airplan):
#     pass
# car_1 = Car("Now I'm going")
# moto_1 = Motobike("Now I'm going")
# airplan_1 = Airplan("Now I'm flying")
# jet_1 = Jet("Now I'm flying very fast")

# car_1.go()
# moto_1.go()
# airplan_1.go()
# jet_1.go()