# Write your code here
from repository import get_cards
from repository import open
from handlers import HANDLERS
from repository import get_card_by_number

from menu import print_menu
from menu import get_menu


def init():
    open()


def main(account):
    init()
    print_menu(account)
    incoming_message = input()
    user_choice = int(incoming_message) if len(incoming_message) else ''

    menu_points = list(filter(lambda x: x['key'] == user_choice, get_menu(account)))

    if len(menu_points) == 0:
        print('Unknown command')
        return main(account)
    else:
        handler_id = menu_points[0]['handler_id']
        handler = HANDLERS[handler_id]
        updated_account = get_card_by_number(account['number']) if account else account
        handler_result = handler(updated_account)
        if handler_id == 2 or handler_id == 4 or handler_id == 7:
            return main(handler_result)
        elif handler_id != 0:
            return main(updated_account)


main(False)
