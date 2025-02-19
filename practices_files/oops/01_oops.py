# Declaration
class Myclass:    # created the class
    def myfun(self):
        pass
    def display(self,name): # created method
        print(name)

mc1= Myclass()   # created the class object
mc1.display("parag") # call the method

## Static & instance method - for static method object creation is not required

class Myclass01:
    def myfun(self):
        print("Instance method")
    @staticmethod
    def stamethod01(self,num):
        print(self,num)
mc01 = Myclass01
mc01.myfun('parag')
Myclass01.stamethod01('paragk',100)


## Class Variable
class Globalvar():
    a = 10
    b = 20
    def add(self):
        print(self.a+self.b)
    def Multi(self):
        print(self.a * self.b)
mc = Globalvar()
mc.add()


##### Global , Class & Local Variables - Variables name are different

a , b = 10 ,20   # global variable
class LocalGlobalClassVar():
    x , y = 1, 2  # class variable
    def add(self,i,j):
        print(i+j)    # local variable
        print(self.x+self.y) # class variable
        print(a+b)
o1 = LocalGlobalClassVar()
o1.add(10,20)


####### global, local, class variable name are same

x,y = 10,20

class SameVariableNameClass():
    x,y =100,200
    def add(self,x,y):
        print(x+y)
        print(self.x+self.y)
        print(globals()['x']+globals()['y'])

####### One class have multiple object ######

class Myclass001():
    def display(self):
        print("Display method")
m1 = Myclass001()
m2 = Myclass001()
m1.display()
m2.display()


### Calling constructor

class MyclassConst():
    def __init__(self):
        print("This is constructor")
    def display01(self):
        print("display method in class")

mc001 = MyclassConst()


#### Class with constructor having argumnet

class Employee():
    def __init__(self,empid,name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def display(self):
        print(self.empid, self.name,self.salary)

e1 = Employee(123,'Parag','40LPA')
e1.display()


########## __str__constructor

class Employee():
    def __init__(self,empid,name, salary):
        self.empid = empid
        self.name = name
        self.salary = salary
    def __str__(self):
        return (self.name)

e01 = Employee(123,'Parag','40LPA')
print(e01)


