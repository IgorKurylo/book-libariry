from CommandEnum import Command
from Customer import Subscription


class Parser:
    long_space = "  "
    space = " "
    exit = "exit"
    add = "+"
    delete = "-"
    query = "?"
    all = "!"

    def __init__(self):
        pass

    @staticmethod
    def parse_input(input_str):
        if input_str.lower() == Parser.exit:
            return None, Command.EXIT
        try:
            if Parser.space in input_str or Parser.long_space in input_str:
                input_data = input_str.replace(Parser.long_space, Parser.space).split()
                if len(input_data) == 4 or len(input_data) == 3:
                    return input_data, Command.INPUT
            if Parser.space in input_str and Parser.query in input_str:
                query_data = input_str.split(Parser.space)
                return query_data, Command.QUERY

        except ValueError:
            print("Input is incorrect")

    @staticmethod
    def parse_data(data):
        if data[len(data) - 1] == Parser.add:
            return dict({'last_name': data[0], 'id': data[1], 'book': data[2]}), Command.TAKE_BOOK
        if data[len(data) - 1] == Parser.delete:
            return dict({'last_name': data[0], 'id': data[1], 'book': data[2]}), Command.RETURN_BOOK
        if data[0] == Parser.add:
            return Subscription(data[2], data[1]), Command.ADD_SUBSCRIPTION
        if data[0] == Parser.delete:
            return Subscription(data[2], data[1]), Command.REMOVE_SUBSCRIPTION

    @staticmethod
    def parse_query(query, data):
        if query == Parser.query:
            if data.isdigit():
                return data, Command.SELECT_BOOKS
            elif Parser.all is not data:
                return data, Command.SELECT_SUBSCRIPTION
            else:
                return None, Command.MAX_BOOKS_HOLDERS
