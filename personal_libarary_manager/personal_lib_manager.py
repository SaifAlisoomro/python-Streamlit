import json

class BookCollection:
    """A class to manage a collection of books."""

    def __init__(self):
        self.books_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books"""
        try:
            with open(self.storage_file, "r") as file:
                self.books_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books_list = []

    def save_to_file(self):
        """Save books to file"""
        with open(self.storage_file, "w") as file:
            json.dump(self.books_list, file, indent=4)

    def add_book(self):
        """Add a new book to the collection"""
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        year = input("Enter the year of publication: ")
        genre = input("Enter the genre of the book: ")
        is_read_book = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        book = {
            "title": title,
            "author": author,
            "year": year,
            "read": is_read_book,
            "genre": genre,
        }

        self.books_list.append(book)
        self.save_to_file()
        print(f"✅ Book '{title}' added to the collection.")

    def remove_book(self):
        """Remove a book from the collection"""
        title = input("Enter the title of the book to remove: ")
        for book in self.books_list:
            if book["title"].lower() == title.lower():
                self.books_list.remove(book)
                self.save_to_file()
                print(f"🗑️ Book '{title}' removed from the collection.")
                return
        print(f"❌ Book '{title}' not found in the collection.")

    def list_books(self):
        """List all books"""
        if not self.books_list:
            print("📚 No books in the collection.")
            return
        for idx, book in enumerate(self.books_list, start=1):
            status = "Read" if book["read"] else "Not Read"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

# Example menu to interact with the class
if __name__ == "__main__":
    collection = BookCollection()

    while True:
        print("\n📘 Book Collection Menu")
        print("1. List all books")
        print("2. Add a book")
        print("3. Remove a book")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            collection.list_books()
        elif choice == "2":
            collection.add_book()
        elif choice == "3":
            collection.remove_book()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select from 1 to 4.")
