# assessment.py
# Parent Class: Assessment
# Child Classes: Quiz, Exam, Project

class Assessment:
    def __init__(self, title, max_score):
        self.title = title
        self.max_score = max_score

    # Calculate percentage
    def calculate_percentage(self, score):
        return (score / self.max_score) * 100

    # General message
    def grade_message(self, score):
        percentage = self.calculate_percentage(score)

        if percentage >= 80:
            return "Excellent"

        elif percentage >= 55:
            return "Passed"

        else:
            return "Failed"

    # Display assessment information
    def display_info(self):
        print(f"{self.title} - Max Score: {self.max_score}")


# Quiz Class

class Quiz(Assessment):

    def display_info(self):
        print(f"Quiz: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 90:
            return "Great job! You got A."

        elif percentage >= 80:
            return "Great job! You got B."

        elif percentage >= 70:
            return "Good job! You got C."

        elif percentage >= 60:
            return "Good work! You got D."

        else:
            return "Keep practicing! You got F."


# Exam Class

class Exam(Assessment):

    def display_info(self):
        print(f"Exam: {self.title} - Max Score: {self.max_score}")

    def grade_message(self, score):

        percentage = self.calculate_percentage(score)

        if percentage >= 55:
            return "Passed exam"

        else:
            return "Failed exam"