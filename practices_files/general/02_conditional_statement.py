age= int(input("Enter ur age "))
if age > 18:
    print("Your are eligible for voting")
else:
    print("Your are below 18, kindly wait for :{} years ".format(18-age))

###########
num = int(input("Enter any no:"))
print("Even Number") if num%2 ==0 else print("Odd number")
