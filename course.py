# course.py
# Course Class

class Course:

    def __init__(self, course_code, course_name):
        self.course_code = course_code
        self.course_name = course_name

        # List of student IDs
        self.students = []

        # List of Assessment Objects
        self.assessments = []


    # Add Student

    def add_student(self, student_id):

        if student_id not in self.students:
            self.students.append(student_id)
            print("Student enrolled successfully.")

        else:
            print("Student is already enrolled.")

