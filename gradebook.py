# gradebook.py
# Main System Controller

class Gradebook:

    def __init__(self):
        # Stores Student objects
        self.students = {}

        # Stores Course objects
        self.courses = {}

        # Stores grades
        # {student_id: {course_code: {assessment: score}}}
        self.grades = {}

        # Passing rule
        self.passing_grade = 55

    # ADD STUDENT

    def add_student(self, student):
        self.students[student.get_id()] = student
        print("Student added successfully.")

    # VIEW STUDENTS

    def view_students(self):
        print("\n===== ALL STUDENTS =====")

        if not self.students:
            print("No students found.")
            return

        for student in self.students.values():
            print(student.display_info())

    # SEARCH STUDENT

    def search_student(self, keyword):
        print("\n===== SEARCH RESULT =====")

        found = False

        for student in self.students.values():
            if keyword.lower() in student.get_name().lower() or keyword in student.get_id():
                print(student.display_info())
                found = True

        if not found:
            print("No student found.")