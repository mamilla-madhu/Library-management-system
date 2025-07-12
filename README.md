This is a console-based Library Management System built using Python and MySQL. It helps manage books, students, and transactions (issuing/returning books) with simple menu-driven options.

---

✅ Features
Add new books to the library 📗
View all available books 📘
Issue books to students 🎓
Return books back to the library 🔄
Delete unavailable or damaged books ❌
Real-time quantity update of books 🔢
Data stored in MySQL database 💾

---

🛠️ Technologies Used
Python – for backend logic and console interaction
MySQL – to store book, student, and transaction records
MySQL Connector – to connect Python with MySQL

---

📂 Project Structure
📁 Library-Management-System/
├── add_book.py
├── delete_book.py
├── issue_book.py
├── return_book.py
├── view_books.py
├── library_console.py
├── books_table.sql
├── students_table.sql
├── transactions_table.sql
└── README.md

---

🔌 Setup Instructions
1️⃣ Database Setup
Open MySQL Workbench or any SQL tool
Run the .sql files to create the following tables:
books
students
transactions

2️⃣ Python Setup
Make sure Python is installed
Install MySQL connector:
pip install mysql-connector-python

3️⃣ Run the Project
Simply run library_console.py in terminal or command prompt:
python library_console.py
