#!/usr/bin/env python

from random import randint

GAME_CONDITIONS = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_number_prime(num):
    """
    Checks, is number prime.
    """
    is_prime = True
    if num <= 1:
        is_prime = False
    elif num == 2:
        is_prime = True
    else:
        for divider in range(2, num):
            if num % divider == 0:
                is_prime = False
                break

    return is_prime


def bool_to_word(bool):
    if bool == True:
        return 'yes'
    else:
        return 'no'


def game():
    num = randint(1, 100)
    question = num
    answer = bool_to_word(is_number_prime(num))
    return question, answer
