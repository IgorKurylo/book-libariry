import typing


class LibraryService:
    def __init__(self):
        pass

    @staticmethod
    def find_customer(subscription_id, subscriptions):
        for index, sub in enumerate(subscriptions):
            if sub.id == subscription_id:
                return index
        return -1

    @staticmethod
    def find_customer_book(customer_id, customer_book):
        for book in customer_book:
            if customer_book[book].id == customer_id:
                return book
        return -1

    @staticmethod
    def add_customer(customer, customers: typing.List):
        customers.append(customer)

    @staticmethod
    def remove_customer(index, customers: typing.List):
        customers.pop(index)

    @staticmethod
    def add_book_customer(customers, index, book):
        customers[index].add_book(book)


    @staticmethod
    def select_books(data, books_map):
        books = books_map[data]
        print(",".join(books))

    @staticmethod
    def select_customer(data, customers_map):
        print(customers_map[data].id)

    @staticmethod
    def select_max_books(mapper_books):
        subscription_list = []
        max_book = len(mapper_books[list(mapper_books.keys())[0]])
        for sub in mapper_books:
            print(sub)
