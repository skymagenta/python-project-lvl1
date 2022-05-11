#!/usr/bin/env python

from random import randint, choice
import prompt


def calc():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('What is the result of the expression?')

    i = 0

    while i < 3:
        x = randint(1, 100)
        y = randint(1, 100)
        sign = choice(['+', '-', '*'])
        print('Question:', f'{x} {sign} {y}')
        answer = prompt.string('Your answer: ')
        if sign == '+':
            correct_answer = str(x + y)
        elif sign == '-':
            correct_answer = str(x - y)
        else:
            correct_answer = str(x * y)

        if answer != correct_answer:
            print(answer, 'is wrong answer ;(. Correct answer was',
                  correct_answer, '.')
            print(f"Let's try again, {name}!")
            break
        else:
            print('Correct!')
        i += 1

    if i == 3:
        print(f'Congratulations, {name}!')
