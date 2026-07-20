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

    # ADD COURSE

    def add_course(self, course):
        self.courses[course.course_code] = course
        print("Course added successfully.")

    # VIEW COURSES

    def view_courses(self):
        print("\n===== ALL COURSES =====")

        if not self.courses:
            print("No courses found.")
            return

        for course in self.courses.values():
            course.display_info()

    # ENROLL STUDENT IN COURSE

    def enroll_student(self, student_id, course_code):

        if student_id not in self.students:
            print("Student not found!")
            return

        if course_code not in self.courses:
            print("Course not found!")
            return

        # Add to course
        self.courses[course_code].add_student(student_id)

        # Add to student
        self.students[student_id].enroll_course(course_code)

        print("Student enrolled successfully.")

    # ADD ASSESSMENT

    def add_assessment(self, course_code, assessment):

        if course_code not in self.courses:
            print("Course not found!")
            return

        self.courses[course_code].add_assessment(assessment)
        print("Assessment added successfully.")