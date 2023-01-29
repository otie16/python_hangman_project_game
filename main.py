# Print function
print("Hello World!")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print("""
Hello world from Gamers
Nice for u all to be here
This is a function to print multiple lines of strings
""")

print("Testing the print!\nHello from new line")
print("Hello" + " Angela")

# Data types

# String
print("Hello"[4])
print("123" + "234")

# Integer
print(123 + 345)

# Float

3.14159

# Boolean

True
False

# Checking DataType
num_char = 123
print(type(num_char))

# Type Casting or conversion
num_char = 123
print(type(str(num_char)))
print(type(float(num_char)))

# two_digit_number = input("Type a two digit number: ")
# new_string = str(two_digit_number)
# a = int(new_string[0])
# b = int(new_string[1])
# c = a + b
# print(f"{a} + {b} = {c}")
# print(c)

# BMI calculator
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
#
#
# bmi = int(weight) / float(height) ** 2
# print(int(bmi))

# mod = 6 % 4
# print(mod)

# Life in weeks
# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# years = abs(int(age) * 365 - 90 * 365)
# weeks = abs(int(age) * 52 - 90 * 52)
# months = abs(int(age) * 12 - 90 * 12)
#
# years = 90 * 365 - int(age) * 365
# weeks = 90 * 52 - int(age) * 52
# months = 90 * 12 - int(age) * 12
#
# print(f"You have {years} days, {weeks} weeks, {months} months left")

# Conditional statements
# height = 34
# if height > 23:
#     print("okay")
# else:
#     print("not okay")
#
# # BMI 2.0
# height = float(input("enter your height in m: "))
# weight = float(input("enter your weight in kg: "))
#
# bmi = round(weight / height ** 2, 1)
#
# if bmi == 18.5:
#     print(f"Your bmi is {bmi}, You are underweight")
# elif bmi <= 25:
#     print(f"Your bmi is {bmi}, You have a normal weight")
# elif bmi <= 30:
#     print(f"Your bmi is {bmi}, You are overweight")
# elif bmi <= 35:
#     print(f"Your bmi is {bmi}, You are obese")
# else:
#     print(f"Your bmi is {bmi}, You are clinically obese")

# print(int(bmi))

# Leap Year project
# year = int(input("which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year}, is a Leap Year !")
#         else:
#             print(f"{year}, is a Not Leap Year!")
#     else:
#         print(f"{year}, is a Not Leap year!")
# else:
#     print(f"{year}, is a Not leap year")

# Pizza Order
# print("Welcome to Python Pizza Deliveries!")
# size = input("What size of pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0
#
# if size == "S":
#     if add_pepperoni == "Y":
#         bill = 15 + 2
# elif size == "M":
#     bill = 20 + 3
# else:
#     bill = 25 + 3
# if extra_cheese == "Y":
#     bill += 1
# print(f"your final bill is: ${bill}")

# Treasure Island Game
# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
#
# second_res = ""
# third_res = ""
#
#
# first_res = input('You are at a crossroad where do u want to go? left or right? ').lower()
#
# if first_res == "left":
#     second_res = input("Suddenly a pool appears swim or wait? ").lower()
# else:
#     print("Game over!")
# if second_res == "wait":
#     third_res = input("While waiting you find three doors, which one do you choose blue, yellow or red? ").lower()
# else:
#     print("Game Over!")
# if third_res == "yellow":
#     print("You Win!")
# elif third_res == "blue":
#     print("Game Over!")
# elif third_res == "red":
#     print("Game Over!")


# third_res = input("While waiting you find three doors, which one do you choose blue, yellow or red").lower()


# Randomizaton and python lists
# import random
# import my_module
#
# random_number = random.randint(1, 10)
# print(random_number)
# print(my_module.pi)

# state_of_america = ["delaware", "maryland", "colorado", "utah"]
# state_of_nigeria = ["oyo", "lagos", "kogi", "edo"]

# states = [state_of_america, state_of_nigeria]
# state_of_america[0] = "ohio"
# print(state_of_america)

# row1 = ["⬜", "⬜", "⬜"]
# row2 = ["⬜", "⬜", "⬜"]
# row3 = ["⬜", "⬜", "⬜"]
#
# map_list = [row1, row2, row3]
#
# position = input("Where do you want to put the treasure? ")
# horizontal = int(position[0])
# vertical = int(position[1])
#
# map_list[vertical - 1][horizontal - 1] = "X"
# # horizonta

# up_list = map_list[1][0] = "2"

# print(map_list)

# Rock paper scissors game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# import random
#
# user_choice = int(input("What do you choose? Type 0 for Rock, Type 1 for Paper, Type 2 for Scissors. "))
# computer_choice = random.randint(0, 2)
#
# if user_choice == 0 and computer_choice == 0:
#     print(rock)
#     print(f"computer choice: {rock}")
#     print("It's a draw")
# elif user_choice == 1 and computer_choice == 1:
#     print(paper)
#     print(f"computer choice: {paper}")
#     print("It's a draw")
# elif user_choice == 2 and computer_choice == 2:
#     print(scissors)
#     print(f"computer choice: {scissors}")
#     print("It's a draw")
# if user_choice == 0 and computer_choice == 1:
#     print(rock)
#     print(f"computer choice: {paper}")
#     print("You lose")
# else:
#     print("you win")

# print(computer_choice)


# For Loop
# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#     # Converting the inputs to integer
#   student_heights[n] = int(student_heights[n])
# print(student_heights)
#
# counter = 0
# height_sum = 0
# for student_height in student_heights:
#     counter += 1
#     height_sum += student_height
#     # print(student_height)
# print(height_sum)
# average = height_sum / counter
# print(round(average))


# Highscore quiz

# 🚨 Don't change the code below 👇
# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
# # 🚨 Don't change the code above 👆
#
# #Write your code below this row 👇
# temp_highscore = 0
# for score in student_scores:
#     if score >= temp_highscore:
#         temp_highscore = score
# print(temp_highscore)

# # FizzBuzz game
# for i in range(1, 101):
#     if i % 5 == 0 and i % 3 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


#Password Generator Project
import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# password = ""
# for letter in range(0, nr_letters):
#     rand_letter = random.choice(letters)
#     password += rand_letter
#
# for symbol in range(0, nr_symbols):
#     rand_symbol = random.choice(symbols)
#     password += rand_symbol
#
# for number in range(0, nr_numbers):
#     rand_number = random.choice(numbers)
#     password += rand_number
# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password_list = []
# for letter in range(0, nr_letters):
#     rand_letter = random.choice(letters)
#     password_list += rand_letter
#
# for symbol in range(0, nr_symbols):
#     rand_symbol = random.choice(symbols)
#     password_list += rand_symbol
#
# for number in range(0, nr_numbers):
#     rand_number = random.choice(numbers)
#     password_list += rand_number
#
# random.shuffle(password_list)
# print(password_list)

# converting password back to a string
# str_password = ""
# for char in password_list:
#     str_password += char
#
# print(f"Your Password is: {str_password} ")



# if front_is_clear():
#     while front_is_clear():
#         keep_moving()
# elif at_goal():
#    while not at_goal:
#        jump()
# else:
#     while wall_in_front():
#         jump()

#Checking if letter is in string
# dog = "beggar"
# if "b" in dog:
#     print("yes")

#HANGMAN PROJECT
#Step 1

word_list = ["baboon", "cadavier", "platoon", "inspect"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# print(chosen_word)
# chosen_word = word_list[random_index]
# print(chosen_word)
chosen_word = random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# user_guess = input("Guess a letter to complete the word: ").lower()
# print(user_guess)
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# for i in range(0, len(chosen_word)):
#     if user_guess == chosen_word[i]:
#         print("Right guess, keep going")
#     else:
#         print("Wrong guess, you have a few more guesses")

# word = "bagoon"
# blank = "_" + " "
# blanks = " "
# what = type(blank)
# for i in word:
#     blanks += blank
# created_list = blanks.split()
# created_list[2] = "a"
# print(created_list)

#Step 2

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.


#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.


blanks = []
for i in chosen_word:
    blanks += "_"

game_over = False
while not game_over:
    guess = input("Guess a letter: ").lower()

    for index in range(0, len(chosen_word)):
        # guess = input("Guess a letter: ").lower()
        if guess == chosen_word[index]:
            blanks[index] = guess
            # print(created_list)
    print(blanks)
    if "_" in blanks:
        game_over = False
    else:
        game_over = True



