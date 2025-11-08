
---

## Design Overview

### Class: `Book`
**Attributes**
- `title` (str): Book title  
- `author` (str): Author name  
- `copies` (int): Number of available copies  

**Key Methods**
- `borrow()`: Reduces the number of available copies by one when borrowed  
- `return_book()`: Increases the number of available copies by one when returned  
- `__str__()`: Returns a formatted string representation of the book  

---

### Class: `Member`
**Attributes**
- `name` (str): Full name of the library member  
- `member_id` (int): Unique member identification number  
- `borrowed_books` (list): List of books currently borrowed  

**Key Methods**
- `borrow_book(book)`: Allows borrowing a book if the member has fewer than 3 books  
- `return_book(book)`: Returns a borrowed book  
- `display_books()`: Displays all books currently borrowed by the member  

---

### Class: `Library`
**Attributes**
- `books` (list): Collection of `Book` objects  
- `members` (list): Collection of `Member` objects  

**Key Methods**
- `add_book(title, author, copies)`: Adds a new book to the library  
- `add_member(name)`: Registers a new member in the library  
- `borrow_book(member_name, book_title)`: Allows a member to borrow a book  
- `return_book(member_name, book_title)`: Allows a member to return a book  
- `display_available_books()`: Displays all books that are currently available  
- `display_member_books(member_name)`: Displays all books borrowed by a given member  

---

## Testing

### Test Coverage
All tests are implemented in **`test_oop.py`**, covering both normal and exceptional scenarios.

#### Basic Operations
- Adding books and members  
- Borrowing and returning books  
- Displaying available books  
- Displaying borrowed books per member  

#### Edge Cases
- Borrowing books with no copies left  
- Borrowing more than 3 books per member  
- Returning books that were not borrowed  
- Attempting operations with non-existent books or members  

---

## How to Run the Test Code

1. Clone this repository:
   ```bash
   git clone <your-repo-link>
   cd library_management
