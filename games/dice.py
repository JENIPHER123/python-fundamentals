# dice game using functions
import random


def win():
    winner = random.randint(3,9)
    return winner

guess = int(input('>> '))

if guess == win():
    print('you win!!')
else:
    print('you loose!!')

