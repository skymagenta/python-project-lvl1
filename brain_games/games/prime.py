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
    # elif num == 2:
        # return True
    for divider in range(2, ceil(sqrt(num) + 1)):
        if num % divider == 0:
            return False

    return True


def game_round():
    num = randint(1, 100)
    question = num
    answer = 'no'
    # answer = is_number_prime(num)
    # if is_prime(num) is True:
    if is_prime(num):
        answer = 'yes'
    # else:
        # answer = 'no'
    return question, answer
