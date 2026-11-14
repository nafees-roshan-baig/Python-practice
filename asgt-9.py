# 1:Create a dictionary student with keys: "name", "age", "course".
# Assign values "John", 20, "Python". Print it.
students ={"name":"john","age":20,"course":"Python"}
print(students)
# 2:From the dictionary below, print only the "model":

car = {"brand": "Ford", "model": "Fiesta", "year": 2010}
print(car["model"])

# 3:Using the dictionary:
# fruit = {"name": "Apple", "color": "Red", "price": 120}
# Retrieve the "color" using get().
fruit = {"name": "Apple", "color": "Red", "price": 120}
print(fruit.get("color"))
# 4:Change the "year" in the dictionary below from 2010 to 2024:
# bike = {"brand": "Yamaha", "model": "R15", "year": 2010}
bike = {"brand": "Yamaha", "model": "R15", "year": 2010}
bike["year"]=2024
print(bike)
# 5:Add a new key "color": "Blue" to the dictionary:
# city = {"name": "Paris", "country": "France"}
city = {"name": "Paris", "country": "France"}
city.update({"color": "Blue"})
print(city)
# 6:Remove "age" from the dictionary:
# person = {"name": "Alice", "age": 25, "job": "Engineer"}
person = {"name": "Alice", "age": 25, "job": "Engineer"}
person.pop("age")
print(person)
# 7:Print all keys of the dictionary:
# animal = {"type": "Dog", "breed": "Labrador", "age": 5}
animal = {"type": "Dog", "breed": "Labrador", "age": 5}
print(animal.keys())
# 8:Print all values of the dictionary using loops:
# country = {"name": "India", "capital": "New Delhi", "currency": "Rupee"}
country = {"name": "India", "capital": "New Delhi", "currency": "Rupee"}
print(country.values())
# 9:Copy the dictionary employee into another dictionary emp_copy:
# employee = {"id": 101, "name": "Rahul", "dept": "Sales"}
employee = {"id": 101, "name": "Rahul", "dept": "Sales"}
emp_copy = employee.copy()
print(emp_copy)
# 10:Create a dictionary students with two students inside:
# Student1: name="Tom", age=15
# Student2: name="Jerry", age=14
students={"student1":{"name":"tom","age":15},"student2":{"name":"Jerry","age":14}}
print(students)