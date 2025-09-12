# OOP Exercise: Encapsulation
# Demonstrates private attributes, getters, setters, and validation

class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1  # private attribute with default value
    
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

if __name__ == "__main__":
    # Create a book instance
    book = Book("Python Programming", "John Doe", 50.00)
    
    # Print original details
    print("Original book details:")
    print(book.get_details())
    print(f"Original price: ${book.price}")
    print(f"Default discount: {book.get_discount()}")
    print(f"Price after discount: ${book.get_price_after_discount():.2f}")
    
    # Set a new discount via setter
    print("\nSetting discount to 0.25 (25%):")
    book.set_discount(0.25)
    print(f"New discount: {book.get_discount()}")
    print(f"Price after new discount: ${book.get_price_after_discount():.2f}")
    
    # Try to set an invalid discount
    print("\nTrying to set invalid discount (1.5):")
    try:
        book.set_discount(1.5)
    except ValueError as e:
        print(f"Error: {e}")
