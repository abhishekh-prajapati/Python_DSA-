#To read the file
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()
# data.txt file will contain hello world
# as it contains hello world in the file

#Readline
file = open("data.txt","r")
print(file.readline())
print(file.readline())

file.close()
