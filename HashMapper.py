import typing


# class which hold the data structs of customer and books and functionality of them.
class HashMapper:
    def __init__(self):
        self._customer_books: typing.Dict[int, typing.List] = dict()  # mapping for customer and list of books
        self._book_customer: typing.Dict[str, typing.Any] = dict()  # mapping for book to customer

    @property
    def customer_books(self):
        return self._customer_books

    @property
    def book_customer(self):
        return self._book_customer

    # add book to customer
    def add_book(self, customer, book_id):
        self._book_customer[book_id] = customer
        if customer.customer_id not in self._customer_books:
            self._customer_books[customer.customer_id] = customer.books[:]
        else:
            self._customer_books[customer.customer_id].append(book_id)

    # return book from customer
    def return_book(self, customer_id, book_id):
        if book_id in self._book_customer and customer_id in self._customer_books:
            del self._book_customer[book_id]
            self._customer_books[customer_id].remove(book_id)
            return True
        else:
            return False

    # remove customer from book mapping
    def remove_customer(self, customer_id):
        if customer_id in self._customer_books:
            books = self._customer_books[customer_id]
            index = 0
            for key in self._book_customer.keys():
                if books[index] == key:
                    del self._book_customer[key]
                index = index + 1
            del self._customer_books[customer_id]

    # check if book is available and customer can take the book
    def book_is_available(self, book_id):
        return book_id not in self._book_customer
