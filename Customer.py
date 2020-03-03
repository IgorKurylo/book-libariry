class Customer:
    MAX_BOOKS = 2

    def __init__(self, customer_id, last_name):
        self.customer_id = customer_id
        self.last_name = last_name
        self.books = []

    def add_book(self, book_id):
        if len(self.books) <= Customer.MAX_BOOKS:
            self.books.append(book_id)
        else:
            raise OverflowError("Error occurred,customer can't take more then {0} books".format(Customer.MAX_BOOKS))

    def remove_book(self, book_id):
        for bid in self.books:
            if bid == book_id:
                self.books.remove(bid)
