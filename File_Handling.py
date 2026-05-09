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

file = open("notes.txt", "w")
file.write("python is easy")
file.close()

#Practice 2
file = open("notes.txt","r")
print(file.read())
file.close()

#append
# Practice 3
file = open("notes.txt","a")
file.write("\nI will master Python")
file.close()


#File handling with statement
#a New way to write this funciton (MODERN WAY)
with open("notes.txt", "r") as file:
    print(file.read())


#Practice 4
with open("Student.txt", "w") as file:
    file.write("Name: Rahul\n")
    file.write("Age: 20")

##CSV/TXT/JSON Basics

# TXT Files
import csv

with open("students.csv", "w",newline="")as file:
    writer = csv.writer(file)

    writer.writerow(["name","age"])
    writer.writerow(["Rahul", 20])
    writer.writerow(["Aman", 22])

#Reading CSV
import csv
with open("students.csv","r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)