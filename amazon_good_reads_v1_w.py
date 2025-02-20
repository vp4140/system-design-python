
"""
Design GoodReads.
Users should be able to get a list of their books
Users should be able to get top K list of their books that their friends have read.
Users should be able to get top K list of books that their network has read. i.e. in a graph like manner go thru all the friend links and get the top books from this
"""
import heapq
from collections import deque

from abc import ABC, abstractmethod

class ReadingStrategy(ABC):
    def getTopBooks(self,books):
        pass

class TopKBooksUsingReads(ReadingStrategy):
    def getTopBooks(self,books):
        return sorted(books,key=lambda x:x.reads,reverse=True)


class TopKBooksUsingRating(ReadingStrategy):
    def getTopBooks(self,books):
        return sorted(books,key=lambda x:x.rating,reverse=True)

class ReadingContext:
    def __init__(self,strategy:ReadingStrategy):
        self.strategy = strategy
    def assignStrategy(self,strategy:ReadingStrategy):
        self.strategy = strategy
    def getTopBooks(self,books):
        books = self.strategy.getTopBooks(books)
        return books

class User:
    def __init__(self, userId):
        self.userId = userId
        self.books = []
        self.friends = []
        self.friendMap = {}


    def addBook(self, book):
        self.books.append(book)

    def addFriend(self, friend):
        self.friends.append(friend)
        self.friendMap[friend.userId] = friend.books

    def gettopKBooksAmongFreinds(self,k,strategy:ReadingStrategy ):
        minHeapBooks = []
        for friend in self.friends:
            for book in friend.books:
                minHeapBooks.append(book)
        return strategy.getTopBooks(minHeapBooks)[:k]


    def gettopKBooksNetwork(self,k,strategy:ReadingStrategy):
        all_books = []
        q = deque()
        q.append(self)

        for book in self.books:
            all_books.append(book)
        visited = set()
        visited.add(self)

        while q:
            node = q.popleft()

            for friend in node.friends:
                if friend not in visited:
                    for book in friend.books:
                        all_books.append(book)
                    q.append(friend)
                    visited.add(friend)


        return strategy.getTopBooks(all_books)[:k]



class Book:
    def __init__(self, bookId, title, author, rating,reads=0):
        self.bookId = bookId
        self.title = title
        self.author = author
        self.rating = rating
        self.reads = reads
    def __repr__(self):
        return f"Book Id: {self.bookId}, Title: {self.title}, Author: {self.author}, Rating: {self.rating}, Reads: {self.reads}"

if __name__ == "__main__":
    Book1 = Book(1,"California","Rahul",5)
    Book2 = Book(2,"SanDiego","Vishal",4)
    Book3 = Book(3,"Stpaul","Vishal",3)
    Book4 = Book(4,"Rochester","Neel",2)

    user1 = User(1)
    user2 = User(2)
    user3 = User(3)

    book1 = Book(101, "Book A", "Author X", 4.8, 100)
    book2 = Book(102, "Book B", "Author Y", 4.5, 200)
    book3 = Book(103, "Book C", "Author Z", 4.7, 150)

    user1.addBook(book1)
    user2.addBook(book2)
    user3.addBook(book3)

    user1.addFriend(user2)
    user2.addFriend(user3)
    strategy1 = TopKBooksUsingReads()
    strategy2 = TopKBooksUsingRating()
    print("Top books among friends:", user1.gettopKBooksAmongFreinds(2,strategy1))

    # Get top 2 books in the user's entire network
    print("Top books in the network:", user1.gettopKBooksNetwork(2,strategy2))








