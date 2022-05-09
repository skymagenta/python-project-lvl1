#!/usr/bin/env python

from random import randint
import prompt


def get_greatest_common_divisor(x, y):
    for num in range(min(x, y), 0, -1):
        if (x % num == 0) and (y % num == 0):
            gcd = num
            break
    return gcd


def gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('Find the greatest common divisor of given numbers.')

    i = 0

    while i < 3:
        x = randint(1, 100)
        y = randint(1, 100)
        print('Question: ', f'{x} {y}')
        answer = prompt.string('Your answer: ')
        correct_answer = str(get_greatest_common_divisor(x, y))
        if answer != correct_answer:
            print(answer, 'is wrong answer ;(. Correct answer was',
                  correct_answer, '.')
            print("Let's try again", name, "!")
            break
        else:
            print('Correct!')
        i += 1

    if i == 3:
        print('Congratulations,', name)
