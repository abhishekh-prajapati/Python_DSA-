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

#Write
file = open("data.txt","w")

file.write("I am learning Python")

file.close()
###I am learning python
###Old content will be erased


#Append()
file = open("data.txt","a")

file.write("\nNew line added")

file.close()
###I am learning Python
### New line added


#close()
file.close()
### open file consume system resources