from random import randint, choice

RULE = 'What is the result of the expression?'


def game_round():
    x = randint(1, 100)
    y = randint(1, 100)
    random_operator = choice(['+', '-', '*'])
    question = f"{x} {random_operator} {y}"
    if random_operator == '+':
        answer = x + y
    elif random_operator == '-':
        answer = x - y
    elif random_operator == '*':
        answer = x * y
    return question, str(answer)
