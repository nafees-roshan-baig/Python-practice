# Single Inheritance
class Vehicle:
    def info(self):
        print("This is a vehicle.")
class Car(Vehicle):
    def car_info(self):
        print("This is a car.")
obj1 = Car()
obj1.car_info()
obj1.info()

# Multiple Inheritance
class Father:
    def father_info(self):
        print("This is the father.")
class Mother:
    def mother_info(self):
        print("This is the mother.")
class Child(Father,Mother):
    def child_info(self):
        print("This is the child.")
obj1 = Child()
obj1.child_info()
obj1.mother_info()
obj1.father_info()

# Multilevel Inheritance
class Person:
    def get_name(self):
        print("name : Roshan")
class Employee(Person):
    def get_employee_id(self):
        print("7838")
class Manager(Employee):
    def get_department(self):
        print("D.S")
obj1 = Manager()
obj1.get_department()
obj1.get_employee_id()
obj1.get_name()


# Hierarchial Inheritance

class Animal:
    def animal_sound(self):
        print("Animals make sounds.")
class Dog(Animal):
    def bark(self):
        print("Dog barks.")
class Cat(Animal):
    def meow(self):
        print("Cat meows.")
obj1=Dog()
obj2=Cat()
obj1.animal_sound()
obj1.bark()
obj2.meow()
obj2.animal_sound()

#HYBRID INHERITANCE
class Device:
    def power_on(self):
        print("Device powered on")
class Phone(Device):
    def make_call(self):
        print("Making a call")
class Tablet(Device):
    def browse_web(self):
        print("Browsing the web")
class Smart:
    def connect_to_wifi(self):
        print("Connected to WiFi")
class Smartphone(Phone, Smart):
    pass
obj1=Smartphone()
obj1.power_on()
obj1.make_call()
obj1.connect_to_wifi()

#Using INIT Constructor
# class Person:
#     def __init__(self,name):
#         self.name=name
#     def person_info(self):
#         print(self.name)
# class Student(Person):
#     def __init__(self,roll_no):
#         self.roll_no=roll_no
#     def student_info(self):
#         print(self.roll_no)
# class Sports:
#     def __init__(self,sport):
#         self.sport=sport
#     def sports_info(self):
#         print(self.sport)
# class StudentAthlete(Student,Sports):
#     def __init__ (self,name,roll_no,sport):
#         pass
#
# obj = StudentAthlete("Roshan", 101, "Cricket")
#
# obj.person_info()
# obj.student_info()
# obj.sports_info()

class Person:
    def __init__(self, name):
        self.name = name

    def person_info(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, roll_no):
        Person.__init__(self, name)
        self.roll_no = roll_no

    def student_info(self):
        print("Roll Number:", self.roll_no)


class Sports:
    def __init__(self, sport):
        self.sport = sport

    def sports_info(self):
        print("Sport:", self.sport)


class StudentAthlete(Student, Sports):
    def __init__(self, name, roll_no, sport):
        Student.__init__(self, name, roll_no)
        Sports.__init__(self, sport)


obj = StudentAthlete("Roshan", 101, "Cricket")

obj.person_info()
obj.student_info()
obj.sports_info()
# 2

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def vehicle_info(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        Vehicle.__init__(self, brand)
        self.model = model

    def car_info(self):
        print("Model:", self.model)


class Electric:
    def __init__(self, battery):
        self.battery = battery

    def battery_info(self):
        print("Battery Capacity:", self.battery)


class ElectricCar(Car, Electric):
    def __init__(self, brand, model, battery):
        Car.__init__(self, brand, model)
        Electric.__init__(self, battery)


obj = ElectricCar("Tata", "Nexon EV", "40.5 kWh")

obj.vehicle_info()
obj.car_info()
obj.battery_info()
