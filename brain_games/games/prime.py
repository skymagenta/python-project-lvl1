#!/usr/bin/env python

from random import randint


def is_number_prime(num):
    """
    Проверяет, является ли число простым.
    """
    is_prime = 'yes'
    if num == 1:
        is_prime = 'no'
    elif num == 2:
        is_prime = 'yes'
    else:
        for divider in range(2, num):
            if num % divider == 0:
                is_prime = 'no'
                break

    return is_prime


def prime(game_count = 3):
    questions = []
    correct_answers = []
    for i in range(game_count):
        num = randint(1, 100)
        questions.append(str(num))
        correct_answers.append(is_number_prime(num))

    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    return questions, correct_answers
