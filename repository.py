from db import read
from db import write
from db import disconnect
from db import connect


def close():
    disconnect()


def open():
    connect()
    table_data = is_table_exists()
    if not table_data:
        create_table()


def is_table_exists(table_name='card'):
    return len(read(f"""
    SELECT name FROM sqlite_master WHERE type='table'
  AND name='{table_name}'; """))


def create_table():
    query = """
        CREATE TABLE card (
            id INTEGER,
            number TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 0
        );
    """
    write(query)


def get_balance(number):
    query = f"""
        SELECT balance FROM card WHERE number = {number};
    """
    return read(query)[0]['balance']


def update_balance(number, amount):
    query = f"""
        UPDATE card SET balance = {amount} WHERE number = '{number}';
    """
    write(query)


def insert_card(card):
    query = f"""
        INSERT INTO card (number, pin) VALUES ('{card['number']}', '{card['pin']}');
    """
    write(query)


def get_cards():
    query = """
        SELECT * FROM card;
    """
    return read(query)


def get_card_by_number(number):
    query = f"""
        SELECT number, pin, balance FROM card WHERE number = '{number}';
    """
    result = read(query)
    return result[0] if len(result) else {}


def delete_card_by_number(card_number):
    query = f"""
        DELETE FROM card WHERE number = {card_number};
    """
    write(query)
