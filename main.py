# main.py

from student import Student
from course import Course
from assessment import Quiz, Exam, Project
from gradebook import Gradebook


def main():

    gb = Gradebook()

    while True:

        print("\n===== STUDENT GRADEBOOK SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Add Course")
        print("6. View Courses")
        print("7. Enroll Student")
        print("8. Add Assessment")
        print("9. Record Grade")
        print("10. Show Report")
        print("11. Show Ranking")
        print("12. Dashboard")
        print("0. Exit")

        choice = input("Choose option: ")



