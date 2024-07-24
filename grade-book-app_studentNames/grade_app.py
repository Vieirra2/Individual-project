#!/usr/bin/python3
print("Welcome to grading application!")

print("Please select an option")

import json

class Student:
    def __init__(self, email, names, courses_registered=None, GPA=0.0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered if courses_registered is not None else []
        self.GPA = GPA

    def calculate_GPA(self):
        if not self.courses_registered:
            self.GPA = 0.0
        else:
            total_credits = sum(course['credits'] for course in self.courses_registered)
            total_points = sum(course['score'] * course['credits'] for course in self.courses_registered)
            self.GPA = total_points / total_credits if total_credits != 0 else 0.0
        return self.GPA

    def register_for_course(self, course, score):
        self.courses_registered.append({
            'name': course.name,
            'trimester': course.trimester,
            'credits': course.credits,
            'score': score
        })

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        email = input("Enter student email: ")
        names = input("Enter student name: ")
        student = Student(email, names)
        self.student_list.append(student)
        self.save_data()

    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = float(input("Enter course credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        self.save_data()

    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        score = float(input("Enter course score: "))

        student = next((s for s in self.student_list if s.email == student_email), None)
        course = next((c for c in self.course_list if c.name == course_name), None)

        if student and course:
            student.register_for_course(course, score)
            self.save_data()
        else:
            print("Student or course not found.")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()
        self.save_data()

    def calculate_ranking(self):
        self.student_list.sort(key=lambda student: student.GPA, reverse=True)
        self.save_data()

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        return filtered_students

    def generate_transcript(self):
        student_email = input("Enter student email: ")
        student = next((s for s in self.student_list if s.email == student_email), None)
        if student:
            print(f"Transcript for {student.names}:")
            for course in student.courses_registered:
                print(f"Course: {course['name']}, Trimester: {course['trimester']}, Credits: {course['credits']}, Score: {course['score']}")
            print(f"GPA: {student.GPA}")
        else:
            print("Student not found.")

    def save_data(self):
        with open('students.json', 'w') as f:
            json.dump([student.__dict__ for student in self.student_list], f)
        with open('courses.json', 'w') as f:
            json.dump([course.__dict__ for course in self.course_list], f)

    def load_data(self):
        try:
            with open('students.json', 'r') as f:
                students_data = json.load(f)
                self.student_list = [Student(**data) for data in students_data]
            with open('courses.json', 'r') as f:
                courses_data = json.load(f)
                self.course_list = [Course(**data) for data in courses_data]
        except FileNotFoundError:
            print("No data files found, starting with empty lists.")

def main():
    gradebook = GradeBook()
    gradebook.load_data()

    while True:
        print("\nMenu:")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate GPA for All Students")
        print("5. Calculate Ranking")
        print("6. Search by Grade Range")
        print("7. Generate Transcript")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            gradebook.add_student()
        elif choice == '2':
            gradebook.add_course()
        elif choice == '3':
            gradebook.register_student_for_course()
        elif choice == '4':
            gradebook.calculate_GPA()
        elif choice == '5':
            gradebook.calculate_ranking()
            for student in gradebook.student_list:
                print(f"{student.names}: {student.GPA}")
        elif choice == '6':
            filtered_students = gradebook.search_by_grade()
            for student in filtered_students:
                print(f"{student.names}: {student.GPA}")
        elif choice == '7':
            gradebook.generate_transcript()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

