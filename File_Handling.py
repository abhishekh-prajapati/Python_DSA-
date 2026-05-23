# #To read the file
# file = open("data.txt", "r")
# content = file.read()
# print(content)
# file.close()
# # data.txt file will contain hello world
# # as it contains hello world in the file
#
# #Readline
# file = open("data.txt","r")
# print(file.readline())
# print(file.readline())
#
# file.close()
#
# #Write
# file = open("data.txt","w")
#
# file.write("I am learning Python")
#
# file.close()
# ###I am learning python
# ###Old content will be erased
#
#
# #Append()
# file = open("data.txt","a")
#
# file.write("\nNew line added")
#
# file.close()
# ###I am learning Python
# ### New line added
#
#
# #close()
# file.close(z)
# # Because open files consume system resources
from test.test_win32trace import BasicSetupTearDown

# file = open("notes.txt", "w")
# file.write("python is easy")
# file.close()
#
# #Practice 2
# file = open("notes.txt","r")
# print(file.read())
# file.close()
#
# #append
# # Practice 3
# file = open("notes.txt","a")
# file.write("\nI will master Python")
# file.close()
#
#
# #File handling with statement
# #a New way to write this funciton (MODERN WAY)
# with open("notes.txt", "r") as file:
#     print(file.read())
#
#
# #Practice 4
# with open("Student.txt", "w") as file:
#     file.write("Name: Rahul\n")
#     file.write("Age: 20")
#
# ##CSV/TXT/JSON Basics
#
# # TXT Files
# import csv
#
# with open("students.csv", "w",newline="")as file:
#     writer = csv.writer(file)
#
#     writer.writerow(["name","age"])
#     writer.writerow(["Rahul", 20])
#     writer.writerow(["Aman", 22])
#
# #Reading CSV
# import csv
# with open("students.csv","r") as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# JSON Basic
#Writing JSON
# import json
# data={
#     "name": "Rahul",
#     "age": 20
# }
# with open("data.json", "w") as file:
#     json.dump(data,file)

#Reading JSON
# import json
# with open("data.json","r") as file:
#     data = json.load(file)
# print(data)

###########Solvinf problems#############
#Append data
# with open ("notes.txt","a") as file:
#     file.write("\n File handling is intresting")

#count lines
# count = 0
#
# with open("student.txt", "r") as file:
#     for line in file:
#         count += 1
#
# print(count)

# count line
# with open("student.txt","r") as file:
#     content = file.read()
# words = content.split()
# print(len(words))

# copy file content
# with open("source.txt", "r") as file:
#     content = file.read()
# with open("Destination.txt","w") as file:
#     file.write(content)

# FInd longest Word
# with open("source.txt","r") as file:
#     content = file.read()
# words = content.split()
# longest = ""
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print(longest)

# we will do small project next time
# Count Specific Word
# with open("source.txt","r") as file:
#     content = file.read()
# count = 0
# words = content.split()
#
# for word in words:
#     if word == "python":
#         count += 1
# print(count)


# Easier method
# with open("source.txt","r") as file:
#     content = file.read()
#
#     words = content.split()
#     print(words.count("python"))

# Reverse File Content
# with open("Source.txt") as file:
#     content = file.read()
# print(content[::-1])



# Merge Two files

# with open("source.txt","r") as file:
#     content1 = file.read()
#
# with open("student.txt","r")as file:
#     content2 = file.read()
#
# with open("merged.txt","w") as file:
#     file.write(content1)
#     file.write("\n")
#     file.write(content2)


#Find Number of Charachters

# with open("Student.txt","r") as file:
#     content = file.read()
#
# print(len(content))

#Remove space from file content
with open("source.txt","r")as file:
    content = file.read()

new_content = content.replace(" ","")
print(new_content)

