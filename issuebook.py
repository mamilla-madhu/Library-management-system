import mysql.connector
from datetime import date

def issue_book():
    try:
        # Step 1: Connect to MySQL
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="madhumamilla",  # Replace with your password
            database="library"
        )
        cursor = conn.cursor()

        # Step 2: Get details from user
        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")

        # Step 3: Check quantity
        cursor.execute("SELECT quantity FROM books WHERE id = %s", (book_id,))
        result = cursor.fetchone()

        if not result:
            print("❌ Book not found.")
            return

        quantity = result[0]
        if quantity <= 0:
            print("❌ Book is currently unavailable.")
            return

        # Step 4: Insert into transactions table
        issue_date = date.today()
        query = """
            INSERT INTO transactions (student_id, book_id, issue_date, return_date, status)
            VALUES (%s, %s, %s, NULL, %s)
        """
        data = (student_id, book_id, issue_date, "issued")
        cursor.execute(query, data)

        # Step 5: Update quantity
        cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE id = %s", (book_id,))

        conn.commit()
        print("✅ Book issued successfully.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        cursor.close()
        conn.close()
