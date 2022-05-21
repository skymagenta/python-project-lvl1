#!/usr/bin/env python

from random import randint, choice


def calc():
    game_conditions = 'What is the result of the expression?'
    questions_and_answers = []
    x = randint(1, 100)
    y = randint(1, 100)
    sign = choice(['+', '-', '*'])
    questions_and_answers.append(f"{x} {sign} {y}")
    if sign == '+':
        questions_and_answers.append(str(x + y))
    elif sign == '-':
        questions_and_answers.append(str(x - y))
    else:
        questions_and_answers.append(str(x * y))
    return questions_and_answers, game_conditions
