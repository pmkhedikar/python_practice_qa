#Example 1: count the char in string
#Example 2: count the word in string
#Example 3: count all upper/lower/numeric case character in string
#Example 4: count only vowels in given string
#Example 6: count occurrence of each  char/word in string
#Example 7: Fetch all the words having even no of chars in string
#Example 8: Fetch all the words which start with vowel
#Example 9: Fetch all the word start & end with consonant
#Example 10: Fetch all the consonant in string
#Example 11: Fetch first/last char of each word in string
#Example 12: Fetch the first & Last char of each word in string
#Example 13: Program to convert the given string into pascal case
#Example 14: Program to reverse the char in given string.
#Example 15: Program to reverse the string words.
#Example 16: Program to reverse each word in string.(PENDING)
#Example 17: Program to sort given string in asending order
#Example 18: Program to swap the cases of string
#Example 38: Program to find longest & shorted word(pending)
#Example 39: Find the index no of all occurance of same character
#Example 40 : Find the missing char from string
#Example 41: Find the biggest palandrome in string



##Example 1:
# def strCount(string):
#     count=0
#     for i in string:
#         count = count +1
#     return count
# print(strCount("parag"))


# ##Example 2:
# def wordCount(string):
#     new_str = string.split()
#     count = 0
#     for i in new_str:
#         count= count+1
#     return count
# print(wordCount("Hi my name is parag"))


# # ##Example 3:
# def charUpperCaseCount(string):
#      count = 0
#      for i in string:
#          # if i.isnumeric():
#          if i.islower():
#          # if i.isnumeric():
#          #if i.isascii():
#              count= count+1
#      return count
# print(charUpperCaseCount("PaRaGkhediKAR123#$"))


# ##Example 4:
# def countVowelesInString(string):
#     count = 0
#     for i in string:
#         if i in 'aeiou':
#             count = count +1
#     return count
# print(countVowelesInString("parag aeiou"))

# ### Example 6:
# def countOccuranceofEachChar(string):
#     #string1 = string.split()
#     d ={}
#     for i in string.lower():
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]= d[i]+1
#     return d
# print(countOccuranceofEachChar("parag aeiou parag am am"))

# ### Example 7:
# def fecthEvenCharWord(string):
#     new_str = string.split()
#     for i in new_str:
#         if len(i)%2==0:
#             print(i)
# fecthEvenCharWord("I amm python automation QA")


### Example 8:
# def fetchWordWithVowel(string):
#     new_stg= string.split()
#     list1=[]
#     for i in new_stg:
#         if i[0] in 'aeiou':
#             list1.append(i)
#     return list1
#
# print(fetchWordWithVowel('Hi my aame is Parag I like apple'))

# ### Example 9:
# def startEndwithVowel(string):
#     new_stg = string.split()
#     new_list=[]
#     for i in new_stg:
#         if i[0].lower and i[-1] not in "aeiou":
#             new_list.append(i)
#     return new_list
#
# print(startEndwithVowel("aa i am Parag aieou"))


# ### Example 10:
# def fetchConsonant(string):
#     str =[]
#     for i in string:
#         if i.lower() not in 'aeiou':
#             str.append(i)
#     return str
#
# print(fetchConsonant("stringAP"))


### Example 11:
# def fetchFirstCharWord(string):
#     new_stg = string.split()
#     list1 =[]
#     for i in new_stg:
#         list1.append(i[0])
#     return list1
# print(fetchFirstCharWord("My name is Parag"))


# ### Example 12:
# def fetchFirstLastCharWord(string):
#     new_str =  string.split()
#     list1 = []
#     for i in new_str:
#         list1.extend([i[0]+i[-1]])
#     return list1
#
# print(fetchFirstLastCharWord('this is python programing'))

# ### Example 13:
# def pascalCase(string):
#     new_stg = string
#     str =''
#     for i in new_stg:
#         # print(i[0])
#         str = str +i[0].upper()+ i[1:].lower()
#     return str
#
# print(pascalCase(" hi tis is Parag python Developer"))



# ## Example 15:
# def reverseWordString(string):
#     new_str = string.split()
#     str = ''
#     for i in new_str:
#         str = i + " " +str
#     return  str
#
# print(reverseWordString('hi i am parag python developer'))

# ### Example 16:
# def reveseEachWordInString(string):
#     str =''
#     new_str = string.split()
#     for i in new_str:
#         print(i[::-1],end=' ')
#
# reveseEachWordInString('Hi my name is Parag i am python Developer'))


# ### Example 17:
# def sortStringInAscOrder(num1):
#     num = list(num1)
#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j] > num[j+1]:
#                 temp = num[j]
#                 num[j] = num[j+1]
#                 num[j+1]= temp
#     return num
#     #return "".join(num)
# num1= 'parag'
# print(sortStringInAscOrder(num1))

# #Example 18:
# def swapCases(string):
#     for i in string:
#         if i.isupper():
#             print(i.lower(),end='')
#         else:
#             print(i.upper(),end='')
#
# swapCases('Parag1')


# ### Example 38
# def longestShortest(string):
#     new_str = string
#     for i in new_str:
#         if len(i)== max(len(i) for i in new_str):
#             return i
#
#
# print(longestShortest('Hi Parag here Python developer'))

# ### Example 39
# def occuranceOfChar(string):
#     char = 'a'
#     list =[]
#     # for i in range(len(string)):
#     #     if string[i] ==char:
#     #         list.append(i)
#     # return list
#     return [i for i in range(len(string)) if string[i]==char]
# print(occuranceOfChar("paragkhedikar"))


# ### Example 40
#
# def missingChar(list):
#     minno =min(list)
#     maxno =max(list)
#     for i in range(minno,maxno):
#         if i not in list:
#             print(i)
#
# list=[1,2,4,6,8,9]
# print(missingChar(list))


### Example 41

# def biggestPalandrome(list):
#     new_list = list.split()
#     for j in [i for i in new_list if i == i[::-1]]
#
#             # if len(i) == max(len(i)):
#             #     print(i)
# print(biggestPalandrome("parag maam madam eve"))