#!/usr/bin/env python

from random import randint


def is_number_prime(num):
    """
    Checks, is number prime.
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


def prime():
    game_conditions = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'
    questions_and_answers = []
    num = randint(1, 100)
    questions_and_answers.append(num)
    questions_and_answers.append(is_number_prime(num))
    return questions_and_answers, game_conditions
