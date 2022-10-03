import random

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

#Write your code below this line 👇
print("We are going to play rock, paper scissors.")
print("Type below 0 for Rock, 1 for Paper, or 2 for Scissors.")
print("What will be your choice?")
users_choice = int(input())

choice1 = 0
choice2 = 1
choice3 = 2
options_choices = [choice1, choice2, choice3]
screen_options = [rock, paper, scissors]

rock1 = options_choices[0], screen_options[0]
paper1 = options_choices[1], screen_options[1]
scissors2 = options_choices[2], screen_options[2]

if users_choice in rock1:
    print("Your choice is: ")
    print(rock)

elif users_choice in paper1:
    print("Your choice is: ")
    print(paper)
else:
    print("Your choice is: ")
    print(scissors)

options1 = [0, 1, 2]
num_items = len(options1)
random_choice = random.randint(0, num_items - 1)
computer_options = options1[random_choice]

if users_choice > computer_options:
    if computer_options in rock1:
        print("Your opponents choice is: ")
        print(rock)
    elif computer_options in paper1:
        print("Your opponents choice is: ")
        print(paper)
    else:
        print("Your opponents choice is: ")
        print(scissors)
    print("You win!")

if users_choice < computer_options:
    if computer_options in rock1:
        print("Your opponents choice is: ")
        print(rock)
    elif computer_options in paper1:
        print("Your opponents choice is: ")
        print(paper)
    elif computer_options in scissors2:
        print("Your opponents choice is: ")
        print(scissors)
    print("You lose!")

if users_choice == computer_options:
    if computer_options in rock1:
        print("Your opponents choice is: ")
        print(rock)
    elif computer_options in paper1:
        print("Your opponents choice is: ")
        print(paper)
    else:
        print("Your opponents choice is: ")
        print(scissors)
    print("You tie!")



