
from datetime import date
import mysql.connector
from datetime import date  # ✅ Import required

def return_book():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="madhumamilla",
            database="library"
        )
        cursor = conn.cursor()

        student_id = input("Enter Student ID: ")
        book_id = input("Enter Book ID: ")
        return_date = date.today()
        status = "returned"

        # ✅ Use correct table: transactions
        query = """
        UPDATE transactions 
        SET return_date = %s, status = %s 
        WHERE student_id = %s AND book_id = %s AND status = 'issued'
        """
        data = (return_date, status, student_id, book_id)
        cursor.execute(query, data)

        if cursor.rowcount > 0:
            # ✅ Increase quantity
            cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE id = %s", (book_id,))
            conn.commit()
            print("✅ Book return recorded and quantity updated.")
        else:
            print("❗ No matching issued book found or already returned.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        cursor.close()
        conn.close()


