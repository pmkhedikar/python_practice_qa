######example 01 try & except

# print("Start of the program")
# try:
#     print(x)
# except:
#     print("exception block")
# print("End of program")


# ###### Particular exception handling

# print("start of program")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print("ZeroDivisionError exception handled")
# print("end of program")


##### except ..else finally

# print("start of program")
# try:
#     print(10/2)
# except ZeroDivisionError:
#     print("ZeroDivisionError exception handled")
# else:
#     print("Else block incase exception not occured")
# finally:
#     print("Finally -It occures every time no matter exception occured or not")
# print("end of program")


######## Raising own Exceptions
def evenOdd(n):
    if n < 0:
        raise ValueError("Only integers are allowed")
    if n%2==0:
        print("{} is even number".format(n))
    else:
        print("{} is odd number".format(n))
n=10
try:
    evenOdd(n)
except ValueError:
    print("Value Error Occure: Please add integer only")







