#collection
list01= [1,2,3] #ordered & mutable
tuple
set
dict

###################--------LIST ------------########
#1. Ordered
#2. Mutable
#3. []

list1 = [1,2,3,4,'apple','mango']
print(list1)
print(list1[2]) # indexing start form 0
print(list1[1:4]) # range of index
print(list1[-1])


# change the item value
list1[4]='NewtonApple'
print(list1)

# Print all the list items
for i in list1:
    print(i)

# check if item present in list or not
if 'mango' in list1:
    print(True)

# length of list
print(len(list1))


# add items in list
list1.append("addedNewItem")
print(list1)
list1.insert(2,"insertedNewItem")
print(list1)


# remove the items from the list
list1.pop(2)
print(list1)
del list1[2]
print(list1)

# copying the list
list2 = list1.copy()
print(list2)


# Joined tow list or concadination
list3 =[list1+list2]
print(list3)
list4 = list1.extend(list2)
print(list4)

#########################----- Tuple ---------###############################
#1. Ordered
#2. Immutable
#3. ()

mytuple = (1,2,3,4,1,"mytuple")
print(mytuple)

# Indexing
print(mytuple[0])
print(mytuple[1:3])

# changing the tuple value
newtuple = list(mytuple)
newtuple.append("addingvalueinTuple")
newtuple = tuple(newtuple)
print(newtuple)