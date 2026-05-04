#####################Functions########################

# def greet():
#     print("Hello")
# greet()

#####################Parameters#########################
# def greet(name):
#     print("Hello", name)
#####################Arguments########################
# greet("Abhishekh")

#####################Return########################
# def add(a,b):
#     return a + b
# result = add(5, 3)
# print(result)


# Q1. Create a function named welcome() that prints:

# def welcome(name):
#     print("welcome", name)
# welcome(" to python")

#####################Types of Arguments########################
# Positional Arguments
# def student(name , age):
#     print(name, age)
# student("Rahul", 20)

#Keyword Arguments
#
# def student(name, age):
#     print(name , age)
# student(age=20, name="Rahul")

#Default Arguments

# def greet(name="Guest"):
#     print("Hello", name)
# greet()
# greet("Sam")

# #Variable length Arguments
# def add(*numbers):
#     print(numbers)
# add(1,2,3,4)

# # Q2. Create a function student() that takes name and age and prints both.
# def student(name , age):
#     print(name , age)
# student(name = "Abhishekh" , age = 20)
# student("Abhishekh" ,20)


#Speacial Arguments

# def add(*args):
#     print(args)
# add(10,20,30)

#
# *Kwargs

# def details(**kwargs):
#     print(kwargs)
# details(name="Abhishekh", age=21)

# Q3. Create a function using *args that prints all numbers passed.


# def show_numbers(*args):
#     for num in args:
#         print(num)
# show_numbers(5, 10 , 15)

#Lambda Functions
# square = lambda x: x * x
# print(square(5))

# Q4. Create a lambda function to multiply two numbers.

# multiply = lambda x , y : x  * y
# print(multiply(4,5))

# #Recursion
# def countdown(n):
#     if n == 0:
#         print("Done")
#     else:
#         print(n)
#         countdown(n - 1)
# countdown(5)

# Q5. Write a recursive function to print numbers from 3 to 1./
#
# def countdown(n):
#     if n == 0:
#         return
#     print(n)
#     countdown(n - 1)
#
# countdown(3)

# Q1 — Basic Function + Return

# def square(num):
#     return num * num
# print(square(4))

# Q2 — Default Argument
# def greet(name = "Guest"):
#     print("Hello", name)
# greet()
# greet("Abhishekh")

# Q3 — *args (slightly logical)
# def find_max(*args):
#     largest = args[0]
#
#     for num in args:
#         if num > largest:
#             largest = num
#     return largest
# print(find_max(3, 7, 2, 9, 5))

# Q4 — Lambda + Logic
# is_even = lambda x: x % 2 ==0

# print(is_even(4))
# print(is_even(7))

# Q5 — Recursion (Final Question)
# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)
# print(sum_n(5))

# Q6 — Mixed (Function + *args + Logic)
# def sum_even(*args):
#     total = 0
#
#     for num in args:
#         if num % 2 == 0:
#             total += num
#     return total
# print(sum_even(1,2,3,4,5,6))

# Q7 — Lambda + *args + Logic (Harder)
# def count_even(*args):
#     is_even = lambda x:x % 2 == 0
#     count = 0
#
#     for num in args:
#         if is_even(num):
#             count += 1
#     return count
# print(count_even(1,2,3,4,5,6,7,8,9))

# Q8 — Recursion (Logic-Based)
def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

print(count_digits(12345))
print(count_digits(7))
print(count_digits(1000))