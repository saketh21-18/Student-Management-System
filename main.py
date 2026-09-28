class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Roll No: {self.roll_no} | Name: {self.name} | Marks: {self.marks}"


class StudentManager:
    def __init__(self):
        self.students = []

    # CREATE
    def add_student(self, roll_no, name, marks):
        if self.find_student(roll_no):
            print("Roll number already exists.")
            return
        self.students.append(Student(roll_no, name, marks))
        print("Student added.")

    # READ
    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        for s in self.students:
            print(s)

    # UPDATE
    def update_student(self, roll_no, new_name, new_marks):
        student = self.find_student(roll_no)
        if student:
            student.name = new_name
            student.marks = new_marks
            print("Student updated.")
        else:
            print("Student not found.")

    # DELETE
    def delete_student(self, roll_no):
        student = self.find_student(roll_no)
        if student:
            self.students.remove(student)
            print("Student deleted.")
        else:
            print("Student not found.")

    # SEARCH
    def find_student(self, roll_no):
        for s in self.students:
            if s.roll_no == roll_no:
                return s
        return None

    def search_by_name(self, keyword):
        results = [s for s in self.students if keyword.lower() in s.name.lower()]
        if results:
            for s in results:
                print(s)
        else:
            print("No matching students.")

    # SORT
    def sort_by_marks(self):
        for s in sorted(self.students, key=lambda x: x.marks, reverse=True):
            print(s)

    def sort_by_name(self):
        for s in sorted(self.students, key=lambda x: x.name.lower()):
            print(s)


def main():
    manager = StudentManager()
    while True:
        print("\n--- STUDENT MANAGEMENT ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search by Roll No")
        print("6. Search by Name")
        print("7. Sort by Marks (High to Low)")
        print("8. Sort by Name (A-Z)")
        print("9. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            manager.add_student(input("Roll No: "), input("Name: "), float(input("Marks: ")))
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.update_student(input("Roll No: "), input("New name: "), float(input("New marks: ")))
        elif choice == "4":
            manager.delete_student(input("Roll No: "))
        elif choice == "5":
            s = manager.find_student(input("Roll No: "))
            print(s if s else "Student not found.")
        elif choice == "6":
            manager.search_by_name(input("Name keyword: "))
        elif choice == "7":
            manager.sort_by_marks()
        elif choice == "8":
            manager.sort_by_name()
        elif choice == "9":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


main()
