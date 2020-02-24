from HashMapper import HashMapper
from LibraryService import LibraryService
from Parser import Parser
from CommandEnum import Command
import typing
from Customer import Customer


def print_input(input, addnewLine):
    print(" {0} ".format(input), end=addnewLine)


def print_data(data):
    print(" ".join(data))


if __name__ == '__main__':
    customers: typing.List[Customer] = list()
    # subscriptionsBooksMapping: typing.Dict[str, typing.Any] = dict()  # mapping for books and subscription
    # bookSubscriptionMapping: typing.Dict[int, typing.List] = dict()  # mapping for subscription and list of books
    hash_mapper = HashMapper()
    print_input("[Welcome to Library]", "\n")
    while True:
        print_input("[Write your query, for finish press 'exit' ]", "\n")
        input_str = input()
        data, cmd = Parser.parse_input(input_str)
        if cmd == Command.INPUT:
            info, cmd = Parser.parse_data(data)
            if cmd == Command.TAKE_BOOK:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_customer(info["id"], customers)
                if index != -1:
                    try:
                        # TODO: check if book is availabale
                        LibraryService.add_book_customer(customers, index, info["book"])
                        subscriptionsBooksMapping[info["book"]] = customers[index]
                        if info["id"] not in bookSubscriptionMapping:
                            bookSubscriptionMapping[info["id"]] = customers[index].books[:]
                        else:
                            bookSubscriptionMapping[info["id"]].append(info["book"])
                        print("Book {0} add to {1} subscription".format(info["book"], info["id"]))
                    except OverflowError as ex:
                        print_input(ex, "\n")
                else:
                    print("Customer {0} is not exists".format(info["id"]))
            if cmd == Command.RETURN_BOOK:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_customer(info["id"], customers)
                if index != -1:
                    customers[index].remove_book(info["book"])
                    if info["book"] in subscriptionsBooksMapping and info["id"] in bookSubscriptionMapping:
                        del subscriptionsBooksMapping[info["book"]]
                        bookSubscriptionMapping[info["id"]].remove(info["book"])
                        print("Book {0} returned".format(info["book"]))
                    else:
                        print("Book {0} is not exists".format(info["book"]))
                else:
                    print("Customer {0} is not exists".format(info["id"]))
            if cmd == Command.ADD_CUSTOMER:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.add_customer(info, customers)
                print("Customer  {0} added ".format(info.id))
            if cmd == Command.REMOVE_CUSTOMER:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_customer(info.id, customers)
                if index != -1:
                    LibraryService.remove_customer(index, customers)
                    hash_mapper.remove_customer(info.id)
                    print("Customer {0} deleted ".format(info.id))
                else:
                    print("Customer {0} is not exists".format(info.id))
        if cmd == Command.QUERY:
            query_data, cmd = Parser.parse_query(data[0], data[1])
            if cmd == Command.SELECT_BOOKS:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                print_input("Customer {0} hold the next books".format(data[1]), " ")
                LibraryService.select_books(query_data, bookSubscriptionMapping)
            if cmd == Command.SELECT_SUBSCRIPTION:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                print_input("The book {0} hold  Customer".format(data[1]), " ")
                LibraryService.select_customer(query_data, subscriptionsBooksMapping)
            if cmd == Command.MAX_BOOKS_HOLDERS:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.select_max_books(bookSubscriptionMapping)
        if cmd == Command.EXIT:
            break
