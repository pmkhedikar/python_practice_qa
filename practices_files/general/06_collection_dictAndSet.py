# Set -
# 1.Unordered & Unindexed
# 2.Mutable
# 3.{ }

myset1 ={1,2,3,'apple'}
print(myset1)

# accessing the value in set
for i in myset1:
    print(i)

# Value exist in set or not
print(1 in myset1)

# add - (single item)& update(multiple value) the tuple
myset1.add('Added_item')
print(myset1)
myset1.update(['x','y',66])
print(myset1)

# remove the value from set

myset1.remove(66)
myset1.discard('parag')  # not throwing any error for non existing item
#myset1.remove('parag')  # throwing error for non existing item
print(myset1)

# clearing the values from set & deleting the set
myset1.clear()
print(myset1)
del myset1


# joining 2 set union & update
set1 ={1,2,3}
set2 ={4,5}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)


#######################----- Dictonary ------ ############################
#1. unordered
#2. indexed
#3. Mutable
#4. {}

# Creating dict
mydict1 = {'name':'parag','age':35}
print(mydict1)

# access the item in dict
print(mydict1['name'])
x= mydict1.get('age')
print(x)

# change the value in dictonary
mydict1['name']='updated_name'
print(mydict1)

# reading items in dictornary using loap
for i in mydict1:
    print(i)
    print(mydict1[i])

for i in mydict1.values():
    print(i)

for x,y in mydict1.items():
    print(x,y)

# find the existence
print("name" in mydict1)
print(len(mydict1))

# adding & remove items to dictonary
mydict1['location']='Pune'
print(mydict1)

mydict1.pop("age")
print(mydict1)