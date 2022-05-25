from random import randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    """
    Creates a list of 10 numbers ranging from 1 to 99
    in an arithmetic progression.
    """
    first_element = randint(1, 29)
    step = randint(2, 7)
    progression = []
    progression_size = 10
    for i in range(progression_size):
        progression.append(str(first_element))
        first_element += step

    return progression


def game_round():
    progression = generate_progression()
    random_index = randint(0, len(progression) - 1)
    answer = progression[random_index]
    progression[random_index] = '..'
    question = ' '.join(progression)
    return question, answer
