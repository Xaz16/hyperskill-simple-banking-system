from repository import update_balance
from repository import get_balance
from repository import get_card_by_number

from credit_card import validate


def print_balance(account):
    print(f'Balance: {account["balance"]}')


def add_income(account):
    income = int(input("Enter income: "))

    if income < 0:
        print('You can not enter negative income')
        return add_income(account)

    current_balance = get_balance(account['number'])
    new_balance = current_balance + income
    update_balance(account['number'], new_balance)

    print('Income was added!')


def transfer(account):
    print('Transfer')
    card_number = input('Enter card number: ')

    is_valid = validate(card_number)

    if not is_valid:
        print('Probably you made a mistake in the card number. Please try again!')
        return

    is_exists = get_card_by_number(card_number) != {}

    if not is_exists:
        print('Such a card does not exist.')
        return

    amount = int(input('Enter how much money you want to transfer:'))

    if amount > account['balance']:
        print('Not enough money!')
        return

    update_balance(account['number'], account['balance'] - amount)
    update_balance(card_number, amount)

    print('Success!')
