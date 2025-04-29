# Collection = Single variable that can store multiple values
# List = [] ordered and changeable. Duplicates OK.
# Set = {} unorderd and immutable. but add / remove okay. No Duplicates
# Tuple = () ordered and unchangeable. Duplicated OK. Faster !!!

# List
fruits = ["Apple", "Pineapple", "Strawberry", "Banana"]

print(fruits)
print(fruits[1])
print(fruits[0:3])
print(fruits[::-1])

for fruit in fruits:
    print(fruit)

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Apple" in fruits)

fruits[0] = "Litchi"
fruits.append("Apple")
fruits.remove("Litchi")
fruits.insert(1, "Litchi")
fruits.sort()
fruits.reverse()
fruits.clear()
print(fruits.index("Apple"))
print(fruits.count("Pineapple"))

print(fruits)

for fruit in fruits:
    print(fruit)

# Set
fruits = {"Apple", "Pineapple", "Strawberry", "Banana"}

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Litchi" in fruits)

fruits.add("Litchi")
fruits.remove("Apple")
fruits.pop()
fruits.clear()

print(fruits)

for fruit in fruits:
    print(fruit)

# Tuples
fruits = ("Apple", "Pineapple", "Strawberry", "Banana", "Banana")

print(dir(fruits))
print(help(fruits))
print(len(fruits))
print("Litchi" in fruits)

print(fruits.index("Pineapple"))
print(fruits.count("Banana"))

print(fruits)

for fruit in fruits:
    print(fruit)

# Shopping Cart Exercise
foods = []
prices = []
total = 0
i = 1

while True:
    food = input("Enter the Food Item (press q to quit): ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)

print()

print("--------- Your Cart ---------")

print()

for food in foods:
    print(f"{i}. {food}")
    i = i + 1

print()

for price in prices:
    total += price

print(f"Total amount: ${total}")


# 2-D Collections
fruits =    ['apple', 'orange', 'banana']
vegetable = ['carrot', 'potato', 'onion']
meat =      ['chicken', 'fish', 'mutton']

groceries = [fruits, vegetable, meat]

print(groceries[1][1])

for collection in groceries:
    for food in collection:
        print(food, end=' ')
    print()

num_pad =   ((1, 2, 3), 
            (4, 5, 6), 
            (7, 8, 9), 
            ('*', 0, '#'))

for row in num_pad:
    for num in row:
        print(num, end = ' ')
    print()


# Quiz Game
Questions = ("How many elements are there in a periodic table ?", 
            "Which animal lays the largest egg ?", 
            "What is the most abundant gas in Earth's Atmosphere ?", 
            "How many bones are there in a human body ?", 
            "Which planet in the solar system is the hottest ?")

Options = (('A: 116', 'B: 117', 'C: 118', 'D: 119'),
        ('A: Whale', 'B: Crocodile', 'C: Elephant', 'D: Ostrich'),
        ('A: Nitrogen', 'B: Oxygen', 'C: Carbon-Dioxide', 'D: Hydrogen'),
        ('A: 206', 'B: 207', 'C: 208', 'D: 209'),
        ('A: Mercury', 'B: Venus', 'C: Earth', 'D: Mars'))

Answers = ("C", "D", "A", "A", "B")

Guesses = []

Score = 0

question_no = 1
print()
print("------------ Python Quiz ------------")
print()
for question in Questions:
    print(f"{question_no}. {question}")
    print()
    for option in Options[question_no-1]:
        print(option)
    print()
    guess = input("Enter you answer: ")
    Guesses.append(guess.upper())
    if guess.upper() == Answers[question_no-1]:
        Score = Score + 1
        print()
        print("!! Correct Answer !!")
    else:
        print()
        print("!! Incorrect Answer !!", end=" ")
        print(f"The correct answer is {Answers[question_no-1]}.")

    question_no = question_no + 1
    print()

print("------------------------------------------------")
print("                    Result                      ")
print("------------------------------------------------")
print()
print("Answers: ", end="")
for y in Answers:
    print(y, end=" ")

print()
print("Guesses: ", end="")
for x in Guesses:
    print(x, end=" ")

percentage = int(Score / len(Questions) * 100)
print()
print()
print(f"Your Score = {Score}")
print(f"Score Percentage: {percentage}%")
print()
print("------------------------------------------------")

# dictionary: Collection of {key:value} pairs. Ordered and changeable. No Duplicates
capitals = {
    "USA": "Washington DC",
    "India": "Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}

print(dir(capitals))
print(help(capitals))

print(capitals.get("USA"))
print(capitals.get("Japan"))

if capitals.get("Japan"):
    print("The Capital of this Country is in the database.")
else: 
    print("The Capital of this Country is not in the database.")

capitals.update({"Germany": "Munich"})
capitals.update({"China": "Shanghai"})
capitals.pop("Russia")
capitals.popitem()
capitals.clear()

keys = capitals.keys()
print(keys)

for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)

for value in capitals.values():
    print(value)

items = capitals.items()
print(items)

for item in capitals.items():
    print(item)

for key, value in capitals.items():
    print(f"{key:10}: {value}")

print(capitals)

menu = {
    "pizza": 3.00, 
    "nachos": 4.50, 
    "popcorn": 6.00, 
    "fries": 2.50, 
    "chips": 1.00, 
    "pretzel": 3.50, 
    "soda": 3.00, 
    "lemonade": 4.25
    }

cart = []
total = 0

print("------------------Menu------------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------------------------")

while True:
    food = input("Enter the Food Item to add (Press Q to quit): ")
    if food.lower() == 'q':
        print()
        break
    elif menu.get(food) is not None:
        cart.append(food.lower())

print("---------------Your Order---------------")
for food in cart:
    total += menu.get(food)
    print(food, end = " ")
print()
print(f"Total is: {total:.2f}")
print("----------------------------------------")
print()
