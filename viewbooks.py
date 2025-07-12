
import mysql.connector

def view_books():
    try:
        # Step 1: Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="madhumamilla",  # Replace with your password
            database="library"
        )
        cursor = conn.cursor()

        # Step 2: Execute SELECT query
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()

        # Step 3: Display books
        if result:
            print("\n📚 Books in Library:\n")
            for book in result:
                print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Year: {book[3]}")
        else:
            print("❗ No books found in the library.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        # Step 4: Close connection
        cursor.close()
        conn.close()
