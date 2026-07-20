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

    # RECORD GRADE

    def record_grade(self, student_id, course_code, assessment_title, score):

        # Validation
        if student_id not in self.students:
            print("Student not found!")
            return

        if course_code not in self.courses:
            print("Course not found!")
            return

        course = self.courses[course_code]
        assessment = course.find_assessment(assessment_title)

        if not assessment:
            print("Assessment not found!")
            return

        if score < 0 or score > assessment.max_score:
            print("Invalid score!")
            return

        # Save structure

        self.grades.setdefault(student_id, {})
        self.grades[student_id].setdefault(course_code, {})
        self.grades[student_id][course_code][assessment_title] = score

        print("Grade recorded successfully.")

    # CALCULATE AVERAGE

    def calculate_average(self, student_id, course_code):

        if student_id not in self.grades:
            return 0

        if course_code not in self.grades[student_id]:
            return 0

        course = self.courses[course_code]
        assessments = self.grades[student_id][course_code]

        total_percentage = 0
        count = 0

        for title, score in assessments.items():

            assessment = course.find_assessment(title)

            if assessment:
                percentage = assessment.calculate_percentage(score)
                total_percentage += percentage
                count += 1

        if count == 0:
            return 0

        return total_percentage / count

    # PASS / FAIL

    def get_result(self, average):

        if average >= self.passing_grade:
            return "Passed"
        else:
            return "Failed"

    # LETTER GRADE (CREATIVE FEATURE)

    def letter_grade(self, average):
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

    # DELETE STUDENT

    def delete_student(self, student_id):

        if student_id not in self.students:
            print("Student not found!")
            return

        # Remove from all courses
        for course in self.courses.values():
            if student_id in course.students:
                course.students.remove(student_id)

        # Remove from students dictionary
        del self.students[student_id]

        # Remove grades
        if student_id in self.grades:
            del self.grades[student_id]

        print("Student deleted successfully.")

    # SHOW REPORT

    def show_report(self, student_id):

        if student_id not in self.students:
            print("Student not found!")
            return

        student = self.students[student_id]

        print("\n===== STUDENT REPORT =====")
        student.display_info()

        if student_id not in self.grades:
            print("No grades available.")
            return

        overall_total = 0
        overall_count = 0

        for course_code, assessments in self.grades[student_id].items():

            course = self.courses[course_code]

            print(f"\nCourse: {course.course_name} ({course_code})")
            print("Grades:")

            total_percentage = 0
            count = 0

            for title, score in assessments.items():

                assessment = course.find_assessment(title)

                if assessment:
                    percentage = assessment.calculate_percentage(score)

                    print(
                        f"{title}: {score}/{assessment.max_score} = {percentage:.2f}%"
                    )

                    total_percentage += percentage
                    count += 1

            if count != 0:
                average = total_percentage / count
            else:
                average = 0

            print(f"Average: {average:.2f}%")
            print(f"Letter Grade: {self.letter_grade(average)}")
            print(f"Result: {self.get_result(average)}")

            overall_total += average
            overall_count += 1

        if overall_count != 0:
            overall_average = overall_total / overall_count
        else:
            overall_average = 0

        print("\n===== OVERALL RESULT =====")
        print(f"Overall Average: {overall_average:.2f}%")
        print(f"Final Letter Grade: {self.letter_grade(overall_average)}")
        print(f"Final Result: {self.get_result(overall_average)}")

    # STUDENT RANKING (CREATIVE FEATURE 2)

    def show_ranking(self):

        ranking = []

        for student_id in self.students:

            total = 0
            count = 0

            if student_id in self.grades:

                for course in self.grades[student_id].values():
                    for score in course.values():
                        total += score
                        count += 1

            avg = total / count if count != 0 else 0
            ranking.append((student_id, avg))

        ranking.sort(key=lambda x: x[1], reverse=True)

        print("\n===== STUDENT RANKING =====")

        for i, (student_id, avg) in enumerate(ranking, 1):
            name = self.students[student_id].get_name()
            print(f"{i}. {name} ({student_id}) - {round(avg, 2)}")

    # DASHBOARD (BONUS FEATURE)

    def dashboard(self):

        print("\n===== DASHBOARD =====")
        print("Total Students :", len(self.students))
        print("Total Courses  :", len(self.courses))

        total_assessments = 0
        for course in self.courses.values():
            total_assessments += len(course.assessments)

        print("Total Assessments:", total_assessments)