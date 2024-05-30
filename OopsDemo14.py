#Constructor is method : When we create object of class it automatically called
#When we do not create any obj. :Default construcor will called
#self Keyword is Mandatory for call variable name in Method
#Instance variable is attached with Object and class varible is not attached with object
#in python constrouctor name is init not class name as in Java
#New Keyword is not required to create an object

class Cal():
    num = 200 #class variables

    def __init__(self,a,b): #Parameterised constructor: Whaterever argument we are throwing that should be implemente in
        self.firstnumber = a
        self.secondnumber = b
        print("I am called automatically when obj. is created")


    def summation(self):
        return self.firstnumber+self.secondnumber + self.num
        # In python we must have to call variable with self keyword
        #self is a object reference: who is calling you

#Instance variable
obj = Cal(2,3)
print(obj.summation())

obj1 = Cal(4,5)
print(obj1.summation())


