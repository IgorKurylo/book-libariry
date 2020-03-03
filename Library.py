import signal
import sys

import colors

from HashMapper import HashMapper
from LibraryService import LibraryService
from Parser import Parser
from CommandEnum import Command
import typing
from Customer import Customer


def print_input(input, add_new_line):
    print(colors.fgcolor.INFO + "{0}".format(input), end=add_new_line)


def print_data(data):
    print(" ".join(data))


if __name__ == '__main__':
    customers: typing.List[Customer] = list()
    hash_mapper = HashMapper()
    print(colors.fgcolor.WARNING, "Welcome to Library v1.0", "")

    while True:
        print(colors.fgcolor.WARNING, "Write a query")
        print(colors.fgcolor.FAIL, "Type exit for finish")
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
                        if hash_mapper.book_is_available(info["book"]):
                            LibraryService.add_book_customer(customers, index, info["book"])
                            hash_mapper.add_book(customers[index], info["book"])
                            print("Book {0} added to {1} customer".format(info["book"], info["id"]))
                        else:
                            print(colors.fgcolor.FAIL + "Book {0} is not available".format(info["book"]))
                    except OverflowError as ex:
                        print(colors.fgcolor.FAIL, ex, "\n")
                else:
                    print(colors.fgcolor.FAIL + "Customer {0} is not exists".format(info["id"]))
            if cmd == Command.RETURN_BOOK:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_customer(info["id"], customers)
                if index != -1:
                    LibraryService.remove_book_customer(customers, index, info["book"])
                    if hash_mapper.return_book(info["id"], info["book"]):
                        print("Book {0} returned".format(info["book"]))
                    else:
                        print("Book {0} is not exists".format(info["book"]))
                else:
                    print("Customer {0} is not exists".format(info["id"]))
            if cmd == Command.ADD_CUSTOMER:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                LibraryService.add_customer(info, customers)
                print("Customer  {0} added ".format(info.customer_id))
            if cmd == Command.REMOVE_CUSTOMER:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                index = LibraryService.find_customer(info.customer_id, customers)
                if index != -1:
                    LibraryService.remove_customer(index, customers)
                    hash_mapper.remove_customer(info.customer_id)
                    print("Customer {0} deleted ".format(info.customer_id))
                else:
                    print("Customer {0} is not exists".format(info.customer_id))
        if cmd == Command.QUERY:
            query_data, cmd = Parser.parse_query(data[0], data[1])
            if cmd == Command.SELECT_BOOKS:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                books = LibraryService.select_books(query_data, hash_mapper.customer_books)
                if books is not None:
                    print_input("Customer {0} hold the next books".format(data[1]), " ")
                    print(",".join(books))
                else:
                    print("Customer {0} is not exists".format(data[1]))
            if cmd == Command.SELECT_CUSTOMER:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                customer = LibraryService.select_customer(query_data, hash_mapper.book_customer)
                if customer is not None:
                    print_input("The book {0} hold Customer".format(data[1]), " ")
                    print_input(customer, "\n")
                else:
                    print("Not any customer hold the book {0}".format(data[1]))
            if cmd == Command.MAX_BOOKS_HOLDERS:
                print_input(cmd.name, " ")
                print_input(input_str, "\n")
                max_books_customer = LibraryService.select_max_books(hash_mapper.customer_books)
                if len(max_books_customer) > 0:
                    print_input("List of customer who hold max count of books", "\n")
                    print_data(max_books_customer)
                else:
                    print_input("No customers holds  max of books", "\n")
        if cmd == Command.EXIT:
            sys.exit(0)
