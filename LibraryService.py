class LibraryService:
    def __init__(self):
        pass

    @staticmethod
    def find_subscription(subscription_id, subscriptions):
        for index, sub in enumerate(subscriptions):
            if sub.id == subscription_id:
                return index
        return -1

    # def take_book(self, data, mapper, tree):
    #     print(data)
    #
    # def return_book(data, mapper, tree):
    #     print(data)
    #
    # def add_subscription(self, data, mapper, tree):
    #     print(data)
    #
    # def remove_subscription(self, data, mapper, tree):
    #     print(data)
    #
    @staticmethod
    def select_books(data, mapper_books):
        print(data)

    @staticmethod
    def select_subscription(data, mapper_subscription):
        print(data)

    @staticmethod
    def select_max_books(mapper_books, mapper_subscription):
        subscription_list = []
