class Customer:
    def __init__(self, customer_id, last_name):
        self.customer_id = customer_id
        self.last_name = last_name
        self.books = []

    def add_book(self, book_id):
        if len(self.books) <= 10:
            self.books.append(book_id)
        else:
            raise OverflowError("Customer already have 10 books")

    def remove_book(self, book_id):
        for bid in self.books:
            if bid == book_id:
                self.books.remove(bid)

