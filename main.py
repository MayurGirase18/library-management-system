books = []
book_details = {}
issued_books = set()

def add_book():
    book_id = input("Enter Book ID: ")

    if book_id in book_details:
        print("Book ID already exist!")
        return
    
    title = input("Enter Book Title: ")
    author = input("Enter Book Author name: ")

    books.append((book_id, title))

    book_details[book_id] = {
        "title": title,
        "author": author
    }

    print("Book added successfully...")


def search_book():
    if len(books) == 0:
        print("No book available!")
        return
    
    else:
        book_id = input("Enter Book ID: ")

        if book_id in book_details:
            print("Book found.")
            print(f"{' Book Details':-^20}")
            print("Book ID: ", book_id)
            print("Book title: ", book_id["title"])
            print("Book Author: ", book_id["author"])

            if book_id in issued_books:
                print("Status: Issued")

            else:
                print("Status: Available")

        else:
            print("Book not found!")


def issue_book():
    if len(books) == 0:
        print("No book available!")
        return
    
    book_id = input("Enter Book ID: ")

    if book_id not in book_details:
        print("Book not found!")
        return
    
    else:
        if book_id in issued_books:
            print("Book is already issued!")
            return

        else:
            issued_books.add(book_id)
            print("Book Issued Successfully")


def return_book():
    if len(books) == 0:
        print("No book available!")
        return
    
    book_id = input("Enter Book ID: ")

    if book_id not in book_details:
        print("Book not found!")
        return
    
    else:
        if book_id not in issued_books:
            print("Book was not issued!")
            return
        else:
            issued_books.remove(book_id)
            print("Book returned successfully")


def delete_book():
    if len(books) == 0:
        print("No book available!")
        return
    
    book_id = input("Enter Book ID: ")

    if book_id not in book_details:
        print("Book not found!")
        return
    
    else:
        del book_details[book_id]

        for book in books:
            if book[0] == book_id:
                books.remove(book)
                break

        issued_books.remove(book_id)   

        print("Books deleted successfully...")


def show_all_books():
    if len(books) == 0:
        print("No book available!")
        return
    
    else:
        print(f"{' Library Books ':-^30}")

        for book_id, title in books:
            author = book_details["book_id"]["author"]

            status = "Issued" if book_id in issued_books else "Available"

            print(f"""
Book ID         : {book_id}
Book Title      : {title}
Book Author     : {author}
Book Status     : {status}
{'':-^20}""")
            

def main():
    print(f"{'\n    Library Management System   \n':=^100}")

    while True:
        print("Menu")
        print("1.Add Book\n2. Search Book\n3. Issue Book\n4. Return Book\n5. Delete Book\n6. Show All Books\n7. Exit\n")
        choice = int(input("Enter your choice(1-7): "))

        if choice == 1:
            add_book()

        elif choice == 2:
            search_book()

        elif choice == 3:
            issue_book()

        elif choice == 4:
            return_book()

        elif choice == 5:
            delete_book

        elif choice == 6:
            show_all_books

        elif choice == 7:
            print("Goodbye...")
            break

        else:
            print("Invalid choice!!")


main()
