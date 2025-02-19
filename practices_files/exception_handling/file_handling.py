#### writing the data in text file

# file = open("E:/python/practices_files/files/demo01.txt","w")
# file.write('First line \n')
# file.write('Second line \n')
# file.close()


######### read the file

# file = open("E:/python/practices_files/files/demo01.txt","r")
# print(file.read())
# print(file.readline())
# file.close()


########## append the new line in existing file
file = open("E:/python/practices_files/files/demo01.txt","a")
file.write("New line in existing file")
file.close()
#print(file.read())