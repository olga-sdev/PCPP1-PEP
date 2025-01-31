"""
If code gets difficult to understand -> divide it into parts for better management.
"""
import random


def enter_name():
    name = str(input("Enter the name: "))
    return name


def get_random_greeting():
    set_of_greetings = ('Hi', 'Hello', 'Hey', 'Greeting', 'Good morning', 'Good afternoon')
    return random.choice(set_of_greetings)


def greeting(i=10):
    while i > 0:
        i -= 1
        print(f'{get_random_greeting()} {enter_name()}')
        continue


greeting(4)
