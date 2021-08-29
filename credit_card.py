from random import randint


def luhn(number, position):
    new_value = number
    if position % 2 != 0 or position == 1:
        new_value *= 2
    if new_value > 9:
        new_value -= 9
    return new_value


def validate(number):
    calculated_last_number = provide_last_number(number)

    return int(number[-1]) == calculated_last_number


def provide_last_number(full_number):
    number_list = [int(x) for x in full_number]
    number_list.pop()
    luhn_sum = []

    for i in range(len(number_list)):
        luhn_sum.append(luhn(number_list[i], i + 1))

    result = 0
    for num in luhn_sum:
        result += num

    last_number = 10 - (result % 10)

    return 0 if last_number == 10 else last_number


def generate_credit_card_number():
    number = randint(1000_0000_00, 9999_9999_99)
    cc_number = f'400000{number}'
    number_list = [int(x) for x in cc_number]
    number_list.pop()
    last_number = provide_last_number(cc_number)
    number_list.append(last_number)

    return ''.join([str(x) for x in number_list])
