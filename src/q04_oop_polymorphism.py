# OOP Exercise: Polymorphism
# Demonstrates duck typing and polymorphism

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"
    
    def get_discount(self):
        return self._discount
    
    def set_discount(self, discount):
        if 0.0 <= discount <= 0.9:
            self._discount = discount
        else:
            raise ValueError("Discount must be between 0.0 and 0.9")
    
    def get_price_after_discount(self):
        return self.price * (1 - self._discount)

class EBook(Book):
    def __init__(self, title, author, price, file_size):
        super().__init__(title, author, price)
        self.file_size = file_size
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}, File Size: {self.file_size}MB"

def print_details(obj):
    # Duck typing - works with any object that has get_details method
    print(obj.get_details())

if __name__ == "__main__":
    # Create a list with both Book and EBook instances
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99),
        EBook("Digital Python Guide", "Jane Smith", 25.00, 2.5),
        Book("To Kill a Mockingbird", "Harper Lee", 14.99),
        EBook("Advanced Algorithms", "Dr. Tech", 35.00, 5.2),
        Book("1984", "George Orwell", 13.99)
    ]
    
    # Iterate through the list and print details using polymorphism
    print("All books in the collection:")
    print("-" * 50)
    for i, book in enumerate(books, 1):
        print(f"{i}. ", end="")
        print_details(book)
        print()
