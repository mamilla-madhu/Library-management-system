import mysql.connector  # ✅ Required to ensure MySQL connector is available in imported functions

from addbook import add_book
from viewbooks import view_books
from issuebook import issue_book
from returnbook import return_book
from deletebook import delete_book

while True:
    print("\n=== Library Management System ===")
    print("1. ADD BOOK")
    print("2. VIEW ALL BOOKS")
    print("3. ISSUE BOOK")
    print("4. RETURN BOOK")
    print("5. DELETE BOOK")
    print("6. EXIT")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        delete_book()
    elif choice == "6":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

    input("\nPress Enter to continue...")
