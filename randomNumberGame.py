#! python3

import random

def get(question, condition, errorText):
    while True:
        print(question)
        getInput = input()
        try:
            if condition(getInput):
                return getInput
        except ValueError:
            print(errorText)
        else:
                print(errorText)

name = get("Hello, What is your name?",lambda a : a != "","Please type your name!")

secretNumber = random.randint(1,20)
print("Well,", name, ", I'm thinking of a number between 1 and 20.")
print("You have 4 tries to guees it... Good Luck!")

print("DEBUG: The secret number is", secretNumber)

for guessesTaken in range(1,5):
    while True:
        try:
            guess = int(input("Take a guess: "))
            if 0 < guess <= 20:
                break
            else:
                print("Enter a number betewwn 1 and 20 please.")
        except ValueError:
            print("Enter a number betewwn 1 and 20 please.")
    if guess > secretNumber:
        print("Your guess is too high!")
    elif guess < secretNumber:
        print("Your guess is too low!")
    else:
        break
if guess == secretNumber:
    print("Good job",name,", you guessed my number in",guessesTaken,"tries.")
else:
    print("Nope, the number i was guessing was",secretNumber)