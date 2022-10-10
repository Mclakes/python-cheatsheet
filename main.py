# from email import message


# course = "python for Beginners"
# another = course[:]
# print(course[-2])
# print(another) 
# message = f"{course} {another}"
# print(message)

# input("i need the word good? ")

# secret_number = 9
# guess_count = 0
# guess_limit = 3
# while guess_count < guess_limit:help
#     guess = int(input('Guess: '))
#     guess_count += 1
#     if guess == secret_number:
#         print('you won!')
#         break
# else: 
#     print("try again later")

# command = ""
# started = False
# while True:
#     command = input ("> ").lower()
#     if command == "start":
#         if started:
#             print("car is already started")
#         else:
#             started = True
#             print("Car started...")
#     elif command == "speed":
#         if not started:
#             print("car has not been kicked")
#         else:
#             started == True
#             print("car is accelerated")        
#     elif command == "stop":
#         if not started:
#             print("car has not been started")
#         else:
#             started = False
#             print("Car stopped.")
#     elif command == "help":
#         print("""
# start- to stop the car
# speed- to accelerate
# stop- to stop thr car
# quit- to quit
#             """)
#     elif command == "quit":
#         break
#     else:
#         print(f"Sorry, I cant recognize the input -{command }-")

# prices= [10, 20, 30]
# total = 0
# for price in prices:
#     total += price
# print(f"Total: {total}")

# for x in range(3):
#     for y in range(3):
#         print (f'({x}, {y})')

# numbers = [5, 2, 5, 2, 3]
# letter = "x"
# for number in numbers:
#     output = ''
#     for count in range(number):
#         output += 'x'
#     print(output)
    
# names = ["john", "Bob", "mosh", "sarah", "mary"]
# names[0] = "Jon"
# print(names)

# numbers = [3, 6, 20, 8, 4, 10]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# # print(matrix[2][2])
# for row in matrix:
#     for item in row:
#         print(item)

# numbers = [5, 2, 1, 7, 5, 4]
# # numbers.append(20)
# # numbers.insert(0, 10)
# # numbers.remove(5)
# # numbers.clear()
# # numbers.pop()
# # lekan = numbers.index(5)
# # lekan = numbers.count(5)
# # numbers.sort()
# # numbers.reverse()
# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)
# # print(lekan in numbers)
    
# numbers = [2,2,4,6,3,4,6,1]
# unique = []

# for number in numbers:
#     if number not in unique:
#         unique.append(number)
# print(unique)  

# customer = {
#     "name" : "john smith",
#     "age" : 30,
#     "is_verified" : True
# }
# customer["name"] = "rasheed"
# print(customer.get("name",  "bankole"))

# phone = input("Phone: ")
# digit_mapping = {
#     "1": "One",
#     "2": "Two",
#     "3": "Three",
#     "4": "Four"
# }
# output = ""
# for ch in phone:
#     output += digit_mapping.get(ch, "!") + " "
# print(output)

# message = input("> ")
# words = message.split(" ")
# emojis = {
#     ":)": "😂",
#     ":(": "😏"
# }
# output = ""
# for word  in words:
#     output += emojis.get(word, word) + " "
    
# print(words)
# print(output)

# def great_user (first_name, last_name):
#     print(f'hi {first_name} {last_name}')
#     print('welcome aboard')
# print('start')
# great_user("lekan", "rasheed")
# great_user( last_name="Bankole", first_name="ayomide")
# # calc_cost(total=50, shipping=5, discount=0.1)
# print("stop")

# def square(number):
#     print(number * number)
# square(3)

# def emoji_converter(message):
#     words = message.split(" ")
#     emojis = {
#         ":)": "😂",
#         ":(": "😏"
#     }
#     output = ""
#     for word in words:
#         output += emojis.get(word, word) + " "
#     return output


# message = input("> ")
# print(emoji_converter(message))

# try: 
#     age = int(input('Age: '))
#     income = 20000
#     risk = income/age
#     print(age)
# except ZeroDivisionError:
#     print("age cannot be zero")
# except ValueError: 
#     print('invalid value')

# class Point: 
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
        
#     def move (self):
#         print("move")
    
#     def draw (self):
#         print("draw")
        
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
# print(point1.y)
# point1.draw()

# point2 = Point()
# point2.x = 1
# print(point2.x)
# point2.move()
# point2.draw()

# point = Point(10, 20)
# point.x = 11
# print(point.x)
# print(point.y)

# class Person:
#     def __init__(self, name, blood):
#         self.name = name
#         self.blood = blood
#     # def name(self):
#     #     print("self")
#     def talk(self):
#         print(f'Hi, I am {self.name} ')
#         print(f'i am of {self.blood} ')        
# john = Person("John Smith", "A+")
# # print(john.name, john.blood)
# john.talk()
# bob = Person ("Bob Smith", "B-")
# bob.talk()

# class mammal:
#     def walk(self):
#         print("walk")
# class Dog(mammal):
#     pass
# class Cat(mammal):
#     def annoy(self):
#         print('cat can be so annoying')
#     pass

# dog1 = Dog()
# dog1.walk()
# Cat().annoy()

# import converter

# from converter import lbs_to_kg

# print(converter.kg_to_lbs(70))
# print(lbs_to_kg(70))

# numbers = [3, 6, 20, 8, 4, 20]
# from converter import find_max


# print(find_max(numbers))
# print(max(numbers))

# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()

# from ecommerce.shipping import calc_shipping
# calc_shipping()

# from ecommerce import shipping
# shipping.calc_shipping()

# import random

# for i in range(1):
#     print(round(random.randint(10, 20)))
    
# members = ["Olalekan", "Ayomide", "Bankole", "Rasheed", "Ayobami"]
# leader = random.choice(members)
# print(leader)

# import random

# for i in range(1):
#     number1 = random.randint(1,10)
#     number2 = random.randint(1,10)
#     print(f'({number1}, {number2})')

# import random
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
# dice = Dice()
# print(dice.roll())

# from pathlib import Path
# path = Path()
# path = Path("emails")
# print(path.mkdir())
# print(path.rmdir())
# print(path.glob("*.py"))
# for file in path.glob("*.py"):
#     print(file)
# for file1 in path.glob("*.html"):
#     print(file1)
# for file2 in path.glob("*.js"):
#     print(file2)
# for file in path.glob("*"):
#     print(file)

