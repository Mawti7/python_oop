# OOP Exercise: Class & Object Basics
# Demonstrates basic class definition, attributes, and methods

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
    
    def get_details(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

if __name__ == "__main__":
    # Create 3 Book instances
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 12.99)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 14.99)
    book3 = Book("1984", "George Orwell", 13.99)
    
    # Print their details using get_details()
    print(book1.get_details())
    print(book2.get_details())
    print(book3.get_details())
