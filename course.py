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

    # Add Assessment

    def add_assessment(self, assessment):

        self.assessments.append(assessment)
        print("Assessment added successfully.")


    # Find Assessment

    def find_assessment(self, title):

        for assessment in self.assessments:

            if assessment.title.lower() == title.lower():
                return assessment

        return None


    # Display Course Information

    def display_info(self):

        print("\n========== COURSE ==========")
        print(f"Course Code : {self.course_code}")
        print(f"Course Name : {self.course_name}")
        print(f"Students    : {len(self.students)}")

        print("\nAssessments:")

        if len(self.assessments) == 0:
            print("No assessments added.")

        else:
            for assessment in self.assessments:
                assessment.display_info()