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

# Ask for their name
name = input("What is your name? ")

# Remove the white spaces from the name
name = name.strip()

# Capitalize the username
name = name.title()

# Say hello to the user
print(f"Hello, {name}.")

# We dont need to write so much of code
name2 =  input("What is your name? ").strip().title()
print(f"Hello, {name2}.")

first, last = name2.split(" ")
print(f"Hello, {first}.")

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

# Conditional Statement - A one line shortcut for the if-else (Ternary Operator)
#                         Print or Assign one of the two values based on a condition.
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


# String Methods

name = input("What is your name ? ")
phone = input("Enter the phone number #: ")

result = len(name)
result = name.find("o")       # Returns the first index in the substring. (First index from left)
result = name.rfind('u')      # Returns the highest index. (First from right)
name = name.capitalize()      # It will capitalize the first index to capital letters, and the rest of them to lowercase.
name = name.upper()           # Converts all index to uppercase.
name = name.lower()           # Converts all index to lowercase
result = name.isdigit()       # Checks if the the string is consisting only of digits.
result = name.isalpha()       # True is the string only consists of alphabets and no numbers or special characters like spaces.
result = phone.count("-")     # Counts the number of the time the character has occured
phone = phone.replace("-", "")

print(name)
print(phone)
print(result)

# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits  

username = input("Enter the Username: ")
if len(username) > 12:
    print("Username is too long.")
elif not username.find(" ") == -1:
    print("Username cannot have spaces.")
elif not username.isalpha():
    print("Username must not contain any numbers.")
else: 
    print(f"Your username is {username}.")

name = "Failed"
print(type(name))
print("My name is " + name + ".")

# Concatenation (Only possible for the same type
first_name = "Failed"
last_name = "Developer"
full_name = first_name + " " + last_name
print("Hello, " + full_name)

# f strings
first_name = "Failed"
last_name = "Developer"
print("My first name is {} and my last name is {}.".format(first_name, last_name))
print(f"My first name is {first_name} and my last name is {last_name}.")

# int (Numbers without decimals)
a= 23
age += 1
print(age)
print(type(age))
# print("Your age is " + age) # Error
print("Your age is " + str(age))ge 

# float (Numbers with decimals)
height = 185.5
print("Your height is " + str(height) + " cm.")
print(type(height))

# Bool (True or false values)
human = True
print("Are you human? : " + str(human))
print(type(human))

# Multiple Assignment - Allows us to create and assign values to multiple variables in the same line of code
name, age, attractive = "Failed", 23, True
print("My name is {}, and I am {} years old. And what you heard about me being attractive is {}.".format(name, age, attractive))

Spongebob = Patrick = Sandy = Squidward = 30
print("The age of Spongebob, Patrick, Sandy and Squidward is {}.".format(Spongebob, Patrick, Sandy, Squidward))

# String Functions
name = "failed"
print(name)
print(len(name))
print(name.find("a"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("a"))
print(name.replace("a", "b"))
print(name*3)

# Type Casting = Convert the datatype of a value to another data type.
x = 1   # integer
y = 2.0 # float
z = "3" # string

# Converting the datatype to float and printing them.
x = float(x)
y = float(y)
z = float(z)
print("{}, {}, {}".format(x, y, z*3))

# Converting the datatype to integer and printing them.
x = int(x)
y = int(y)
z = int(z)
print("{}, {}, {}".format(x, y, z*3))

# Converting the datatype to string and printing them.
x = str(x)
y = str(y)
z = str(z)
print("{}, {}, {}".format(x, y, z*3))

print("X is {}, Y is {} and Z is {}".format(str(x), str(y), str(z*3)))

# Taking Inputs
name = input("What is your name: ")
age = int(input("How old are you: "))
height = float(input("How tall are you: "))
print("Hello, " + str(name))
print("You are " + str(age) + " years old")
print("You are " + str(height) + " cm tall")
print("Hello, ", end = "")
print(name)

# Using the Math Library
import math
pi = -3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
print(pow(pi, 2))
print(math.sqrt(420))
print(max(x, y, z))
print(min(x, y, z))

# Slicing - Creating a string by extracting values and elements from another string
#     indexing[] or slice()
#     [start:stop:step]
name = "Failed Developer"
first_name = name[:6]       # name[0:6}
last_name = name[7:]        # name[7:end}
funky_name = name[::2]      # name[0:end:2}
reversed_name = name[::-1]  # name[0:end:-1]
print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)
website_1 = "http://google.com"
website_2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website_1[slice])
print(website_2[slice])

# if Condition - A block of code that will only execute if a certain condition is true
age = int(input("Age: "))
if age == 100:
    print("You are a century old.")
elif age >= 18:
    print("You are an adult.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are not an adult.")

# Logical Operators (and, or, not) = used to check if two or more conditional statements are correct.
temp = int(input("What is the Temperature outside : "))
if not(temp > 30 and temp < 30):
    print("The temperature outside is good.")
    print("Go Outside")
elif not(temp > 30 and temp < 0):
    print("The temperature is bad today!")
    print("Stay Inside")

# Format Specifier: {value:flags} : give out the value based in the flags inserted. Some of the flags are:
price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

# :(number)f = round the value to the (number) of decimal places.
print(f"Price 1 is: {price1:.2f}")
print(f"Price 2 is: {price2:.2f}")
print(f"Price 3 is: {price3:.2f}")

# :(number) = allocate that many spaces
print(f"Price 1 is: {price1:10}")
print(f"Price 2 is: {price2:10}")
print(f"Price 3 is: {price3:10}")

# :03 = Allocate and zero pad that many spaces
print(f"Price 1 is: {price1:010}")
print(f"Price 2 is: {price2:010}")
print(f"Price 3 is: {price3:010}")

# :< = left justify
print(f"Price 1 is: {price1:<10}")
print(f"Price 2 is: {price2:<10}")
print(f"Price 3 is: {price3:<10}")
print(f"Price 1 is: {price1:<010}")
print(f"Price 2 is: {price2:<010}")
print(f"Price 3 is: {price3:<010}")

# :> = right justify
print(f"Price 1 is: {price1:>10}")
print(f"Price 2 is: {price2:>10}")
print(f"Price 3 is: {price3:>10}")
print(f"Price 1 is: {price1:>010}")
print(f"Price 2 is: {price2:>010}")
print(f"Price 3 is: {price3:>010}")

# :^ = center align
print(f"Price 1 is: {price1:^10}")
print(f"Price 2 is: {price2:^10}")
print(f"Price 3 is: {price3:^10}")
print(f"Price 1 is: {price1:^010}")
print(f"Price 2 is: {price2:^010}")
print(f"Price 3 is: {price3:^010}")

# :+ = puts a plus sign in front of positive values
print(f"Price 1 is: {price1:+}")
print(f"Price 2 is: {price2:+}")
print(f"Price 3 is: {price3:+}")

# := = place sign to leftmost position
print(f"Price 1 is: {price1:=}")
print(f"Price 2 is: {price2:=}")
print(f"Price 3 is: {price3:=}")

# :  = enter space between positive numbers
print(f"Price 1 is: {price1: }")
print(f"Price 2 is: {price2: }")
print(f"Price 3 is: {price3: }")

# :, = comma separator
print(f"Price 1 is: {price1:,}")
print(f"Price 2 is: {price2:,}")
print(f"Price 3 is: {price3:,}")

# Combining the flags
print(f"Price 1 is: {price1:+,.2f}")
print(f"Price 2 is: {price2:+,.2f}")
print(f"Price 3 is: {price3:+,.2f}")

# while loop - a statement that will execute its block of code, as long as its condition remains true.
name = input("Enter your name: ")
while len(name) == 0:
    print("You did not enter any name.")
    name = input("Enter your name: ")
print("Hello " + name + "!")

age = int(input("What is the age: "))
while age < 0:
    print("Age can not be negative.")
    age = int(input("What is the age: "))
print(f"Age: {age}")

food = input("Enter the food item you like ('q' to Quit): ")
while not food == 'q':
    print(f"You have {food} in your cart.")
    another_item = input("Enter the food item you like ('q' to Quit): ")
    if another_item == 'q':
        break
    else:
        food = food + ", " + another_item
if food == 'q':
    print("You have nothing in your cart.")
else:
    print(f"Your cart is : {food}.")
    print("You must proceed to pay the bill.")

print("BYE !!!!!")

# Compound Interest Rate Exercise
principle = 0
time = 0
roi = 0

while principle <= 0:
    principle = int(input("Enter the Principle: "))
    if principle <= 0:
        print("Princple can't be less than or equal to zero")

while time <= 0:
    time = int(input("Enter the amount of time (in years): "))
    if time <= 0:
        print("Time can't be less than or equal to zero.")

while roi <= 0:
    roi = float(input("Enter the rate of interest: "))
    if roi <= 0:
        print("The rate of interest can't be less than or equal to zero.")

print(f"Principle: {principle}")
print(f"Time: {time}")
print(f"Rate of Interest: {roi}")

amount = principle * pow((1 + (roi / 100)), time)

print(f"Amount after {time} year(s): ${amount:.2f}")

# Compound Interest Rate Exercise with value zero
principle = 0
time = 0
roi = 0

while True:
    principle = int(input("Enter the Principle: "))
    if principle < 0:
        print("Princple can't be less than zero")
    else:
        break

while True:
    time = int(input("Enter the amount of time (in years): "))
    if time < 0:
        print("Time can't be less than zero.")
    else:
        break

while True:
    roi = float(input("Enter the rate of interest: "))
    if roi < 0:
        print("The rate of interest can't be less than zero.")
    else:
        break

print(f"Principle: {principle}")
print(f"Time: {time}")
print(f"Rate of Interest: {roi}")

amount = principle * pow((1 + (roi / 100)), time)

print(f"Amount after {time} year(s): ${amount:.2f}")

# for loop - A statement that will execute it's block of code a fixed number of times. You can iterate over a range, string or sequence, etc.
for i in range(10):
    print(i+1)

for i in range(50, 100+1, 2):
    print(i)

for i in "Bro Code":
    print(i)

for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year !!!")

credit_card = '1234-5678-9012-3456'
for i in credit_card:
    print(i)

for x in range(1, 21):
    if x == 13:
        continue
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break
    else:
        print(x)

# Exercise: Timer Exerise
import time
my_time = int(input("Enter the remaining time: "))
for seconds in range(my_time, 0, -1):
    print(seconds)
    time.sleep(1)
print("Happy New Year!!!!")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("TIME'S UP !!!!")

# Nested Loops - The "inner loop" will finish off with its iteration before the outer loop

for x in range(3):
    for y in range(1, 10):
        print(y, end=" ")
    print()

rows = int(input("Enter the Number of rows: "))
columns = int(input("Enter the Number of columns: "))
symbols = input("Enter the Symbols: ")
for i in range(rows):
    for j in range(columns):
        print(symbols, end=" ")
    print("\n")

Loop control statement - changes loop execution from its normal execution.
break - used to terminate the loop entirely
continue - skips to the next iteration of the loop
pass - does nothing, acts as a placeholder
while True:
    name = input("Name: ")
    if name != "":
        break

phone_number = "123-456-789"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

for i in range(1, 21):
    if i == 13:
        pass
    else:
        print(i)
