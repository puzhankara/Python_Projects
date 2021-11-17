import random
name = input("What is your name: \n")
print(f"Hello {name}, welcome to the number guessing game")
ai_number = random.randint(1, 20)
#guessing the number 6 times
for num in range(1, 7):
    print("Guess a number between 1 and 20")
    f_guess = int(input())
    if f_guess > ai_number:
        print("It's bigger")
    elif f_guess < ai_number:
        print("It's smaller")
    else:
        break
if f_guess == ai_number:
    print(f"You nailed it {name}!!")
else:
    print(f"The number I had in mind was {ai_number}")
