#!/usr/bin/env python3


import prompt


COUNT = 3


def run_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? \n')
    print(f'Hello, {name}')
    print(game.DESCRIPTION)

    for i in range(COUNT):
        correct_answer, question_message = game.get_question_and_answer()
        print(f'Question: {question_message}')
        user_answer = prompt.string('Your answer: ')

        if correct_answer != user_answer:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'"
                f"Let's try again, {name}!"
            )
            return

        print('Correct!')

    print(f'Congratulations, {name}!')    
