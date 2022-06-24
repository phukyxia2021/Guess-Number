from asyncio.windows_events import NULL
import random

topOfRange = NULL
while True:
    topOfRange= int(input("Enter a top of range: "))
    if topOfRange <= 0:
        print("Please enter a number larger than 0!")
    else: 
        break

randomNumber = random.randint(0, topOfRange)
guesses = 0
while True:
    guesses += 1
    userGuess = input("Your guess number: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("Please enter a number!")
        continue
    if userGuess == randomNumber:
        print("You got it!")
        break
    elif userGuess > randomNumber:
        print("You was above the number!")
    else:
        print("You was below the number!")
print("You got it in", guesses, "guesses.")