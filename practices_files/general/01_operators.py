from webbrowser import parse_args

a = True
b = False
c = 5
name = 'Parag'
print(a+b)
print(a>b)
print(a+5) # concadination True = 1 & False = 0
print("My name is Parag and my age is ", c)
print("My name is Parag and my age is %c" %(c))
print("My name is :{} and my age is".format(name,c))
a = int(input("Kindly enter ur age: "))
b = float(input("add ur percentage"))
print(a + b)