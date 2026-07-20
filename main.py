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

        # ADD STUDENT

        if choice == "1":

            sid = input("Student ID: ")
            name = input("Name: ")
            email = input("Email: ")

            student = Student(sid, name, email)
            gb.add_student(student)

        # VIEW STUDENTS

        elif choice == "2":
            gb.view_students()


        # SEARCH STUDENT

        elif choice == "3":
            keyword = input("Enter name or ID: ")
            gb.search_student(keyword)


        # DELETE STUDENT

        elif choice == "4":
            sid = input("Student ID: ")
            gb.delete_student(sid)


        # ADD COURSE

        elif choice == "5":

            code = input("Course Code: ")
            name = input("Course Name: ")

            course = Course(code, name)
            gb.add_course(course)


        # VIEW COURSES

        elif choice == "6":
            gb.view_courses()


        # ENROLL STUDENT

        elif choice == "7":

            sid = input("Student ID: ")
            code = input("Course Code: ")

            gb.enroll_student(sid, code)


        # ADD ASSESSMENT

        elif choice == "8":

            code = input("Course Code: ")
            title = input("Assessment Title: ")
            max_score = float(input("Max Score: "))

            print("Type: 1=Quiz, 2=Exam, 3=Project")
            t = input("Choose type: ")

            if t == "1":
                assessment = Quiz(title, max_score)

            elif t == "2":
                assessment = Exam(title, max_score)

            else:
                assessment = Project(title, max_score)

            gb.add_assessment(code, assessment)


        # RECORD GRADE

        elif choice == "9":

            sid = input("Student ID: ")
            code = input("Course Code: ")
            title = input("Assessment Title: ")
            score = float(input("Score: "))

            gb.record_grade(sid, code, title, score)


        # SHOW REPORT

        elif choice == "10":
            sid = input("Student ID: ")
            gb.show_report(sid)


        # SHOW RANKING

        elif choice == "11":
            gb.show_ranking()


        # DASHBOARD

        elif choice == "12":
            gb.dashboard()


        # EXIT

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")




if __name__ == "__main__":
    main()



