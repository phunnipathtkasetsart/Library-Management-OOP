
---

## Design Overview

### Class: `Library`
**Purpose:** Central management class that stores all books, members, and transactions.

**Attributes**
- `books` (list): Stores all `Book` objects in the library  
- `members` (list): Stores all `Member` objects registered in the library  
- `borrowed_books` (list): Stores `Transaction` objects representing active borrowings  

**Key Methods**
- `add_book(book_id, title, author, available_copies)`: Adds a new book to the collection  
- `add_member(member_id, name, email)`: Registers a new member  
- `find_book(book_id)`: Searches for a book by ID  
- `find_member(member_id)`: Searches for a member by ID  
- `borrow_book(member_id, book_id)`: Allows a member to borrow a book if conditions are met  
- `return_book(member_id, book_id)`: Allows a member to return a previously borrowed book  
- `display_available_books()`: Displays all books that currently have available copies  
- `display_member_books(member_id)`: Shows all books borrowed by a specific member  

---

### Class: `Book`
**Purpose:** Represents a single book in the library.

**Attributes**
- `id` (int): Unique identifier for the book  
- `title` (str): Title of the book  
- `author` (str): Author of the book  
- `total_copies` (int): Total number of copies owned by the library  
- `available_copies` (int): Number of copies currently available for borrowing  

**Typical Behavior**
- A book can be borrowed if `available_copies > 0`  
- When returned, `available_copies` increases by one  

---

### Class: `Member`
**Purpose:** Represents a library member who can borrow and return books.

**Attributes**
- `id` (int): Unique member ID  
- `name` (str): Full name of the member  
- `email` (str): Contact email address  
- `borrowed_books` (list): List of `book_id`s currently borrowed  

**Borrowing Rules**
- A member may borrow up to **3 books** at the same time.  
- Members cannot borrow books that are unavailable.  
- Returning a book removes it from the borrowed list.

---

### Class: `Transaction`
**Purpose:** Records a borrowing transaction.

**Attributes**
- `member_id` (int): ID of the borrowing member  
- `book_id` (int): ID of the borrowed book  
- `member_name` (str): Member’s name  
- `book_title` (str): Book title  

**Usage**
- Stored inside `Library.borrowed_books` to track active loans.

---

## Testing

### Test Coverage
All tests are contained in **`test_oop.py`**, verifying both normal and edge-case behaviors.

#### Basic Operations
- Adding books and members  
- Borrowing and returning books  
- Displaying available books  
- Displaying member’s borrowed books  

#### Edge Cases
- Borrowing books when no copies are left  
- Exceeding borrowing limit (more than 3 books)  
- Returning books not borrowed by the member  
- Attempting to borrow or return non-existent books or members  

---

## How to Run the Test Code

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd library_management

