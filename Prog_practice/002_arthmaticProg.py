#Example 29: Write the prog to interchange the values in dic
#Example 30: Find the square all the no in list
#Example 31: Reverse the dictonary
#Example 32: Fetch the unique element in list, only duplicates ,only single time occurance
#Example 33: Fetch the only duplicate char in string (check video again)
#Example 34: Fetch only integer in given list
#Example 35: find the paladrome in list
#Example 42: Reversing all the keys in dict
#Example 43: Fetch all keys having even value
#Example 44: Updating the highest value with all values in dict
#Example 45: Fetch all non repeating elements in list

# ####Example 29:
# def interChangeKeyValue(dict):
#     dict= {'name':'Parag','Location':'Pune'}
#     for key,value in dict.items():
#         print(value,key)
#
# print(interChangeKeyValue(dict))

# ### Example 30:
# def findSqureList(list):
#     # for i in list:
#     #     if i % 2 == 0:
#     #         print(str(i) + '=' + str(i**2))
#     print([i**2 for i in list if i%2 == 0])
#
# list=[1,23,4,5,6,8,9]
# findSqureList(list)

# ### Example 31:
# def reverse_dict(dict):
#     print(list(dict.items())[::-1])
#
# dict={'a':1,'b':2,'c':3}
# print(reverse_dict(dict))

# ### Example 32:
# def uniqueList(list1):
#     list01=[]
#     for i in list1:
#         if i not in list1:
#             list01.append(i)
#     return list01
# list1=[1,4,5,2,4,1,8]
# print(uniqueList(list1))
# #print(list(set(list1)))


# ### Example 34:
# def onlyduplicateChar(string):
#     for i in string:
#         if
#         print(i)
#
# print(onlyduplicateChar('paragkhedikar'))



### Example 34:
# def fetchInteger(list):
#     #return [i for i in list if type(i) is int]
#     # for i in list:
#     #     if type(i) is int:
#     #         print(i)
#
# list =['Parag',1,2,True,5]
# print(fetchInteger(list))


# ### Example 35:
# def paladrome(list):
#     return [i for i in list if i ==i[::-1]]
#
# list =['parag','madam','hi','eve']
# print(paladrome(list))

# ### Example Reversing all the keys
# def reverseOnlyKeys(dict):
#     for i in dict:
#         print(dict.items())
# dict ={'a':1,'b':2,'c':3}
# print(reverseOnlyKeys(dict))


## Example 43:
# def fetchEvenValuesinDic(dict):
#    return [i for i in dict if dict[i]%2==0]
# dict ={'a':1,'b':2,'c':3,'d':4}
# print(fetchEvenValuesinDic(dict))


# Example 44:
# def updateHighValuesToAllValuesinDic(dict):
#     max_value =max(dict[i] for i in dict)
#     for j in dict:
#         dict[j]=max_value
#     return dict
#
# dict ={'a':1,'b':2,'c':3,'d':4}
# print(updateHighValuesToAllValuesinDic(dict))

# ### Example 45
# def uniqueCharInString(string):
#     str = ''
#     ## Unique occurance
#     # for i in string:
#     #     if i not in str:
#     #         str=str+i
#     # return str
#
#     # ##Only Single Occurance
#     # for i in string:
#     #     if string.count(i)==1:
#     #         str=str+i
#     # return str
#
#     # ## Only duplicates
#     # for i in string:
#     #     if string.count(i)>1:
#     #         str=str+i
#     # return str
# string='paragkhedikar'
# print(uniqueCharInString(string))
