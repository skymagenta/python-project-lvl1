#!/usr/bin/env python

from random import randint, choice

GAME_CONDITIONS = 'What is the result of the expression?'

def game():
    x = randint(1, 100)
    y = randint(1, 100)
    random_operator = choice(['+', '-', '*'])
    question = f"{x} {random_operator} {y}"
    if random_operator == '+':
        answer = str(x + y)
    elif random_operator == '-':
        answer = str(x - y)
    elif random_operator == '*':
        answer = str(x * y)
    return question, answer
