import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(2, 30)
    correct_answer = is_prime(number)
    math_message = ("{}".format(number))

    return 'yes' if correct_answer else 'no', math_message


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
