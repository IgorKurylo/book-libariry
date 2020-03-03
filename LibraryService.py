import typing

import Customer


# class which implements all library services
class LibraryService:
    def __init__(self):
        pass

    # find customer from customer list
    @staticmethod
    def find_customer(customer_id, customers):
        for index, sub in enumerate(customers):
            if sub.customer_id == customer_id:
                return index
        return -1

    # find book id by customer id
    @staticmethod
    def find_customer_book(customer_id, customer_book):
        for book in customer_book:
            if customer_book[book].customer_id == customer_id:
                return book
        return -1

    # add customer
    @staticmethod
    def add_customer(customer, customers: typing.List):
        customers.append(customer)

    # remove customer
    @staticmethod
    def remove_customer(index, customers: typing.List):
        customers.pop(index)

    # add book to customer
    @staticmethod
    def add_book_customer(customers, index, book):
        customers[index].add_book(book)

    # remove book from customer
    @staticmethod
    def remove_book_customer(customers, index, book):
        customers[index].remove_book(book)

    # select books by customer id
    @staticmethod
    def select_books(customer_id, books_map):
        if customer_id in books_map:
            return books_map[customer_id]
        return None

    # show customer by book id
    @staticmethod
    def select_customer(book_id, book_customer):
        if book_id in book_customer:
            return book_customer[book_id].customer_id
        return None

    @staticmethod
    def select_max_books(mapper_customer_books: typing.Dict):
        customer_hold_count_books: typing.List = list()
        max_books = len(mapper_customer_books[list(mapper_customer_books.keys())[0]])
        # find the max of books
        for customer in mapper_customer_books:
            if max_books < len(mapper_customer_books[customer]):
                max_books = len(mapper_customer_books[customer])
        # find all customers who hold maximum of books
        for customer in mapper_customer_books:
            if max_books == len(mapper_customer_books[customer]):
                customer_hold_count_books.append(customer)

        return customer_hold_count_books
