#!/usr/bin/env python

from random import randint
from math import gcd

GAME_CONDITIONS = 'Find the greatest common divisor of given numbers.'


def game():
    x = randint(1, 100)
    y = randint(1, 100)
    question = f"{x} {y}"
    answer = str(gcd(x, y))
    return question, answer
