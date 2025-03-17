import csv
import os
from utils import *
def main_menu():
    school = School(FileManager.load_file("DATA/student-scores.csv"))
    
    while True:
        print("\n===== Student Grade Analyzer =====")
        print("1. Manage Students")
        print("2. Analyze Performance")
        print("3. Visualize Data")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
        
        if choice == "1":
            manage_students(school)
        elif choice == "2":
            analyze_performance(school)
        elif choice == "3":
            visualize_data(school)
        elif choice == "4":
            print("Exiting program...")
            return
        else:
            print("Invalid choice. Please enter a valid option.")

def manage_students(school):
    while True:
        print("\n===== Manage Students =====")
        print("1. Show All Students")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. Modify Student")
        print("5. Find Student by ID")
        print("6. Count Dropout Students")
        print("7. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
        
        if choice == "1":
            show_all_students()
        elif choice == "2":
            add_student()
        elif choice == "3":
            remove_student()
        elif choice == "4":
            modify_student()
        elif choice == "5":
            find_student_by_id()
        elif choice == "6":
            count_dropout_students(school)
        elif choice == "7":
            return
        else:
            print("Invalid choice. Try again.")

def analyze_performance(school):
    while True:
        print("\n===== Analyze Performance =====")
        print("1. Find Average Score of Student")
        print("2. Find Average Score of Students in Class")
        print("3. Find Average Score of Students in School")
        print("4. Identify Outstanding and Low Performing Students")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
        
        if choice == "1":
            find_average_score_of_student(school)
        elif choice == "2":
            find_average_score_of_students_in_class(school)
        elif choice == "3":
            find_average_score_of_students_in_school(school)
        elif choice == "4":
            find_high_and_low_performers(school)
        elif choice == "5":
            return
        else:
            print("Invalid choice. Try again.")

def visualize_data(school):
    while True:
        print("\n===== Visualize Data =====")
        print("1. Show Box and Whisker Plot of Scores")
        print("2. Show Pie Chart of Gender Distribution")
        print("3. Show Scatter Plot of Student Ages")
        print("4. Show Subject Average Scores")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
   
        if choice == "1":
            show_whisker_plot_scores()
        elif choice == "2":
            show_pie_chart_gender()
        elif choice == "3":
            show_scatter_plot_age()
        elif choice == "4":
            show_subject_average_scores(school)
        elif choice == "5":
            return
        else:
            print("Invalid choice. Try again.")

# ===== STUDENT MANAGEMENT FUNCTIONS =====

def show_all_students():
    """Display the list of all students in the school"""
    students = FileManager.load_file("DATA/student-scores.csv")
    if not students:
        print("No student data available.")
        return
    print("    ID | First Name            | Last Name             | Gender  | Dropout | Absences | Age | Class")
    print("--------------------------------------------------------------------------------------------------------------")
    for student in students:
        print(f"{student.student_id:5} | {student.first_name:20} | {student.last_name:20} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:10}")

def add_student():
    """Add a new student to the school"""
    while True:
        try:
            student_id = int(input("Enter Student ID: "))
            
            first_name = input("Enter First Name: ").strip()
            while not first_name.isalpha():
                print("Invalid input! First name can only contain letters.")
                first_name = input("Enter First Name: ").strip()

            last_name = input("Enter Last Name: ").strip()
            while not last_name.isalpha():
                print("Invalid input! Last name can only contain letters.")
                last_name = input("Enter Last Name: ").strip()

            gender = input("Enter Gender (male/female): ").strip().lower()
            while gender not in ("male", "female"):
                print("Invalid input! Gender must be 'male' or 'female'.")
                gender = input("Enter Gender (male/female): ").strip().lower()

            is_dropout_input = input("Is the student a dropout? (yes/no): ").strip().lower()
            while is_dropout_input not in ("yes", "no"):
                print("Invalid input! Please enter 'yes' or 'no'.")
                is_dropout_input = input("Is the student a dropout? (yes/no): ").strip().lower()
            is_dropout = is_dropout_input == "yes"

            while True:
                try:
                    absences = int(input("Enter number of absences: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for absences.")

            while True:
                try:
                    age = int(input("Enter age: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a number for age.")

            student_class = input("Enter class name: ").strip()
            while not student_class.isalpha():
                print("Invalid input! Class name can only contain letters.")
                student_class = input("Enter class name: ").strip()

            scores = {}
            score_names = ["math_score", "history_score", "physics_score", "chemistry_score", "biology_score", "english_score", "geography_score"]
            for score_name in score_names:
                while True:
                    try:
                        scores[score_name] = float(input(f"Enter {score_name.replace('_', ' ').capitalize()}: "))
                        break
                    except ValueError:
                        print(f"Invalid input. Please enter a number for {score_name.replace('_', ' ').capitalize()}.")

            new_student = Student(student_id, first_name, last_name, gender, is_dropout, absences, age, student_class, **scores)
            FileManager.append_to_file("DATA/student-scores.csv", new_student)
            print("Student added successfully!")
            break  # Exit the loop if successful
        except ValueError:
            print("Invalid input! Please enter correct values.")

def remove_student():
    """Remove a student from the school"""
    while True:
        try:
            students = FileManager.load_file("DATA/student-scores.csv")
            student_id = int(input("Enter Student ID to remove: "))

            updated_students = [student for student in students if student.student_id != student_id]

            if len(updated_students) == len(students):
                print("Student not found!")
                return

            FileManager.save_file("DATA/student-scores.csv", updated_students)
            print("Student removed successfully!")
            break
        except ValueError:
            print("Invalid Student ID input. Please enter a valid number.")

def modify_student():
    """Modify an existing student's details"""
    while True:
        try:
            students = FileManager.load_file("DATA/student-scores.csv")
            student_id = int(input("Enter Student ID to modify: "))

            for student in students:
                if student.student_id == student_id:
                    new_first_name = input(f"Enter new First Name ({student.first_name}): ").strip()
                    while new_first_name and not new_first_name.isalpha():
                        print("Invalid input! First name can only contain letters.")
                        new_first_name = input(f"Enter new First Name ({student.first_name}): ").strip()
                    student.first_name = new_first_name or student.first_name

                    new_last_name = input(f"Enter new Last Name ({student.last_name}): ").strip()
                    while new_last_name and not new_last_name.isalpha():
                        print("Invalid input! Last name can only contain letters.")
                        new_last_name = input(f"Enter new Last Name ({student.last_name}): ").strip()
                    student.last_name = new_last_name or student.last_name

                    new_gender = input(f"Enter new Gender ({student.gender}): ").strip().lower()
                    while new_gender and new_gender not in ("male", "female"):
                        print("Invalid input! Gender must be 'male' or 'female'.")
                        new_gender = input(f"Enter new Gender ({student.gender}): ").strip().lower()
                    student.gender = new_gender or student.gender

                    student_class = input(f"Enter new Class ({student.student_class}): ").strip()
                    while student_class and not student_class.isalpha():
                        print("Invalid input! Class name can only contain letters.")
                        student_class = input(f"Enter new Class ({student.student_class}): ").strip()
                    student.student_class = student_class or student.student_class

                    FileManager.save_file("DATA/student-scores.csv", students)
                    print("Student details updated successfully!")
                    return

            print("Student not found!")
        except ValueError:
            print("Invalid Student ID or other input. Please enter valid values.")

def find_student_by_id():
    """Find a student by their ID"""
    while True:
        try:
            students = FileManager.load_file("DATA/student-scores.csv")
            student_id = int(input("Enter Student ID: "))

            for student in students:
                if student.student_id == student_id:
                    print("Student found:")
                    print(f"ID: {student.student_id}, Name: {student.first_name} {student.last_name}, Class: {student.student_class}, Average Score: {student.get_average_score():.2f}")
                    return
            print("Student not found!")
        except ValueError:
            print("Invalid Student ID input. Please enter a valid number.")             
# ===== PERFORMANCE ANALYSIS FUNCTIONS =====

def find_average_score_of_student(school):
    """Find and display the average score of a student"""
    student_input = input("Enter the student ID: ")     # Let user to enter the student ID
    student = school.find_student(int(student_input))   # find the student by ID
    if not student:
        print("Student not found")      # Print a message if the student doesn't found
        return 
    print(f"Average score of student ID: {student_input} is {student.get_average_score():.2f}")
    # Print the average score of the student

def find_average_score_of_students_in_class(school):
    """Find and display the average score of students in a specific class"""
    student_class_input = input("Enter the class name: ")   # Let user to enter the class name
    class_students = Analyzer.find_students_in_class(school.students, student_class_input)     # Find the students in the specified class
    if not class_students:
        print("No students found in this class")    # Print a message if no students are found in the class
        return
    print(f"Average score of students in class {student_class_input} is {Analyzer.find_overall_average(class_students):.2f}")
    # Print the average score of students in the class
    
def find_average_score_of_students_in_school(school):
    """Find and display the average score of all students in the school"""
    print(f"Average score of students in school is {Analyzer.find_overall_average(school.students):.2f}")
    # Print the average score of all students in the school
    
def find_high_and_low_performers(school):
    """Identify and display high and low-performing students"""
    while True:
        print("------------------------------------")
        print("Show High and Low performing students")
        print("------------------------------------")
        print("1. Show in a Specific Class")
        print("2. Show in a School")
        option = input("Enter your choice: ")   # Ask user to choose specific class or school
        if option.strip() == "1":
            class_to_show = input("Enter the class name: ")     # Ask the user to enter the class name
            specific_class = Analyzer.find_students_in_class(school.students, class_to_show)    # Find students in the specified class
            student_to_show = int(input("Enter the number of students to show: "))  # Ask the user to enter the number of students to show
            top_perfomers = Analyzer.find_top_performers(specific_class, student_to_show)   # Find top performers in the class
            print("Top performers in class")
            for student in top_perfomers:
                student.show_info()     # Display information of top performers
            
            low_perfomers = Analyzer.find_low_performers(specific_class, student_to_show)   # Find low performers in the class
            print("Low performers in class")
            for student in low_perfomers:
                student.show_info()     # Display information of low performers
            return
        
        elif option.strip() == "2":
            student_to_show = int(input("Enter the number of students to show: "))      # Ask the user to enter the number of students to show
            top_perfomers = Analyzer.find_top_performers(school.students, student_to_show)  # Find top performers in the school
            print("Top performers in school")
            for student in top_perfomers:
                student.show_info()     # Display information of top performers
            
            low_perfomers = Analyzer.find_low_performers(school.students, student_to_show)  # Find low performers in the school
            print("Low performers in school")
            for student in low_perfomers:
                student.show_info()     # Display information if low performers
            return
        else: 
            print("Invalid choice. Try again.")     # Print a message if the choice is invalid
    return


# ===== DATA VISUALIZATION FUNCTIONS =====

def show_whisker_plot_scores():
    """Show a whisker plot (boxplot) of student scores in each class or a class"""
    while True:
        print("------------------------------------")
        print("Show Box and Whisker Plot of Scores")
        print("------------------------------------")
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_to_show = input("Enter the class name: ")
            print("Plotting...")
            Visuallize.show_whisker_plot_avg_scores(Analyzer.find_students_in_class(FileManager.load_file("DATA\student-scores.csv"), class_to_show))
            return
        elif option.strip() == "2":
            print("Plotting...")
            Visuallize.show_whisker_plot_avg_scores(FileManager.load_file("DATA\student-scores.csv"))
            return
        else:
            print("Invalid choice. Try again.")
            return
        
def show_pie_chart_gender():
    """Show a pie chart of the gender distribution in the school/class"""
    while True:
        print("------------------------------------")
        print("Show Pie Chart of Genders")
        print("------------------------------------")
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_to_show = input("Enter the class name: ")
            print("Plotting...")
            Visuallize.show_pie_chart_gender(Analyzer.find_students_in_class(FileManager.load_file("DATA\student-scores.csv"), class_to_show))
            return
        elif option.strip() == "2":
            print("Plotting...")
            Visuallize.show_pie_chart_gender(FileManager.load_file("DATA\student-scores.csv"))
            return
        else:
            print("Invalid choice. Try again.")
            return

def show_scatter_plot_age():
    """Show a scatter plot of student ages in the school/class"""
    while True:
        print("------------------------------------")
        print("Show Scatter Plot of Age")
        print("------------------------------------")
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_to_show = input("Enter the class name: ")
            print("Plotting...")
            Visuallize.show_scatter_plot_age(Analyzer.find_students_in_class(FileManager.load_file("DATA\student-scores.csv"), class_to_show))
            return
        elif option.strip() == "2":
            print("Plotting...")
            Visuallize.show_scatter_plot_age(FileManager.load_file("DATA\student-scores.csv"))
            return
        else:
            print("Invalid choice. Try again.")
            return

def show_subject_average_scores(school):
    """Show the average scores for each subject in the school (Compare Each Class based on Subject)"""
    print("------------------------------------")
    print("Show Scatter Plot of Age")
    print("------------------------------------")
    print("Plotting...")
    
    Visuallize.show_subject_averages_bar_chart(school)

if __name__ == "__main__":
    main_menu()
