s1 = "String"
s2 = str("welcome")
print(type(s1))


# Slicing
str ="Welcome"
print(str[1:3])
print(str[2:]) #till end of string
print(str[:4]) #start by default from zero
print(str[2:-1])


# min(), max() , len()
print(min(str))
print(max(str))
print(len(str))

print("#### in & not in ####")
print("come" not in str)
print("come" in str)


print("#### string comparisiom ####")
print('parag'=='garap')
print('parag'=='parag')
print('parag'=='abc')


print("########## Testing string True/False ##########")
x = "this is string None"
print(x.isalnum())
print(x.isnumeric())
print(x.isidentifier()) # reserved keys in python
print(x.islower())
print(x.isupper())


print("##### Searching for Substring #####")
s = "Welcome to pYthon"
print(s.endswith("python"))
print(s.find("to"))
print(s.count("o"))


print("####### Converting the string #########")
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.replace('to','in'))


print("######### Reverse the String #########")