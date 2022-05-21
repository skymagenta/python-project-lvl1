#!/usr/bin/env python

from random import randint


def get_greatest_common_divisor(x, y):
    """
    Finds the greatest common divisor of two positive integers.
    """
    for num in range(min(x, y), 0, -1):
        if (x % num == 0) and (y % num == 0):
            gcd = num
            break
    return gcd


def gcd():
    game_conditions = 'Find the greatest common divisor of given numbers.'
    questions_and_answers = []
    x = randint(1, 100)
    y = randint(1, 100)
    questions_and_answers.append(f"{x} {y}")
    questions_and_answers.append(str(get_greatest_common_divisor(x, y)))
    return questions_and_answers, game_conditions
