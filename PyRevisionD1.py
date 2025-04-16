print("I love pizza")
print("It's really good")
from idlelib.editor import index2line

# Variables - It is a container for a value and behaves as the value it contains
# Strings
first_name = "Failed"
food = "Nutri Kulcha"
email = "thatfaileddeveloper@gmail.com"

print(f"Hello, {first_name}")
print(f"Your favorite food is {food}")
print(f"Your email address is : {email}")

# Integers
age = 23
num_of_students = 30

print(f"Your Age is: {age}")
print(f"How many Students are there ? {num_of_students}")

# Float
fees = 79999.99
gpa = 9.44
distance = 3.5

print(f"Your fees (in $) is : {fees}")
print(f"Your GPA is : {gpa}")
print(f"You live {distance} miles away.")

# Boolean
is_student = True

if is_student: 
    print("You are a Student.")
else:
    print("You are not a Student.")

is_online = True
if is_online:
    print("You are online.")
else:
    print("you are not online.")

# Typecasting - The process of conerting one datatype to another using str(), int(), float(), bool()
name = "Failed Developer"
age = 23
gpa = 9.44
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print("Converting GPA to Int - {}".format(gpa), end = ", ")
print(type(gpa))

age = float(age)
print("Conerting the Age to Float - {}".format(age), end = ", ")
print(type(age))

age = str(age)
print("Conerting the Age to String - {} {} {} {}".format(age[0], age[1], age[2], age[3]), end = ", ")
print(type(age))

# input() - A function that prompts the user to enter the data. Returns the entered data as a string.
name = input("What is your name ? : ")
age = int(input("What is your age ? : "))

age += 1

print(f"Your name is {name}, and you will turn {age} years old on your birthday.")

# Exercise 1 - Build a Rectangle area calculator
length = float(input("Enter Length: "))
breadth = float(input("Enter Breadth: "))
area = length * breadth
print(f"Area of the Rectangle: {area} cm².")

# Exercise 2 - Shopping Cart Program
item = input("Enter the name of the product: ")
price = float(input("Enter the price: "))
quantity = int(input("Enter the Number of items: "))

total = price * quantity

print(f"You have bought {quantity} {item} at a price of {price} each.")
print(f"Total Cost: $ {total}")

# Madlibs game - word game where you create sentences by filling in the blanks with random words.

adjective1 = input("Enter an adjective (description): ")
noun1 = input("Enter a noun (person, place or thing): ")
adjective2 = input("Enter an adjective (description): ")
verb1 = input("Enter the verb ending with 'ing': ")
adjective3 = input("Enter an adjective (description): ")

print(f"Today! I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}.")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}.")

# Maths and Arithmetic
friends = 0
print(friends)

friends = friends + 1
friends += 1
print(friends)

friends = friends - 2
friends -= 2
print(friends)

friends = friends * 2
friends *= 2
print(friends)

friends = friends / 2
friends /= 2
print(friends)

friends = friends ** 2
friends **= 2
print(friends)

x = 3.14
y = -4
z = 5

result = round(x)
result = abs(x)
result = pow(4, 3)
result = max(x, y, z)
result = min(x, y, z)

print(result)

# Math Library
import math

x = 9.9

print(math.pi)
print(math.e)
result = math.ceil(x)
result = math.floor(x)
result = math.sqrt(x)

print(result)

radius = float(input("Enter the radius of the Circle: "))

circumference = 2 * math.pi * radius

area = math.pi * pow(radius, 2)

print(f"Circumference of the circle is: {round(circumference, 2)} cm")

print(f"Area of the Circle is: {round(area, 2)} cm²")

# Pythogoras Theorem
a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

print(f"Side C: {round(c, 2)}")

# if = Do some code IF some condition is True
#      Else do something else

# Example 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up!")
elif age >= 18: 
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet!")
else:
    print("You must be above the age of 18 to sign up!")

# Example 2
response = input("Would you like some food? (Y/N): ")

if response == "Y":
    print("Have some food.")
else:
    print("No food for you.")

# Example 3
for_sale = True

if for_sale:
    print("This item is for sale.")
else:
    print("This item is not for sale.")

# Example 4
online = True

if online:
    print("The user is online.")
else:
    print("The user is offline.")

# Python Calculator
sign = input("Enter the Sign (+ - * /): ")

num1 = float(input("Enter the Number 1: "))
num2 = float(input("Enter the Number 2: "))

if sign == '+':
    result = num1 + num2
    print(round(result, 3))
elif sign == '-':
    result = num1 - num2
    print(round(result, 3))
elif sign == '*':
    result = num1 * num2
    print(round(result, 3))
elif sign == '/':
    result = num1 / num2
    print(round(result, 3))
else:
    print(f"{sign} is not a valid symbol.")

# Weight Conversion
weight = float(input("Enter your weight: "))
unit = input("Enter the unit Kilogram or Pounds? (K or L): ")

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
elif unit == 'L':
    weight = weight / 2.205
    unit = 'Kgs.'
else:
    print(f"{unit} is not a valid unit of measurement.")

print(f"Your Weight is: {round(weight, 1)} {unit}")

# Python Temperature Conversion
temp = float(input("Enter the temp.: "))
unit = input("Enter the unit Celsius or Fahrenheit? (C or F): ")

if unit == 'C':
    temp = round((temp * 9) / 5, 1) + 32
    unit = '°F.'
elif unit == 'F':
    temp = round(((temp - 32) * 5) / 9, 1)
    unit = '°C.'
else:
    print(f"{unit} is not a valid unit of measurement.")

print(f"Temperature in {unit} is: {temp}{unit}")

# Logical Operators - evaluate multiple conditions (or, and, not)
#                or - atleast one condition is true
#               and - Both/all conditions have to be true
#               not - inverts the condition (not true, not false)

temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("The scheduled event is cancelled.")
else:
    print("The event is happening as per the schedule.")

temp = -1
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is Hot outside 🥵")
    print("It is Sunny outside ☀️")
elif temp <= 0 and is_sunny:
    print("It is Cold outside 🥶")
    print("It is Sunny outside ☀️")
elif 28 > temp > 0 and is_sunny:
    print("It is Warm outside 😊")
    print("It is Sunny outside ☀️")
elif temp >= 28 and not is_sunny:
    print("It is Hot outside 🥵")
    print("It is Cloudy outside ☁️")
elif temp <= 0 and not is_sunny:
    print("It is Cold outside 🥶")
    print("It is Cloudy outside ☁️")
elif 28 > temp > 0 and not is_sunny:
    print("It is Warm outside 😊")
    print("It is Cloudy outside ☁️")

# Conditional Statement - A one-line shortcut for the if-else (Ternary Operator)
#                         Print or assign one of the two values based on a condition.
#                         X if condition else Y

num = 5
print('Negative' if num < 0 else 'Positive')

result = "Even" if num % 2 == 0 else "Odd"
print(result)

a = 3
b = 8
max_num = a if a > b else b
min_num = a if b > a else b
print(max_num)
print(min_num)

age = 21
status = "Adult" if age >= 18 else "Child"

temperature = 30
weather = "Hot" if temperature >= 28 else "Cold"
print(weather)

user_role = "Guest"
access_level = "Full Access" if user_role == 'admin' else "Limited Access"
print(access_level)
max_num = a if a > b else b
print(max_num)
