#!/usr/bin/python3
print("Welcome to the Grade book Application!\n")
print("Please select an action")

class Student:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.courses_registered = []
        self.GPA = {}

    def register_course(self, course):
        self.courses_registered.append(course)
        self.grades[course.name] = None

    def update_grade(self, course_name, grade):
        self.grades[course_name] = grade

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for course in self.courses_registered:
            grade = self.grades[course.name]
            if grade is not None:
                total_credits += course.credits
                total_points += grade * course.credits
        if total_credits == 0:
            return 0
        return total_points / total_credits


class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits
class Grade_Book:
    def __init__(self):
        self.student_list = []
        self.course_list = []
    def add_student(self):
        email = input("Enter student email: ")
        first_name = input("Enter student first name: ")
        last_name = input("Enter student last name: ")
        student = Student(email, first_name, last_name)
        self.student_list.append(student)
        print("Student added successfully!")
    def add_course(self):
        name = input("Enter course name: ")
        trimester = input("Enter course trimester: ")
        credits = int(input("Enter course credits: "))
        course = Course(name, trimester, credits)
        self.course_list.append(course)
        print("Course added successfully!")
    def register_student_for_course(self):
        student_email = input("Enter student email: ")
        course_name = input("Enter course name: ")
        print("Student registered for course successfully!")
    def calculate_gpa(self):
        for student in self.student_list:
            total_credits = 0
            total_points = 0
            for course in student.courses_registered:
                grade = student.grades[course.name]
                if grade is not None:
                    total_credits += course.credits
                    total_points += grade * course.credits
            if total_credits == 0:
                student.gpa = 0
            else:
                student.gpa = total_points / total_credits

    def calculate_ranking(self):
        self.student_list.sort(key=lambda s: s.gpa, reverse=True)
        print("\nRanking:")
        for i, student in enumerate(self.student_list):
            print(f"{i+1}. {student.email} - GPA: {student.gpa:.2f}")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum grade: "))
        max_grade = float(input("Enter maximum grade: "))
        filtered_students = [s for s in self.student_list if min_grade <= s.gpa <= max_grade]
        print("\nFiltered Students:")
        for student in filtered_students:
            print(f"{student.email} - GPA: {student.gpa:.2f}")
        return filtered_students
# Main program
def main():
    students = []
    courses = []

    while True:
        print("\n1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
        
            email = input("Enter student email: ")
            first_name = input("Enter student first name: ")
            last_name = input("Enter student last name: ")
            student = Student(email, first_name, last_name)
            students.append(student)
            print("Student added successfully!")

        elif choice == "2":
        
            name = input("Enter course name: ")
            trimester = input("Enter course trimester: ")
            credits = int(input("Enter course credits: "))
            course = Course(name, trimester, credits)
            courses.append(course)
            print("Course added successfully!")

        elif choice == "3":
        
            student_email = input("Enter student email: ")
            course_name = input("Enter course name: ")
            student = next((s for s in students if s.email == student_email), None)
            course = next((c for c in courses if c.name == course_name), None)
            if student and course:
                student.register_course(course)
                print("Student registered for course successfully!")
            else:
                print("Student or course not found!")

        elif choice == "4":
            # Calculate Ranking
            students.sort(key=lambda s: s.calculate_gpa(), reverse=True)
            print("\nRanking:")
            for i, student in enumerate(students):
                print(f"{i+1}. {student.email} - GPA: {student.calculate_gpa():.2f}")

        elif choice == "5":
            # Search by Grade
            min_grade = float(input("Enter minimum grade: "))
            max_grade = float(input("Enter maximum grade: "))
            filtered_students = [s for s in students if min_grade <= s.calculate_gpa() <= max_grade]
            print("\nFiltered Students:")
            for student in filtered_students:
                print(f"{student.email} - GPA: {student.calculate_gpa():.2f}")

        elif choice == "6":
            # Generate Transcript
            for student in students:
                print(f"\nTranscript for {student.email}:")
                for course in student.courses_registered:
                    grade = student.grades[course.name]
                    if grade is not None:
                        print(f"{course.name} - Grade: {grade:.2f} - Credits: {course.credits}")
                print(f"GPA: {student.calculate_gpa():.2f}")

        elif choice == "7":
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
