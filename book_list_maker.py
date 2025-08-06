def main():
    filename = input("Enter the filename to your book list (e.g., books.txt): ")
    books = []
    print_book_list(filename)
    while True:
        book_details = get_book_details()
        books.append(book_details)
        another = input("Do you want to add another book? (yes/no): ")
        if another.lower() != "yes":
            break
    save_books_to_file(filename, books)
    print(f"Books saved to {filename}.")


def get_book_details():
    """
    takes no argument, return a string in csv format of the book's title, author & publication year
    """
    title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    year = input("Enter the year of publication: ")
    # TODO: I should make sure that the name that the user enterd don't have a comma and that the year is valid number
    # NOTE: use csv library for python to fix this problem
    # TODO: make sure it gives the user the flexiblity to save in csv or any other formats like txt, md or other.
    return f"{title}, {author}, {year}\n"


def save_books_to_file(filename, books):
    with open(filename, "a") as file:
        file.writelines(books)
        # TODO: I should add an index so that user can see the number of books


def print_book_list(filename):
    try:
        with open(filename, "r") as file:
            print("current book list\n--------------")
            print(file.read())
    except FileNotFoundError:
        print("the file doesn't exists, try again.")


if __name__ == "__main__":
    main()
