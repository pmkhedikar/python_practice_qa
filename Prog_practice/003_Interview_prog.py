#Example 1: Sorting list
#Example 2: Find teh max no
#Example 3: Prime no &  List of prime no
#Example 4: Factorial of No
#Example 5: Total No of char in string
#Example 6: Fabonacci series
#Example 7: Reverse the string/Palindrome
#Example 8: Find duplicate,Unique - String
#Example 9: Find the occurance of char in string
#Exxample 10: Sort the word in sentence

from itertools import count


###Example 1:
# def sorting(list):
#     # #return max(list)
#     # print(sorted(list))
#     # list.sort()
#     # print(list)
#     for i in range(len(list)-1,0,-1):
#         for j in range(i):
#             if list[j] > list[j+1]:
#                 temp = list[j]
#                 list[j]=list[j+1]
#                 list[j+1]=temp
#     return list
#
# list=[1,24,5,8,3,64,3]
# print(sorting(list))


# ### Example 2:
# def findMaxNo(list):
#     max_no = 0
#     for i in range(len(list)):
#         if list[i] > max_no:
#             max_no = list[i]
#     return max_no
#
#
# list=[1,33,56,2,78]
# print(findMaxNo(list))

# ### Example 3:
# def primeNo(n):
#     for i in range(2,n):
#         if n%i==0:
#             return False
#     return n
#
# def primeList(x):
#     list =[]
#     for j in range(2,x):
#         if primeNo(j) != False:
#             list.append(primeNo(j))
#     return list
#
# print(primeNo(100))
# print(primeList(100))

# ###Example 4:
# def factoriial(n):
#     fac=1
#     for i in range(1,n+1):
#         fac = fac * i
#     return fac
# n=4
# print(factoriial(n))

# ### Example 5:
# def totalChar(string):
#     count=0
#     for i in range(len(string)):
#         count= count +1
#     return count
# string='parag'
# print(totalChar(string))


# ### Example 6:
# def fab(n):
#     a,b= 0,1
#     for i in range(n):
#         c= a+b
#         a = b
#         b = c
#         print(c, end=' ')
# fab(10)

### Example 7:
# def reverseString(string):
#     str =''
#     for i in string:
#         str = i + str
#     return str
#
# def palidrome(string):
#     if string == reverseString(string):
#         return True
#     else:
#         return False
# string='parag'
# print(reverseString(string))
# # print(palidrome('madam'))

###Example -8
# def findDuplicate(string):
#     str =''
#     for i in string:
#         if string.count(i)==1:
#             if i not in str:
#                 str= str+i
#     return str
# string =  'parag'
# print(findDuplicate(string))

### Example 9:
# def charOccurance(string):
#     d ={}
#     for i in string.lower():
#         if i != ' ':
#             if i not in d:
#                 d[i]=1
#             else:
#                 d[i] = d[i] +1
#     return d
#
# string = 'i am python developer staying in Pune'
# print(charOccurance(string))


### Example 10:
def sortString(string):
    str = string.split()
    for i in str:
        print(i)

string='my name is Parag i am python developer'
print(sortString(string))