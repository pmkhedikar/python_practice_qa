# single inheritance
####Example 01
# class A:
#     def m1(self):
#         print("method m1 from class A")
# class B(A):
#     def m2(self):
#         print("method m2 from class B")
#
# b1 = B()
# b1.m2()
# b1.m1()

####### Example 02
# class A:
#     a , b = 10,20
#     def m01(self):
#         print(self.a +self.b)
#
# class B(A):
#     x , y = 100,200
#     def m02(self):
#         print(self.x - self.y)
#
# b01 = B()
# b01.m01()
# b01.m02()


######### Multi level inheritance
# class A:
#     a , b = 10,20
#     def add(self):
#         print(self.a +self.b)
#
# class B(A):
#     x , y = 100,200
#     def sub(self):
#         print(self.x - self.y)
#
# class C(B):
#     x,y = 101,201
#     def multi(self):
#         print(self.x*self.y)
#
# c01 = C()
# c01.add()

############ Hirarchy inheritance ###########
# class A:
#     a , b = 10,20
#     def add(self):
#         print(self.a +self.b)
#
# class B(A):
#     x , y = 100,200
#     def sub(self):
#         print(self.x - self.y)
#
# class C(A):
#     x,y = 101,201
#     def multi(self):
#         print(self.x*self.y)
#
# c01 = C()
# c01.add()
# c01.multi()

############ Multiple inheritance ###########
# class A:
#     a , b = 10,20
#     def add(self):
#         print(self.a +self.b)
#
# class B:
#     x , y = 100,200
#     def sub(self):
#         print(self.x - self.y)
#
# class C(A,B):
#     i,j = 101,201
#     def multi(self):
#         print(self.i*self.j)
#
# c01 = C()
# c01.add()
# c01.multi()
# c01.sub()


########## Method Overridding & Super class##########
# class A:
#     def m1(self):
#         print("method m1 from class A")
# class B(A):
#     def m1(self):
#         print("method m1 from class B")
#         super().m1()
#
# b1= B()
# b1.m1()


# ############## usage of class variable in child class ########
# class A:
#     a,b = 10,20   # class variable
#
# class B(A):
#     x,y = 100,200      #class variable
#     def m1(self):
#         i,j =101,201    #local variable
#         print(i+j)
#         print(self.x+self.y)
#         print(self.a+self.b)
#
# b01 = B()
# b01.m1()


############## variable over ridding in child class ########
class A:
    a,b = 10,20   # class variable

class B(A):
    x,y = 100,200      #class variable
    def m1(self):
        i,j =101,201    #local variable
        print(i+j)
        print(self.x+self.y)
        print(self.a+self.b)

b01 = B()
b01.m1()


############## over loading/ Polymorphisum ##########

class Greeting():
    def sayHello(self,name=None):
        if name is not None:
            print("Hello :{}".format(name))
        else:
            print('hello')

g1 = Greeting()
g1.sayHello()
g1.sayHello("Parag")