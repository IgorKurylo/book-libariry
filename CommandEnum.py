from enum import Enum


class Command(Enum):
    TAKE_BOOK = 1
    RETURN_BOOK = 2
    ADD_CUSTOMER = 3
    REMOVE_CUSTOMER = 4
    BOOKS_QUERY = 5
    SUBSCRIPTION_QUERY = 6
    MAX_BOOKS_HOLDERS = 7
    QUERY = 8
    INPUT = 9,
    SELECT_BOOKS = 11,
    SELECT_CUSTOMER = 12,
    EXIT = 10
