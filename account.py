from random import randint
from repository import insert_card
from repository import delete_card_by_number
from credit_card import generate_credit_card_number


def create_account(account):
    credit_card_number = generate_credit_card_number()
    pin = randint(1000, 9999)

    insert_card({'number': credit_card_number, 'pin': pin})

    print('Your card has been created')
    print('Your card number:')
    print(credit_card_number)
    print('Your card PIN:')
    print(pin)


def close_account(account):
    credit_card = account['number']
    delete_card_by_number(credit_card)
    print('The account has been closed!')
    return None
