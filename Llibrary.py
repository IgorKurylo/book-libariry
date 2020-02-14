from LibraryService import LibraryService
from Parser import Parser
from CommandEnum import Command
import typing
from Subscription import Subscription


def print_command(command):
    print("[" % command % "]")


if __name__ == '__main__':
    subscriptions = []
    subscriptionsBooksMapping = typing.Dict[str, Subscription]  # mapping for books and subscription
    bookSubscriptionMapping = typing.Dict[int, typing.List]  # mapping for subscription and list of books
    print("Welcome to Library")
    while True:
        print("Write your query, for finish press 'exit' ")
        input_str = input()
        data, cmd = Parser.parse_input(input_str)
        if cmd == Command.INPUT:
            info, cmd = Parser.parse_data(data)
            if cmd == Command.TAKE_BOOK:
                print_command(Command.TAKE_BOOK)
                index = LibraryService.find_subscription(info["id"], subscriptions)
                if index != -1:
                    try:
                        subscriptions[index].add_book(info["book"])
                        subscriptionsBooksMapping[info["book"]] = subscriptions[index]
                        if info["id"] not in bookSubscriptionMapping:
                            bookSubscriptionMapping[info["id"]] = subscriptions[index].books
                        else:
                            bookSubscriptionMapping[info["id"]].append(info["book"])
                    except OverflowError:
                        print("Overflow Error")
                else:
                    print("Subscription {0} is not exists".format(info["id"]))
            if cmd == Command.RETURN_BOOK:
                print_command(Command.RETURN_BOOK)
                index = LibraryService.find_subscription(info["id"], subscriptions)
                if index != -1:
                    subscriptions[index].remove_book(info["book"])
                    if info["book"] in subscriptionsBooksMapping and info["id"] in bookSubscriptionMapping:
                        del subscriptionsBooksMapping[info["book"]]
                        bookSubscriptionMapping[info["id"]].remove(info["book"])
                    else:
                        print("Book {0} is not exists".format(info["book"]))
                else:
                    print("Subscription {0} is not exists".format(info["id"]))
            if cmd == Command.ADD_SUBSCRIPTION:
                print_command(Command.ADD_SUBSCRIPTION)
                # print(info)
                subscriptions.append(info)
                print("Subscription  {0} added ".format(info.id))
            if cmd == Command.REMOVE_SUBSCRIPTION:
                print_command(Command.REMOVE_SUBSCRIPTION)
                # print(info)
            index = LibraryService.find_subscription(info.id, subscriptions)
            if index == -1:
                subscriptions.pop(index)
                print("Subscription {0} found with ".format(info.id))
                print("Subscription {0} deleted ".format(subscriptions.pop(index).id))

        if cmd == Command.QUERY:
            query_data, cmd = Parser.parse_query(data[0], data[1])
            if cmd == Command.SELECT_BOOKS:
                print(LibraryService.select_books(query_data, bookSubscriptionMapping))
            if cmd == Command.SELECT_SUBSCRIPTION:
                print(LibraryService.select_subscription(query_data, subscriptionsBooksMapping))
            if cmd == Command.ALL_SUBSCRIPTION:
                print(LibraryService.select_max_books(bookSubscriptionMapping, subscriptionsBooksMapping))
        if cmd == Command.EXIT:
            break
