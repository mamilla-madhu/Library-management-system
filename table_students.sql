
use library;
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50),
    year INT,
    email VARCHAR(100),
    phone VARCHAR(15)
);