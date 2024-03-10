digital_library = []

while True:
    print("1. Add book to library")
    print("2. View library")
    print("3. Search for a book")
    print("4. Exit")

    try:
        choice = int(input("Select your choice (1 - 4): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if choice == 1:
        book_title = input("Enter the title of the book: ")
        book_author = input("Who is the author of the book: ")
        publication_year = input("Enter the publication year: ")
        digital_library.append({'Title': book_title, 'Author': book_author, 'Year': publication_year})
        print(f"Book '{book_title}' added to the library.")

    elif choice == 2:
        if not digital_library:
            print("The library is empty.")
        else:
            for i, book in enumerate(digital_library, 1):
                print(f"{i}. Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")

    elif choice == 3:
        search_title = input("Enter the book title to search: ")
        matching_books = [book for book in digital_library if search_title.lower() in book['Title'].lower()]
        if not matching_books:
            print(f"No books found with title '{search_title}'.")
        else:
            print("Matching books:")
            for i, book in enumerate(matching_books, 1):
                print(f"{i}. Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}")

    elif choice == 4:
        print("Exiting the digital library program.")
        break

    else:
        print("Invalid input. Please enter a number between 1 and 4.")

    print("What else would you like to do?")
