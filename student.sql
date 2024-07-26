CREATE TABLE students (
    name TEXT PRIMARY KEY NOT NULL, 
    marks INTEGER NOT NULL
);

BEGIN TRANSACTION;
INSERT INTO students (name, marks) VALUES 
('Ramesh', 70), 
('Ramya', 100), 
('Ramana', 85);
COMMIT;


SELECT * FROM students;