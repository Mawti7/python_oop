# Python OOP + HTTP Requests Assignment

This repository contains Python Object-Oriented Programming and HTTP requests exercises.

## Project Structure

```
python-apis-oop-assignment/
├─ src/
│  ├─ q01_oop_book_basics.py           # OOP: Class & Object Basics
│  ├─ q02_oop_encapsulation.py         # OOP: Encapsulation with private attributes
│  ├─ q03_oop_inheritance.py           # OOP: Inheritance with EBook subclass
│  ├─ q04_oop_polymorphism.py          # OOP: Polymorphism with duck typing
│  ├─ q05_oop_all_in_one.py            # OOP: Combined exercise (Price, Book, Inventory)
│  ├─ q06_requests_get.py               # HTTP: Basic GET request
│  ├─ q07_requests_get_params.py        # HTTP: GET with parameters
│  ├─ q08_requests_post.py              # HTTP: POST JSON request
│  ├─ q09_requests_put_delete.py        # HTTP: PUT & DELETE requests
│  ├─ q10_http_status_classifier.py     # HTTP: Status code classifier
│  ├─ q11_fetch_with_status_handling.py # HTTP: Practical status handling
│  └─ q12_cli_http_client.py           # HTTP: Mini CLI HTTP client
├─ tests/
│  └─ smoke_tests.py                    # Simple runner to test all files
├─ requirements.txt                      # Dependencies
└─ README.md                            # This file
```

## Requirements

- Python 3.10+
- requests library (see requirements.txt)

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Files

### OOP Exercises (Q01-Q05)
```bash
# Run individual OOP exercises
python src/q01_oop_book_basics.py
python src/q02_oop_encapsulation.py
python src/q03_oop_inheritance.py
python src/q04_oop_polymorphism.py
python src/q05_oop_all_in_one.py
```

### HTTP Requests Exercises (Q06-Q12)
```bash
# Run individual HTTP exercises
python src/q06_requests_get.py
python src/q07_requests_get_params.py
python src/q08_requests_post.py
python src/q09_requests_put_delete.py
python src/q10_http_status_classifier.py
python src/q11_fetch_with_status_handling.py

# CLI HTTP Client usage examples
python src/q12_cli_http_client.py GET https://jsonplaceholder.typicode.com/posts/1
python src/q12_cli_http_client.py POST https://jsonplaceholder.typicode.com/posts '{"title":"Test","body":"Content","userId":1}'
```

### Run All Tests
```bash
python tests/smoke_tests.py
```

## Exercise Descriptions

### OOP Exercises
- **Q01**: Basic Book class with attributes and methods
- **Q02**: Encapsulation with private discount attribute and getter/setter
- **Q03**: Inheritance with EBook subclass extending Book
- **Q04**: Polymorphism demonstrating duck typing
- **Q05**: Combined OOP concepts with Price, Book, and Inventory classes

### HTTP Requests Exercises
- **Q06**: Basic GET request to JSONPlaceholder API
- **Q07**: GET request with query parameters
- **Q08**: POST request with JSON payload
- **Q09**: PUT and DELETE requests
- **Q10**: HTTP status code classification function
- **Q11**: Practical status handling with error management
- **Q12**: Command-line HTTP client supporting GET, POST, PUT, DELETE

## Features Demonstrated

- Object-Oriented Programming concepts (encapsulation, inheritance, polymorphism)
- Class methods, dunder methods, and composition
- HTTP requests with the requests library
- JSON handling and error management
- Command-line interface development
- Exception handling and validation
