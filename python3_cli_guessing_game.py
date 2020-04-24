# This is a guessing game where we use the import.random module to generate a random number between 1 and 30.
# The goal is to guess the correct number within a set amount of tries and with feedback that informs you wether your guess is to high or to low.

# To generate a random number, we have to import the random module.
import random

print('Hello, can you please tell me your name?')
playerName = input()

# We generate a random number with this line of code.
secretNumber = random.randint(1, 30)

print('Okay ' + playerName + ' let`s get started!')
print('I am thinking of a number between 1 and 30, can you guess what it is?')
print('You have 5 tries!')

print(secretNumber)

# We can count the number of guessings the player have done by using the "for in range function".
for guessAttempts in range(1, 6):
    print('Type the number followed by pressing the "enter" key!')
    guessNumber = int(input())
    if guessNumber != secretNumber and guessNumber > secretNumber + 1:
        print('Your guess is to high!')
        print('You have ' + str(int(5) - int(guessAttempts)) + ' remaining attempts!')
        print('Try again!')
    elif guessNumber != secretNumber and guessNumber < secretNumber + 1:
        print('Your guess is to low!')
        print('You have ' + str(int(5) - int(guessAttempts)) + ' remaining attempts!')
        print('Try again!')
    elif guessNumber == secretNumber + 1 or guessNumber == secretNumber -1 and guessNumber != secretNumber:
        print('You are so close!')
        print('You have ' + str(int(5) - int(guessAttempts)) + ' remaining attempts!')
        print('Try again!')
    else:
        break

if guessNumber == secretNumber:
    print('Congratulations ,' + playerName +'! You guessed the correct answer in ' + str(guessAttempts) + ' attempts!')
else:
    print('Sorry, you did not guess the correct number. The number I was thinking of was ' + str(secretNumber) + '!')

