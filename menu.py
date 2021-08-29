VISITOR_MENU = [
    {'key': 1, 'name': 'Create an account', 'handler_id': 1},
    {'key': 2, 'name': 'Log into account', 'handler_id': 2},
    {'key': 0, 'name': 'Exit', 'handler_id': 0}
]

USER_MENU = [
    {'key': 1, 'name': 'Balance', 'handler_id': 3},
    {'key': 2, 'name': 'Add income', 'handler_id': 5},
    {'key': 3, 'name': 'Do transfer', 'handler_id': 6},
    {'key': 4, 'name': 'Close account', 'handler_id': 7},
    {'key': 5, 'name': 'Log out', 'handler_id': 4},
    {'key': 0, 'name': 'Exit', 'handler_id': 0},
]


def print_menu(account=None):
    menu_options = map(lambda x: f'{x["key"]}. {x["name"]}', get_menu(account))
    menu_string = '\n'.join(menu_options)
    print(menu_string)


def get_menu(is_logged_in):
    return USER_MENU if is_logged_in else VISITOR_MENU
