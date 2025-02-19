friends ={"tom":123,'jerry': 456}
print(friends)
print(friends.keys())
print(friends['tom'])
friends['bob']= 890 # added new key
print(friends)
friends['bob']='updated_890' #updated the value
print(friends)
del friends['bob']
print(friends)
friends['bob']='newly_added'  #addedd new value
print(friends)

for i in friends:    #getting keys
    print(i)

for i in friends.keys(): #getting keys
    print(i)

for i in friends:         #getting values
    print(friends[i])

for i in friends:
    print(i ,"=" ,friends[i])

print(len(friends))

print(friends.popitem())   # remove last item in dictonary

print(friends)

print(friends.keys())   # return all the values in tuples

print(friends.values())  # return all the values in tuple

print(friends.get('tom')) # returning the value

print(friends.pop('tom')) #deleted the key & value

print(friends)