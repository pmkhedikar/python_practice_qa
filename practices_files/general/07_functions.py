from dis import Positions


def fun01():
    print('Hi ..without any argument')
fun01()

def fun02(a):
    return a*2
print(fun02(2))

def fun03(a,b):
    return a+b
fun03(2,3)

def fun04():
    return
fun04()

########## Local & Global Variables
n = 10   # Global variable
def local01():
    p = 20  #local Variable
    print(p)
local01()
print(n)
#print(p) # throwing error as local variable not accessible outside

x = 100
def local02():
    global x
    x =200
    y= 300
    print(x)
    print(y)
local02()
print(x)


def local02():
    global z
    z=1000
    print(z)
local02()
print(z)


# Positional & Keyword argument
def funt01(i,j=30):
    print(i,j)
funt01(10,20)   # - Positional argument/parameter
funt01(i=100,j=200)  #- keyword argument/parameter
funt01(100,200)
funt01(100)

#positional argument follows keyword argument

# Function can return multiple value
def largest(a,b):
    if a>b:
        return (a,b)
    else:
        return (b,a)

result = largest(1,2)
print(type(result))