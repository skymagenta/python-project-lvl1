from random import randint
from math import sqrt, ceil

RULE = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_prime(num):
    """
    Checks, is number prime.
    """
    if num <= 1:
        return False
    for divider in range(2, ceil(sqrt(num) + 1)):
        if num % divider == 0:
            return False

    return True


def game_round():
    num = randint(1, 100)
    question = num
    answer = 'no'
    if is_prime(num):
        answer = 'yes'
    return question, answer
