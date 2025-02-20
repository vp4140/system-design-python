from collections import defaultdict

class Book:
    def __init__(self, title: str, author: str, ISBN: str, category: str, count: int = 0):
        self.ISBN = ISBN  # Fixed comma issue
        self.title = title
        self.author = author
        self.category = category
        self.count = count

class User:
    def __init__(self, name: str):
        self.name = name
        self.books = []  # Changed to a more meaningful name

    def buy_book(self, book: Book):
        self.books.append(book)

    def get_book_count(self):
        return len(self.books)

class Library:
    def __init__(self):
        self.books = []  # Fixed incorrect declaration
        self.mapper = defaultdict(set)  # Maps users to borrowed books

    def add_books(self, book: Book):
        self.books.append(book)

    def search_books(self, category: str, search_str: str):
        search_list = []
        for book in self.books:
            if getattr(book, category, None) == search_str:  # Fixed incorrect dictionary key access
                search_list.append(book)
        return search_list

    def borrow_books(self, ISBN: str, user: User):
        for book in self.books:
            if book.ISBN == ISBN:  # Changed from book_id to ISBN
                if book.count > 0:
                    book.count -= 1
                    user.buy_book(book)
                    self.mapper[user].add(book)
                    return "Book borrowed successfully"
                else:
                    return "No books left for this one"
        return "No such book found"

    def return_books(self, ISBN: str, user: User):
        for book in self.books:
            if book.ISBN == ISBN and book in self.mapper[user]:  # Ensuring user actually borrowed it
                book.count += 1
                user.books.remove(book)
                self.mapper[user].remove(book)
                return "Book returned successfully"
        return "No such book borrowed by this user"

# Example usage
if __name__ == "__main__":
    lib = Library()
    b1 = Book("The Alchemist", "Paulo Coelho", "123456", "Fiction", 5)
    u1 = User("Alice")

    lib.add_books(b1)
    print(lib.borrow_books("123456", u1))  # Borrow book
    print(lib.return_books("123456", u1))  # Return book
