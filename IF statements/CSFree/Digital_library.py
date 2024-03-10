# Python program for managing a digital library. Use a while loop to display a menu with the following options:
digital_libary = [] 

while True:
    print("1. Add book to library")
    print("2. View library")
    print("3. Search for a book")
    print("4. Exit")

    try:
        choice = int("Select your choice (1 - 4): ")
    except ValueError: 
        print("Invalid input. Please enter a valid number")
        continue

    if choice == 1:
        book_title = input("Select the title of the book: ")
        book_author = input("Who is the author of the book: ")
        publication_year = input("The publication year")
        digital_libary.append({'Title': book_title, 'Author': book_author, 'Year': publication_year})
        print(f"add book {book_title} to library.")

    elif choice == 2:
        if not digital_libary:
            print("The library is empty.")
        else:
            for i, book in enumerate(digital_libary,):
                print(f"{i + 1}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
            
    elif choice == 3:
        search_title = input("Enter the book title to search: ")
        matching_books = [book for book in digital_libary if search_title.lower() in book['title'].lower()]
        if not matching_books:
            print(f"No books found with title '{search_title}'.")
        else:
            print("Matching books:")
            for i, book in enumerate(matching_books, 1):
                print(f"{i + 1}. Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

    elif choice == 4:
        print("Exit the digital library program")
        break

    else:
        print("Invalid input. Kindly enter a number between 1 and 4. ")

    print("Which other book would you like to read?")
