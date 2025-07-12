import mysql.connector

def add_book():
    try:
        # Step 1: Connect to the database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="madhumamilla",   # Replace with your MySQL password
            database="library"
        )
        cursor = conn.cursor()

        # Step 2: Get book details from the user
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        year = input("Enter Year of Publication: ")
        quantity = int(input("Enter Quantity: "))

        # Step 3: Prepare and execute the SQL insert query
        query = "INSERT INTO books (title, author, year, quantity) VALUES (%s, %s, %s, %s)"
        data = (title, author, year, quantity)
        cursor.execute(query, data)

        # Step 4: Commit and confirm
        conn.commit()
        print("✅ Book added successfully.")

    except mysql.connector.Error as err:
        print("❌ Error:", err)

    finally:
        # Step 5: Close the connection
        cursor.close()
        conn.close()
