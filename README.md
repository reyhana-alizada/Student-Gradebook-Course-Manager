# Student Gradebook System

## Student Name
Reyhana Alizada

## Project Title
Student Gradebook & Course Manager

## Project Description

Student Gradebook System is a Python application that helps manage students, courses, assessments, and grades.
The system allows users to add students, create courses, enroll students, add assessments, record grades, and generate student reports.

## How to Run

1. Make sure Python is installed on your computer.
2. Open the project folder.
3. Run the main.py file:

### python main.py
Use the menu options to interact with the system.
## Classes Created
The project contains the following classes:
### Student: 
Manages student information such as ID, name, email, and enrolled courses.
### Course: 
Manages course information, students, and assessments.
### Assessment: 
The parent class for different assessment types.
#### Quiz: 
Inherits from Assessment and represents quiz assessments.
#### Exam: 
Inherits from Assessment and represents exam assessments.
#### Project: 
Inherits from Assessment and represents project assessments.
### Gradebook: 
Controls the main system operations such as managing students, courses, grades, reports, and ranking.
### main.py:
This file is the main entry point of the program.
It creates the Gradebook object, displays the menu, receives user choices, and connects the user's actions with the system functions.
## OOP Concepts Used
### Encapsulation
Encapsulation is used in the Student class. Student information such as student ID, name, and email are stored as private attributes. Getter and setter methods are used to access and update this information safely.
### Inheritance
Inheritance is used between the Assessment class and its child classes:
Quiz,
Exam,
Project
These classes inherit common properties and methods from the Assessment class.
### Method Overriding
Method overriding is used in the Quiz, Exam, and Project classes. The display_info() and grade_message() methods are overridden to provide different behaviors for each assessment type.
## Custom Features
1. Student Ranking
The system calculates student averages and displays a ranking list from the highest score to the lowest score.
2. Dashboard
The dashboard provides a quick summary of the system, including:
- Total number of students
- Total number of courses
- Total number of assessments

These features improve the usability of the system and provide more information about student performance.