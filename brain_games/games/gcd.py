from random import randint
from math import gcd

RULE = 'Find the greatest common divisor of given numbers.'


def game_round():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = f"{random_number_1} {random_number_2}"
    answer = str(gcd(random_number_1, random_number_2))
    return question, answer
