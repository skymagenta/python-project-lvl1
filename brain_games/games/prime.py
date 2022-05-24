from random import randint

RULE = 'Answer "yes" if given number is prime. \
Otherwise answer "no".'


def is_number_prime(num):
    """
    Checks, is number prime.
    """
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for divider in range(2, num):
            if num % divider == 0:
                return False

    return True


def game_round():
    num = randint(1, 100)
    question = num
    answer = is_number_prime(num)
    if answer is True:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
