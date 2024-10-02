#100 day python coding
from nturl2path import pathname2url
from posixpath import splitext
from random import randint

# test = {
#         # 'data_input' : {
#      'list': [1, 2, 3,4 ,5, 6, 7, 8, 9, 10, 11, 23],
#      'query' : 4
# }
# output = ' ',
# }

# for item in test:
#     if item == query[0] :
#        print( output.count(test))


#find the position of a given number

# data = int(input("Input the list of numbers: "))
# list = []
# for i in range(0,data):
#     elements = int(input())
#     list.append(elements)
# print(list)    # taking list as a user data
# query = int(input(' Input the expected output: '))
#
# def locate_value(list , query):
#    for item in list:
#     if item == query:
#      value = list.index(item)
#      return value
#    else:
#         return -1
# output = locate_value(list , query)
# print(output)

#GCD Test case

# first = int(input('Input the first number: '))
# second = int(input('Input the second number: '))
#
# def gcd(first, second):
#     list = []
#     for i in range(1, first+1):
#       if first%i ==0:
#         list.append(i)
#     # return list
#     list2= []
#     for j in range(1, second+1):
#        if second%j == 0:
#         list2.append(j)
#     # return list2
#     max = []
#     for i in list:
#         if i in list2:
#           max.append(i)
#
#     return max[-1]


# print(gcd(first, second))

# #Other way to solve this
# def gcd(m, n):
#     cf = []
#     for i in range(1, max(m,n)+1):
#         if(m%i)==0 and (n%i)==0:
#             cf.append(i)
#     return cf[-1]
# output = gcd(8, 12)
# print(output)
#
# #  other simple way
# def gcd(m, n):
#
#     for i in range(1, min(m,n)+1):
#         if(m%i)==0 and (n%i)==0:
#             value = i
#     return value
# output = gcd(8, 12)
# print(output)

#while loop
# def gcd(m,n):
#     if m<n:
#         (m,n) = (n,m)
#     while (m%n!=0):
#         diff = m-n
#         (m,n) = (max(n,diff), min(n,diff))
#     return n
# print(gcd(8,12))
#
# #while loop
# def gcd(m,n):
#     if m<n :
#         (m,n)=(n,m)
#         while m%n!=0:
#             (m,n)=(n,m%n)
#     return n
# print(gcd(8,21))
#
# #Printing on the another line by using three (') or we can do that with \n as well
# print('''
# Hello my name is Abhigyan Punj
# I am 26 years old
# I love cars
# My dream is to be in F1''')
#
# print('Hello my name is Satyam\nI am randwa')
#
# print('hello' + ' satyam')

# name = input("Enter your name: ")
# print(f"hello {name}!")   #formating
# print('hello' +name+ '!')

# username = len(input("Enter your name: "))
# print(username)

# user_city= input("Enter the city you are grow up in: ")
# user_pet = input("Enter your pet name: ")
# print(f'Your band name could be {user_city} {user_pet}')

# total = int(input("The total amount of the bill: $ "))
# person = int(input('number of person in which we split: '))
# percentage = int(input('What percent tip we want to pay, 10% 20% or 30%: '))
# def bill_pay(total, person , percentage):
#     percentage_calculator = float(((percentage/100)*total))
#     split = float(percentage_calculator/person)
#     return split
# print(bill_pay(total, person, percentage))

# name = "Satyam"
# print(name[1:-1])

# name = len(input('Enter your name:'))
#
# print(f'Number of letter in your name: {name} ')

# value = 1.65234678
# print(round(value,2)) #rounding method upto 2 digits
# print(round(value))
#
# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)
# if bmi < 18.5:
#     print('underweight')
# elif bmi >= 18.5 and bmi < 25:
#     print('normal weight')
# else:
#     print(' Overweight')

#pizza order
# print('Welcome to python pizza delivery')
# size_pizza = input('What size of pizza you want?, Small, Medium or Large? ')
# topping_pizza = input(' What type of topping you like?, Soft or crushed? ')
# extra_pizza = input(' Do you want extra cheese? Yes or No ')
# def pizza(size_pizza, topping_pizza, extra_pizza):
#     if size_pizza == 'Small':
#         bill = int(15)
#     if size_pizza == 'Medium':
#         bill = int(20)
#     elif size_pizza == 'Large':
#         bill = int(25)
#     if topping_pizza == 'Soft':
#         if bill !=0:
#           bill += int(2)
#     elif topping_pizza == 'crushed':
#         if bill !=0:
#           bill += int(3)
#     if extra_pizza == 'Yes':
#         if bill !=0 :
#            bill += int(1)
#     elif extra_pizza == 'No':
#         if bill !=0:
#          pass
#     else:
#         print("no data")
#     return bill
#
#
# output = pizza(size_pizza,topping_pizza,extra_pizza)
# print(f'Your total bill amount is ${output}')

# path game
# print('''
#
#                          _______ _______ _______
#                         |   |   |    ___|    |  |
#                         |       |    ___|       |
#                         |__|_|__|_______|__|____|
#     _______ ______ _______ _______    _______ _______ ______ _______ _______
#    |    ___|   __ \       |   |   |  |    ___|   _   |   __ \_     _|   |   |
#    |    ___|      <   -   |       |  |    ___|       |      < |   | |       |
#    |___|   |___|__|_______|__|_|__|  |_______|___|___|___|__| |___| |___|___|
#
#                            _______________________
#                          //     _..--~~~--.._    \\
#                         ||_____/ |  |  |  |  \ __/ |
#                         ||    /   ________    \    |
#                         ||__ /   /........\    |   |
#                         |   |   /........  \   |   |
#    _____________________|  _|  /.........   \  |   |________________
#     ;   . . .   .       |_/ | |.........     | |   | .''."...  ... .
#    ___   ..~.         _.'  /| |........      | |   |         . ~
#     .      '     .   / \_.' | |........      | |   |\ ~.   ._..---._
#                     |. /|    \ \........    / /    |/ .    /\      /\
#       '""" ... ~~~  | \||  _.'\ \........  / /'._ _|      // ~-._./ -\
#     ..~             |  |_.~\\  \ \________/ / // '.|     /__       __.\
#     ___   ..~.      |_.~    \   \__________/  /   _ ~-.  ~~~~..  ~~~~~.
#                    .~ -.     \__.---.________/   ______\.
#    .''."...  ... ./\        _|      |---|  = |__ \__\===\   '""" ... ~~~
#                  /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
#      ..~        / .   \      |=     |___|    ||       __. \
#                /           _ |_______________|   _.        \
#    .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
#              /          '' /   \      /         \           /\
#    ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
#            /            /    / \\ --  _____//          ~ - .   \
#     ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
#          /   ___     ./|__  / _/   (_____ / \\  .          \ ~  /   .
#      .  /___////_   /  |   / _/    (_____ \  \\       _./ .._  /~-
#        /___/__/_ \ /  _|  /__/ _-- (_____  \:.\\______________/        ._
#    _  /         \ /_.' | /  /       (_________/ ~~-|
#      /           //   _|/  /-              .    __ |..~. _____ -.. '  "
#    ..\==========/'   \_/ _/  __      ___..     /  \|
#        / _____  \'.______/___....------......__\__/|
#    '  |          \     |\__________________|__|___/|  ~~~~~..   - ~  '
#     ~ |        _  \   /~      \     \ --  /         \
#       | | | | | \_|  |   \     \ ~      //           |
#    _. |_| | | | .    |-----..   \       /  /-      __|..~. _____ -.. '  "
#         |_|_|_|   _. |       \_  \\ _ ./          ___|
#     ~~~  ..   - ~  ' |         \__\___/__...------   |  ~~~~~..   - ~  '
#                      |  .-         | | .       __    |
#                      |     __..    | |    ______     |      .     ~
#   ..~. _  __ -.. '   \           __| |   |      |    | _        .
#                      /             | | ~ |__.___|.   |
#                      |    __       | |   |      |    |              .. '
#     ~~~~~..   - ~  ' | ''          / \   |      |    |___     __.
#     ....   -         |  _____...   | |   \______/    |  ~~~~~..   - ~  '
#                      | /        '--| |      ~~       |
#        ~..   - ~  '  |/            | |    __----  .. |   .      .     _
#                      ||____......._| |               |
#                      |----         | |               |  ~~~~~..   - ~  '
#      '""" ... ~~~    |       -.    | |       _..     |
#                      | ..         // |               | _~"".    .
#                      |          -  \ | __----.   ..  \
#     ~~~..   - ~  '   |_____________| |_______________/
#                      \_____________| |______________/   '    ...  __  ~
#                       /     ----- \   /----------- \
#      __~~..   - ~  ' /___      ----\ /--...___      \
#                     /    ..--      | | __..     ___./  .     .   ~
#         - ~  '..    \  __________./  |_____________/  .   - ~  ' ~~~~
#     ..._____~~~~~~JRO\___________/    \___________/  -_______...._____
#   ..            ___ . ~~~~~~~~~~~.   \ ~~~~~~~~~~~~~...      _  ~
#    __    ....         ''        ...""       ....'''   )
# print('Welcome to nowhere')
# def game():
#
#       path1 = input('Choose your path?, left or right ').lower()
#       if path1 == 'right':
#         print('you are in the wrong room\n, game over')
#       elif path1 == 'left':
#         print('Going to the next stage of the game')
#         path2 = input('Do you want to swim or wait for the boat ').lower()
#         if path2 == 'swim':
#            print('You have eaten by the master\n,game over')
#         elif path2 == 'wait':
#           print('Cong you are on the next stage')
#           path3 = input('Choose your door?, red, blue or yellow ').lower()
#           if path3 == 'Blue':
#             print('Eaten by the beast\n, game over')
#           elif path3 == 'red':
#             print('You have enter in the burning room\n, game over')
#           elif path3 == 'yellow':
#             print('You won')
#           else:
#               print('You habe enter wrong input\ngame over')
#         else:
#             print('You habe enter wrong input\ngame over')
#       else:
#          print('You habe enter wrong input\ngame over')
#
# game()
# print(test.stage1())
# print(test.stage2())
# print(test.stage3())


# pizza order

# print('Welcome to python pizza delivery')
# size_pizza = input('What size of pizza you want?, small, medium or large? ').lower()
# topping_pizza = input(' What type of topping you like?, soft or crushed? ').lower()
# extra_pizza = input(' Do you want extra cheese? yes or no ').lower()
#
#
# def pizza(size_pizza, topping_pizza, extra_pizza):
#     bill = 0
#     if size_pizza =='small':
#       bill = 15
#     elif size_pizza == 'medium':
#       bill = 20
#     elif size_pizza == 'large':
#       bill = 25
#     else:
#       return "Invalid pizza size"
#     if topping_pizza == 'soft':
#         bill += 2
#     elif topping_pizza == 'crushed':
#
#         bill += 3
#     else:
#         return "Invalid input"
#     if extra_pizza == 'yes':
#
#         bill += 1
#
#     return bill
#
#
# output = pizza(size_pizza, topping_pizza, extra_pizza)
# if isinstance(output, int):
#     print(f'Your total bill amount is ${output}')
#  else:
#     print(output)


import random

# random_play = randint(1, 10)    #give random int
# print(random_play)
#
# rand_game = random.random()*10     #give random floating value, *10 means it will go upto 10 but not include 10.
# print(rand_game)
#
# # rand_play = random.uniform(1, 10)    #give random floating value, 1 and 10 is the range of it, it is not sure either it can give 10 or not
# # print(rand_play)
#
# # rand_head_tail = randint(0,1)
# # if rand_head_tail == 0:
# #     print('head')
# # else:
# #     print('tail')
#
#
#
# #bill pay
# friends = ['Alice', 'Bob', 'Charlie', 'David', 'Emanuel']
# #Option 1
# # random_select = randint(0,4)
# # if random_select == 0:
# #     print(friends[0])
# # elif random_select == 1:
# #     print(friends[1])
# # elif random_select == 2:
# #     print(friends[2])
# # elif random_select ==3:
# #     print(friends[3])
# # elif random_select == 4:
# #     print(friends[4])
# # else:
# #     print('Wrong name')
#
# #Option 2
# print(random.choice(friends))
#
# #nested list
# first_name = [ 'Abhigyan ', 'Satyam', 'Ravi', 'Rajdev']
# surname = ['Punj', 'Kashyap', 'Kumar', 'Randi']
# name = [first_name,surname]
# print(name)

# Stone paper game
# def rock_paper_seizer():
#      rock = '''
#               _______
#            ---'   ____)
#                 (_____)
#                 (_____)
#                  (____)
#             ---.__(___)
#             '''
#
#
#      paper = '''
#                     _______
#                  ---'   ____)____
#                            ______)
#                           _______)
#                           _______)
#                    ---.__________) '''
#
#      seizer = '''
#                      _______
#                   ---'   ____)____
#                             ______)
#                         __________)
#                         (____)
#                    ---.__(___)
#                   '''
#      user_input = int(input('what do you choose? 0 is Rock, 1 is Paper and 2 is Seizer '))
#      if user_input == 0:
#          print('Your choice:')
#          print(rock)
#      elif user_input == 1:
#          print('Your choice:')
#          print(paper)
#      elif user_input == 2:
#          print('Your choice:')
#          print(seizer)
#      else:
#          print("Invalid choice. Please choose 0, 1, or 2.")
#          return
#
#      computer = random.randint(0, 2)
#      if computer == 0:
#          print('computer choice:')
#          print(rock)
#      elif computer == 1:
#          print('computer choice:')
#          print(paper)
#      elif computer == 2:
#          print('computer choice:')
#          print(seizer)
#
#      if user_input == computer :
#           print('match draw!')
#      elif (user_input == 0 and computer == 1) or (user_input == 1 and computer == 2) or (user_input == 2 and computer == 0) :
#           print('you lost')
#      elif (user_input == 0 and computer == 2) or (user_input == 1 and computer == 0) or (user_input == 2 and computer == 1):
#           print('you won')
#      else:
#            print('wrong input')
#
#
# rock_paper_seizer()

# find the max score in range of scores
# score = [12, 23, 44, 90, 99, 30, 20, 60, 70, 10 , 5, 40]
# max = 0
# score.append(100)
# for item in score:
#     if item > max:
#         max = item
# print(max)

# add the number from 1 to 100
# add = 0
# for number in range(1, 101):
#     add += number
# print(add)

# for number in range(1, 100, 2):  #here the code is not taking 1 after 1 it is take 1 , 3, 5, 7, 9, 11(means gap of 2)
#     print(number)

#  FizzBuzz game
# for number in range(1,101):
#     if number%3 == 0 and number%5 ==0:
#         print('FizzBuzz')
#     elif number%5 == 0:
#         print('Buzz')
#     elif  number%3 ==0:
#         print('Fizz')
#     else:
#         print(number)

# Create a password
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
# password_generation = []
# for i in range(nr_letters):
#     password_generation.append(random.choice(letters))
# for j in range(nr_symbols):
#     password_generation.append(random.choice(symbols))
# for k in range(nr_numbers):
#     password_generation.append(random.choice(numbers))
# random.shuffle(password_generation)
# print(password_generation)
# password= ''.join(password_generation)   # take the value from the list and concertinate them
# print(password)

# robot game
# def move_robot():
#     move()
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def turn_to_left():
#     turn_left()
#
# def jump():
#     move_robot()
#     turn_to_left()
#     move_robot()
#     turn_right()
#     move_robot()
#     turn_right()
#     move_robot()
#     turn_to_left()
#
# for i in range(0, 6):
#     jump()
#
# number_of_hurdles = 6
# while number_of_hurdles >0:
#     jump()
#     number_of_hurdles -=1
#     print(number_of_hurdles)
#
#
# # robot game, when the finish line unknown
#
# def move_robot():
#     move()
#
#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def turn_to_left():
#     turn_left()
#
#
# def jump():
#     move_robot()
#     turn_to_left()
#     move_robot()
#     turn_right()
#     move_robot()
#     turn_right()
#     move_robot()
#     turn_to_left()
#
#
# number_of_hurdles = 6
# while number_of_hurdles > 0:
#     jump()
#     if at_goal():
#         break
#     number_of_hurdles -= 1
#     print(number_of_hurdles)
#
# # game of puzzle
# def move_robot():
#     move()

#
# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
#
#
# def turn_to_left():
#     turn_left()
#
#
# def jump():
#     while wall_on_right():
#
#         if front_is_clear():
#             move()
#         else:
#             turn_left()
#     while right_is_clear():
#         if wall_in_front():
#             turn_right()
#
#         else:
#             turn_left()
#
#
# while not at_goal():
#     if right_is_clear():
#         turn_right()
#         move()
#     elif front_is_clear():
#         move_robot()
#     else:
#         turn_left()
import random

from Tools.scripts.dutree import display



stages = [
    """
       --------
       |      |
       |      
       |    
       |      
       |     
       |
    --------
    You have total 6 lives
    """,
    """
       --------
       |      |
       |      O
       |    
       |      
       |     
       |
    --------
    You have 5/6 lives remaining
    """,
    """
       --------
       |      |
       |      O
       |      |
       |      
       |     
       |
    --------
    You have 4/6 lives remaining
    """,
    """
       --------
       |      |
       |      O
       |     /|
       |      
       |     
       |
    --------
    You have 3/6 lives remaining
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |      
       |     
       |
    --------
    You have 2/6 lives remaining
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / 
       |     
       |
    --------
    Oh no you have 1/6 live left now
    """,
    """
       --------
       |      |
       |      O
       |     /|\\
       |     / \\
       |     
       |
    --------
    hangman died!..... 
    """
       ,
    """
     --------
       |      
       |
       |      O
       |     /|\\
       |     / \\
       |     
       |
    --------
    happy happy happy, hangman survived. 
    """
]
list = ['stortage', 'analytic', 'habilimented', 'schadenfreude', 'arrant', 'antidisestablishmentarianism', 'round', 'colonel', 'conception', 'narrative', 'economics', 'blinker', 'book', 'rural', 'accessory', 'artless', ]
chosen_word = random.choice(list)
#print(chosen_word)
placeholder = chosen_word
for item in chosen_word:
    placeholder = placeholder.replace(item,'_')
print(placeholder)
def correct_words():
    wrong = 0
    game_over = False
    list_char =[]
    while not game_over:
        user_input = input('enter the letter: ').lower()
        print(user_input)
        display = " "

        for item in chosen_word:
            if item == user_input:
                display += item
                list_char.append(item)

            elif item in list_char:
                 display +=item

            else:
                display += "_"


        print(display)

        if user_input not in chosen_word:
            wrong += 1
            if wrong == 6:
                game_over = True
                print('you lose')
                print(chosen_word)
        print(stages[wrong])
        if '_' not in display:
            game_over = True
            print('You won')
            print(stages[7])

correct_words()
