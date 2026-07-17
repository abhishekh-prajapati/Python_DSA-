#Q1: First and Last Character + Reverse
# word =  "Developer"
# print(word[0])
# print(word[-1])
# print(word[::-1])
#

# #Q2: Convert Text Format
# text = ("python is easy")
# print(text.upper())
# print(text.title())

# Q3: Using f-String
# name = "Rahul"
# age = 25
# print(f"my name is {name} anda I am {age} years old")

# Q4: Count Characters
# word = "banana"
# print(word.count("a"))

##################LIST######################
# Q1: Create and Access List

# fruits = ["apple", "banana","mango","orange"]
# print(fruits[0])
# print(fruits[-1])
# print(fruits[1])

# Q2: Add Items to List

# numbers = [10,20,30]
# numbers.append(40)
# numbers.insert(1,15)
# print(numbers)

# Q3: Remove Items from List

# colors = ["red", "blue","green","yellow"]
# colors.remove("blue")
# colors.pop()
# print(colors)

# Q4: Sort and Reverse List

# nums = [4,1,8,2,5]
# nums.sort()
# nums.reverse()
# print(nums)

##################TUPLE######################
# Q1: Tuple Basics
# colors = ("red","blue","green","yellow")
#
# colors[0]
# colors[-1]
# print(len(colors))


# text = "Banana"
# text.upper()
# text.replace("a","o")
# print(text)
#

# Q2 Tuple packing and unpacking

# name = "Rahul"
# age = 25
# city = "Mumbai"
#
# person = (name , age , city )
# name , age , city = person
#
# print(person)
#
# print(name)
# print(age)
# print(city)



##################SETS######################
#
# # Q1: Unique Values
# nums = {1,2,2,3,4,4,5}
# print(nums)

# Q2: Add and Remove in Set

# fruits = {"apple","banana","mango"}
# fruits.add("orange")
# fruits.remove("banana")
# print(fruits)

# Q3: Union of Sets

# set1 = {1,2,3}
# set2 = {3,4,5}
#
# result = set1.union(set2)
# print(result)

# Q4: Intersection of Sets
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}
#
# result = set1.intersection(set2)
# print(result)


##################Dictionaries######################


#Q1 How to Access a Value
# Student = {
#     "name": "Rahul",
#     "age": 25,
#     "city":"Mumbai"
# }
#
# print(Student["name"])
# print(Student["city"])



# Q2: Dictionary Methods — keys(), values(), items()
# car = {
#     "brand": "Toyota",
#     "model": "Camry",
#     "year": 2022
# }
# print(car.keys())
# print(car.values())
# print(car.items())


# Q3: get() and update()
# person = {
#     "name": "Amit",
#     "age": 28
# }
# print(person.get("name"))
# person.update({"city" : "Delhi"})
# print(person)
#

###################QUESTIONSSS######################
# finding vowels
# Text = "programming"
# count = 0
# for t in Text:
#     if t in "aeiou":
#         count += 1
#
# print(count)


# Q2: Palindrome Check
# word = "madam"
#
# if word == word[::1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# Q3: Count Character Frequency
# text = "banana"
# for ch in set(text):
#     print(ch,":",text.count(ch))


# Q4: Remove Duplicate Characters
# text = "programming"
# result = ""
# for i in text:
#     if i not in result:
#         result += i
# print(result)

# Q5: Find Longest Word
# sentence = "Python is very powerful language"

# words = sentence.split()
# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# print(longest)

# Q6: Find Maximum Number

# nums = [4, 7, 2, 9, 1]
#
# largest = nums[0]
#
# for num in nums:
#     if num > largest:
#         largest = num
# print(largest)


# Q7: Find Second Largest Number
# nums = [10, 45, 23, 67, 12]
#
# largest = nums[0]
# second_largest = nums[0]
#
# for num in nums:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
#
# print(second_largest)


# Q8: Remove Duplicates from List

# nums = [1, 2, 2, 3, 4, 4, 5]
#
# result = []
#
# for num in nums:
#     if num not in result:
#         result.append(num)
#
# print(result)

# Q10: Find Common Elements

# list1 = [1, 2, 3, 4]
# list2 = [3, 4, 5, 6]
#
# result = []
#
# for num in list1:
#     for hello in list2:
#         if num == hello:
#             result.append(num)
# print(result)

# Q11: Find Maximum Value in Tuple

# numbers = (12, 45, 7, 89, 23)
# result = (0)
#
# for num in numbers:
#     if num > result:
#         result = num
# print(result)
