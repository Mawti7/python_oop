# OOP Exercise: Inheritance
# Demonstrates class inheritance and method overriding

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

if __name__ == "__main__":
    # Create an EBook instance
    ebook = EBook("Digital Python Guide", "Jane Smith", 25.00, 2.5)
    
    # Print details (overridden method)
    print("EBook details:")
    print(ebook.get_details())
    
    # Print discounted price
    print(f"Original price: ${ebook.price}")
    print(f"Discount: {ebook.get_discount()}")
    print(f"Price after discount: ${ebook.get_price_after_discount():.2f}")
    
    # Set a different discount
    ebook.set_discount(0.2)
    print(f"\nAfter setting 20% discount:")
    print(f"Price after discount: ${ebook.get_price_after_discount():.2f}")
