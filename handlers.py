from program import exit_program
from authorization import login
from authorization import logout
from balance import print_balance
from balance import add_income
from balance import transfer
from account import create_account
from account import close_account

HANDLERS = {
    0: exit_program,
    1: create_account,
    2: login,
    3: print_balance,
    4: logout,
    5: add_income,
    6: transfer,
    7: close_account
}
