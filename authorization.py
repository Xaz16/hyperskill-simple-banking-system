from repository import get_card_by_number


def ask_card_number():
    card_number = input('Enter your card number: ')
    return card_number


def ask_pin(found_pin):
    pin = input('Enter your PIN: ')

    return found_pin == pin


def login(account):
    card_number = ask_card_number()
    account = get_card_by_number(card_number)
    is_pin_correct = ask_pin(account['pin'] if 'pin' in account.keys() else None)

    if not is_pin_correct:
        print('Wrong card number or PIN!')
    else:
        print('You have successfully logged in!')

    return account if is_pin_correct else None


def logout(account):
    return None
