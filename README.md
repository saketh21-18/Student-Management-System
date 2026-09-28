# 🎓 Student Management System

A terminal program with full CRUD operations for student records, plus searching and sorting.

## Concepts Used
OOP (classes) • CRUD • Searching • Sorting

## Requirements
- Python 3.7+
- No external libraries

## How to Run
```bash
python student_management.py
```
On Mac/Linux use `python3`.

## Menu
```
1. Add Student
2. View All Students
3. Update Student
4. Delete Student
5. Search by Roll No
6. Search by Name
7. Sort by Marks (High to Low)
8. Sort by Name (A-Z)
9. Exit
```

## How It Works
- The `Student` class stores roll number, name and marks.
- The `StudentManager` class keeps all students in a list and provides the operations:
  - **Create:** `add_student()` rejects duplicate roll numbers.
  - **Read:** `view_students()` prints every record.
  - **Update:** `update_student()` changes name and marks.
  - **Delete:** `delete_student()` removes a record.
- **Searching:** by exact roll number, or by part of a name (case-insensitive).
- **Sorting:** `sorted()` with a `lambda` key, by marks (descending) or name (A to Z).

## Example
```
Enter choice: 1
Roll No: 101
Name: Priya
Marks: 88
Student added.
```

## Important
⚠️ Data is stored **in memory only**. All records are lost when you exit the program.

## Tips
- Use a unique roll number for every student.
- Enter numbers only for marks.
- Add several students first, then try the sort options.

## Ideas to Extend
- Save and load students using a file
- Add grades (A, B, C) based on marks
- Add class average and topper display
