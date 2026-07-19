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