import prompt

ROUNDS_COUNTER = 3


def launch(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print(game.RULE)

    for i in range(ROUNDS_COUNTER):
        question, answer = game.game_round()
        print('Question:', question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != answer:
            print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{answer}'.")
            print(f"Let's try again, {name}!")
            break
        print('Correct!')
    else:
        print(f"Congratulations, {name}!")
