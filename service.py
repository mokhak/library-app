from models import BookItem

class BookService:
    def __init__(self):
        self.model = BookItem()

    def create_book(self, params):
        return self.model.create(params)

    def update_book(self, book_id, params):
        return self.model.update(book_id, params)

    def delete_book(self, book_id):
        return self.model.delete(book_id)

    def list_books(self):
        return self.model.list_items()

    def get_book_by_id(self, book_id):
        return self.model.get_by_id(book_id)