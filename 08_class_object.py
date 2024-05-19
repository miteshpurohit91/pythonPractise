# Classes are user defined blueprint or Prototype
# sum, Addition,
# Class have Methods, Class variable, Instant variable, Constructor etc

class Calculator:
    num = 100

#function wrapped into class are calling as Methods
    def getData(self):
        print("I am now executing a Method in Class")


obj = Calculator() #syntax to create a Object in Python
obj.getData()
print(obj.num)
