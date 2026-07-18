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