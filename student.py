# student.py
# Student Class

class Student:

    def __init__(self, student_id, name, email):
        # Private Attributes (Encapsulation)
        self.__student_id = student_id
        self.__name = name
        self.__email = ""

        # Set email using setter
        self.set_email(email)

        # Public Attribute
        self.courses = []

    # Getter Methods

    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    # Setter Methods

    def set_name(self, name):
        if len(name.strip()) >= 2:
            self.__name = name
        else:
            print("Invalid name!")


    def set_email(self, email):
        # Simple Email Validation
        if "@" in email and "." in email:
            self.__email = email
        else:
            print("Invalid email!")
            self.__email = "Not Available"

    # Enroll Student in Course

    def enroll_course(self, course_code):
        if course_code not in self.courses:
            self.courses.append(course_code)
        else:
            print("Student already enrolled in this course.")