# file_name = open("read.txt","r")

#file_name = open("read.txt","a") # use 'U' if you want instead of 'a'
#file_name = open("read.txt","w")

#file_name.write("I am overwritting read.txt file \n I am learning python!")

#file_name.close()


# file_name = open("read.txt","r")
# print(file_name.read())
# file_name = open("../../read2.txt","r")

# print(file_name.read())
# print(file_name.read(5))

# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readline())
# print(file_name.readline())

# for l in file_name:
#    print(l)

#file_name.close()
# check x value in file operation


#file_name = open("read2.txt","w")

import os

#os.remove("read2.txt") . # to remove/delete file

# if os.path.exists("../../read2.txt"):
#     os.remove("../../read2.txt")
# else:
#     print("File not found!")

os.rmdir("test")


