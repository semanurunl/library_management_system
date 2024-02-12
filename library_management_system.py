class Library:
    def __init__(self):

        self.file = open( "books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()

        if not lines:
            print("No books in the library.")
            return

        for line in lines:
            book_info = line.split(',')
            book_name, author, release_date, num_pages = book_info
            print(f"Book: {book_name}, Author: {author}, Release date: {release_date}, Page number: {num_pages}")

    def add_book(self):
        book_name = input("Enter book title: ")
        author = input("Enter author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")

        book_info = f"{book_name},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print(f"Book '{book_name}' added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        file = open("books.txt", "r")
        lines = file.readlines()

        index_to_remove = -1
        for i in range(len(lines)):
            if title_to_remove in lines[i]:
                index_to_remove = i
                break
        if index_to_remove != -1:
            lines.pop(index_to_remove)

            file = open("books.txt", 'w')
            file.writelines(lines)
            file.close()


            print(f"Book '{title_to_remove}' removed successfully.")
        else:
            print(f"Book '{title_to_remove}' not found in the library.")


lib = Library()

while True:
    print("\n*** MENU ***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("4) Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        lib.list_books()
    elif choice == "2":
        lib.add_book()
    elif choice == "3":
        lib.remove_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
