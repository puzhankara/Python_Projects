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
import random
images = [rock, paper, scissors]
user_choice = int(input("Choose 0 for Rock, 1 for Paper and 2 for Scissors: "))
print (images[user_choice])
ai_choice = random.randint(0,2)
print(f"The computer chose {images[ai_choice]}")
if user_choice == 0 and ai_choice == 1:
  print ("You lost")
elif user_choice == 0 and ai_choice == 2:
  print ("You won")
elif user_choice == 1 and ai_choice == 0:
  print ("You won")
elif user_choice == 2 and ai_choice == 1:
  print ("You won")
elif user_choice == 1 and ai_choice == 2:
  print ("You lost")
elif user_choice == 2 and ai_choice == 0:
  print ("You lost")
elif user_choice == ai_choice:
  print ("Its a draw")