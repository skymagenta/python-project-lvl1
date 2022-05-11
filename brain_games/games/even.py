#!/usr/bin/env python

from random import randint
import prompt


def even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    i = 0

    while i < 3:
        x = randint(1, 100)
        print('Question: ', str(x))
        answer = prompt.string('Your answer: ')
        if x % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

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
