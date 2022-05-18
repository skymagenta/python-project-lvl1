#!/usr/bin/env python

from random import randint, choice


def calc(game_count = 3):
    questions = []
    correct_answers = []
    for i in range(game_count):
        x = randint(1, 100)
        y = randint(1, 100)
        sign = choice(['+', '-', '*'])
        questions.append(f"{x} {sign} {y}")

        if sign == '+':
            correct_answers.append(str(x + y))
        elif sign == '-':
            correct_answers.append(str(x - y))
        else:
            correct_answers.append(str(x * y))
    
    print('What is the result of the expression?')
    return questions, correct_answers