from random import randint, choice

RULE = 'What is the result of the expression?'


def game_round():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    random_operator = choice(['+', '-', '*'])
    question = f"{random_number_1} {random_operator} {random_number_2}"
    if random_operator == '+':
        answer = random_number_1 + random_number_2
    elif random_operator == '-':
        answer = random_number_1 - random_number_2
    elif random_operator == '*':
        answer = random_number_1 * random_number_2
    return question, str(answer)
