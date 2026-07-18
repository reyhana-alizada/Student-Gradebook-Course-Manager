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