import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    number = random.randint(2, 30)
    correct_answer = is_prime(number)
    math_message = ("{}".format(number))

    return 'yes' if correct_answer else 'no', math_message


def is_prime(num):
    prime_number = [2, 3, 5, 7]
    check_num = [num > 1,
                 num % 2 != 0,
                 num % 3 != 0,
                 num % 5 != 0,
                 num % 7 != 0]
    return all(check_num) or num in prime_number
