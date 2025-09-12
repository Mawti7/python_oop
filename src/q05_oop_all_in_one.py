"""
OOP Exercise: Combined Concepts
Demonstrates composition, dunder methods, class methods, and validation

Author: Aditya Kasyap
Website: https://www.adityakasyap.com
"""

class Price:
    def __init__(self, value: float, currency: str = "INR"):
        if value < 0:
            raise ValueError("Price value cannot be negative")
        if not currency:
            raise ValueError("Currency cannot be empty")
        
        self.value = value
        self.currency = currency
    
    def __repr__(self):
        return f"Price({self.value}, '{self.currency}')"
    
    def __str__(self):
        return f"{self.currency} {self.value:.2f}"

class Book:
    def __init__(self, title: str, author: str, price: Price):
        if not title or not author:
            raise ValueError("Title and author cannot be empty")
        
        self.title = title
        self.author = author
        self.price = price
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title and self.author == other.author
    
    def __str__(self):
        return f"'{self.title}' by {self.author} - {self.price}"
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.price!r})"
    
    @classmethod
    def from_dict(cls, d: dict) -> 'Book':
        price = Price(d['price'], d.get('currency', 'INR'))
        return cls(d['title'], d['author'], price)

class Inventory:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Only Book objects can be added to inventory")
        self._books.append(book)
    
    def remove_book(self, title: str, author: str):
        for i, book in enumerate(self._books):
            if book.title == title and book.author == author:
                return self._books.pop(i)
        raise ValueError(f"Book '{title}' by {author} not found in inventory")
    
    def find_by_author(self, author: str) -> list[Book]:
        return [book for book in self._books if book.author == author]
    
    def __len__(self):
        return len(self._books)
    
    def __iter__(self):
        return iter(self._books)
    
    def __str__(self):
        if not self._books:
            return "Inventory is empty"
        return "\n".join(f"{i+1}. {book}" for i, book in enumerate(self._books))

if __name__ == "__main__":
    # Create 3 books via from_dict
    book_data = [
        {"title": "Python Programming", "author": "John Doe", "price": 499.00, "currency": "INR"},
        {"title": "Data Structures", "author": "Jane Smith", "price": 599.00, "currency": "INR"},
        {"title": "Machine Learning", "author": "John Doe", "price": 799.00, "currency": "INR"}
    ]
    
    # Create inventory and add books
    inventory = Inventory()
    
    print("Creating books from dictionary data:")
    for data in book_data:
        book = Book.from_dict(data)
        inventory.add_book(book)
        print(f"Added: {book}")
    
    print(f"\nTotal books in inventory: {len(inventory)}")
    print("\nAll books in inventory:")
    print(inventory)
    
    # Remove one book
    print(f"\nRemoving 'Data Structures' by Jane Smith:")
    removed_book = inventory.remove_book("Data Structures", "Jane Smith")
    print(f"Removed: {removed_book}")
    print(f"Books remaining: {len(inventory)}")
    
    # Find books by author
    print(f"\nBooks by John Doe:")
    john_books = inventory.find_by_author("John Doe")
    for book in john_books:
        print(f"  - {book}")
    
    print(f"\nFinal inventory:")
    print(inventory)
