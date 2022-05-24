from random import randint
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def game_round():
    x = randint(1, 100)
    y = randint(1, 100)
    question = f"{x} {y}"
    answer = str(gcd(x, y))
    return question, answer
