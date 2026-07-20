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