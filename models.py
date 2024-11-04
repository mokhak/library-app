import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.create_books_table()
        
    def __del__(self):
        self.conn.commit()
        self.conn.close()
        
    def create_books_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Books" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Title TEXT,
            Author TEXT, 
            PublishedYear INTEGER,
            Genre TEXT,
            IsAvailable BOOLEAN DEFAULT 1
        );
        """
        self.conn.execute(query)
        
class BookItem:
    TABLENAME = "Books"
    
    def __init__(self):
        self.conn = sqlite3.connect('library.db')
        self.conn.row_factory = sqlite3.Row
        
    def __del__(self):
        self.conn.commit()
        self.conn.close()
        
    def get_by_id(self, book_id):
        query = f"SELECT * FROM {self.TABLENAME} WHERE id={book_id}"
        result = self.conn.execute(query).fetchone()
        return dict(result) if result else None
    
    def create(self, params):
        query = f'INSERT INTO {self.TABLENAME} (Title, Author, PublishedYear, Genre) ' \
                f'VALUES ("{params.get("Title")}", "{params.get("Author")}", "{params.get("PublishedYear")}", "{params.get("Genre")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, book_id):
        query = f"DELETE FROM {self.TABLENAME} WHERE id={book_id}"
        self.conn.execute(query)
        return {"status": "Book deleted successfully"}
    
    def update(self, book_id, update_dict):
        set_query = ", ".join([f'{column} = "{value}"' for column, value in update_dict.items()])
        query = f"UPDATE {self.TABLENAME} SET {set_query} WHERE id={book_id}"
        self.conn.execute(query)
        return self.get_by_id(book_id)
    
    def list_items(self):
        query = f"SELECT * FROM {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        return [dict(row) for row in result_set]