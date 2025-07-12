import mysql.connector

def delete_book():
    try:
        # Step 1: Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="madhumamilla",  # Replace with your password
            database="library"
        )
        cursor = conn.cursor()

        # Step 2: Ask for Book ID to delete
        book_id = input("Enter the Book ID to delete: ")

        # Step 3: Delete from table
        query = "DELETE FROM books WHERE id = %s"
        data = (book_id,)
        cursor.execute(query, data)
        conn.commit()

        # Step 4: Confirm deletion
        if cursor.rowcount > 0:
            print("✅ Book deleted successfully.")
        else:
            print("❗ Book not found.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        cursor.close()
        conn.close()
