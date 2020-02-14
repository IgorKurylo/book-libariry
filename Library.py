from LibraryService import LibraryService
from Parser import Parser
from CommandEnum import Command
import typing
from Subscription import Subscription


def print_input(input, addnewLine):
    print("[ {0} ]".format(input), end=addnewLine)


if __name__ == '__main__':
    subscriptions = []
    subscriptionsBooksMapping: typing.Dict[str, typing.Any] = dict()  # mapping for books and subscription
    bookSubscriptionMapping: typing.Dict[int, typing.List] = dict()  # mapping for subscription and list of books
    print_input("Welcome to Library", "\n")
    while True:
        print_input("Write your query, for finish press 'exit' ", "\n")
        input_str = input()
        data, cmd = Parser.parse_input(input_str)
        if cmd == Command.INPUT:
            info, cmd = Parser.parse_data(data)
            if cmd == Command.TAKE_BOOK:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_subscription(info["id"], subscriptions)
                if index != -1:
                    try:
                        subscriptions[index].add_book(info["book"])
                        subscriptionsBooksMapping[info["book"]] = subscriptions[index]
                        if info["id"] not in bookSubscriptionMapping:
                            bookSubscriptionMapping[info["id"]] = subscriptions[index].books[:]
                        else:
                            bookSubscriptionMapping[info["id"]].append(info["book"])
                        print("Book {0} add to {1} subscription".format(info["book"], info["id"]))
                    except OverflowError:
                        print_input("Overflow Error Subscription Have already 10 books ", "\n")
                else:
                    print("Subscription {0} is not exists".format(info["id"]))
            if cmd == Command.RETURN_BOOK:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_subscription(info["id"], subscriptions)
                if index != -1:
                    subscriptions[index].remove_book(info["book"])
                    if info["book"] in subscriptionsBooksMapping and info["id"] in bookSubscriptionMapping:
                        del subscriptionsBooksMapping[info["book"]]
                        bookSubscriptionMapping[info["id"]].remove(info["book"])
                        print("Book {0} returned".format(info["book"]))
                    else:
                        print("Book {0} is not exists".format(info["book"]))
                else:
                    print("Subscription {0} is not exists".format(info["id"]))
            if cmd == Command.ADD_SUBSCRIPTION:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                subscriptions.append(info)
                print("Subscription  {0} added ".format(info.id))
            if cmd == Command.REMOVE_SUBSCRIPTION:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_subscription(info.id, subscriptions)
                if index != -1:
                    subscriptions.pop(index)
                    if info.id in bookSubscriptionMapping:
                        del bookSubscriptionMapping[info.id]
                        bookId = LibraryService.find_book_subscription(info.id, subscriptionsBooksMapping)
                        if bookId != -1:
                            del subscriptionsBooksMapping[bookId]

                    print("Subscription {0} deleted ".format(info.id))
                else:
                    print("Subscription {0} is not exists".format(info.id))
        if cmd == Command.QUERY:
            query_data, cmd = Parser.parse_query(data[0], data[1])
            if cmd == Command.SELECT_BOOKS:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.select_books(query_data, bookSubscriptionMapping)
            if cmd == Command.SELECT_SUBSCRIPTION:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.select_subscription(query_data, subscriptionsBooksMapping)
            if cmd == Command.ALL_SUBSCRIPTION:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.select_max_books(bookSubscriptionMapping, subscriptionsBooksMapping)
        if cmd == Command.EXIT:
            break
