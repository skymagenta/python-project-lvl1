#!/usr/bin/env python

from random import randint
import prompt


def is_number_prime(num):
    """
    Проверяет, является ли число простым.
    """
    is_prime = 'yes'
    if num == 1:
        is_prime = 'no'
        return is_prime
    elif num == 2:
        return is_prime
    else:
        for divider in range(2, num):
            if num % divider == 0:
                is_prime = 'no'
                break

    return is_prime


def prime():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello', name, '!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    i = 0

    while i < 3:
        num = randint(1, 100)
        print('Question: ', num)
        answer = prompt.string('Your answer: ')
        correct_answer = is_number_prime(num)
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
