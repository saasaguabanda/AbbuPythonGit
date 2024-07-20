#ntroduced in Python 3.10, the match statement offers a powerful and concise way to perform pattern matching based on values.

def greet(person):
    match person:
        case "Alice":
            print("Hello, Alice!")
        case "Bob":
            print("Hello, Bob!")
        case _:
            print("Hello, stranger!")

greet("Alice")  # Output: Hello, Alice!
greet("Charlie")  # Output: Hello, stranger!