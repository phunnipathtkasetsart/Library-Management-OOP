# Library Management System - Procedural Style

class Library():
    def __init__(self):
        self.books = []
        self.members = []
        self.borrowed_books = []
        
    def add_book(self,book_id, title, author, available_copies):
        """Add a new book to the library"""
        self.books.append(Book(book_id, title, author, available_copies, available_copies))
        print(f"Book '{title}' added successfully!")

    def add_member(self,member_id, name, email):
        """Register a new library member"""
        self.members.append(Member(member_id, name, email, []))
        print(f"Member '{name}' registered successfully!")

    def find_book(self,book_id):
        """Find a book by ID"""
        for book in self.books:
            if book.id == book_id:
                return book
        return None
    
    def find_member(self,member_id):
        """Find a member by ID"""
        for member in self.members:
            if member.id == member_id:
                return member
        return None
    
    def borrow_book(self,member_id, book_id):
        """Process a book borrowing transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member:
            print("Error: Member not found!")
            return False
        
        if not book:
            print("Error: Book not found!")
            return False
        
        if book.available_copies <= 0:
            print("Error: No copies available!")
            return False
        
        if len(member.borrowed_books) >= 3:
            print("Error: Member has reached borrowing limit!")
            return False
        
        # Process the borrowing
        book.available_copies -= 1
        member.borrowed_books.append(book_id)
        self.borrowed_books.append(Transaction(member_id, book_id, member.name, book.title))
        
        print(f"{member.name} borrowed '{book.title}'")
        return True

    def return_book(self,member_id, book_id):
        """Process a book return transaction"""
        member = self.find_member(member_id)
        book = self.find_book(book_id)
        
        if not member or not book:
            print("Error: Member or book not found!")
            return False
        
        if book_id not in member.borrowed_books:
            print("Error: This member hasn't borrowed this book!")
            return False
        
        # Process the return
        book.available_copies += 1
        member.borrowed_books.remove(book_id)
        
        # Remove from borrowed_books list
        for i, transaction in enumerate(self.borrowed_books):
            if transaction.member_id == member_id and transaction.book_id == book_id:
                self.borrowed_books.pop(i)
                break
        
        print(f"{member.name} returned '{book.title}'")
        return True
    def display_available_books(self):
        """Display all books with available copies"""
        print("\n=== Available Books ===")
        for book in self.books:
            if book.available_copies > 0:
                print(f"{book.title} by {book.author} - {book.available_copies} copies available")

    def display_member_books(self,member_id):
        """Display books borrowed by a specific member"""
        member = self.find_member(member_id)
        if not member:
            print("Error: Member not found!")
            return
        
        print(f"\n=== Books borrowed by {member.name} ===")
        if not member.borrowed_books:
            print("No books currently borrowed")
        else:
            for book_id in member.borrowed_books:
                book = self.find_book(book_id)
                if book:
                    print(f"- {book.title} by {book.author}")


class Transaction():
    def __init__(self,member_id, book_id, member_name, book_title):
        self.member_id = member_id
        self.book_id = book_id
        self.member_name = member_name
        self.book_title = book_title


class Book():
    def __init__(self,id, title, author, total_copies, available_copies):
        self.id = id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = available_copies

class Member():
    def __init__(self,id, name, email, borrowed_books):
        self.id = id
        self.name = name
        self.email = email
        self.borrowed_books = borrowed_books
    


l = Library()
l.add_book(1, "Python Crash Course", "Eric Matthes", 2)
l.add_book(2, "Clean Code", "Robert Martin", 2)
l.add_member(101, "Alice Smith", "alice@email.com")
print(l.find_book(1))
print(l.find_member(101))

l.borrow_book(101, 1) 
l.return_book(101, 1)