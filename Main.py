import random

secretNum = random.randint(1, 20)
print('I am thinking about a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('Take a guess ^^')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('your guess is bigger than the number')
