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
            manage_students()
        elif choice == "2":
            analyze_performance(school)
        elif choice == "3":
            visualize_data()
        elif choice == "4":
            print("Exiting program...")
            return
        else:
            print("Invalid choice. Please enter a valid option.")

def manage_students():
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
            count_dropout_students()
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

def visualize_data():
    while True:
        print("\n===== Visualize Data =====")
        print("1. Show Box and Whisker Plot of Scores")
        print("2. Show Pie Chart of Gender Distribution")
        print("3. Show Dot Plot of Student Ages")
        print("4. Show Subject Average Scores")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        choice = choice.strip()

        
        if choice == "1":
            show_whisker_plot_scores()
        elif choice == "2":
            show_pie_chart_gender()
        elif choice == "3":
            show_dot_plot_age()
        elif choice == "4":
            show_subject_average_scores()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Try again.")

# ===== STUDENT MANAGEMENT FUNCTIONS =====

def show_all_students():
    """Display the list of all students in the school"""
    pass

def add_student():
    """Add a new student to the school"""
    pass

def remove_student():
    """Remove a student from the school"""
    pass

def modify_student():
    """Modify an existing student's details"""
    pass

def find_student_by_id():
    """Find a student by their ID"""
    pass

def count_dropout_students():
    """Count the number of dropout students"""
    pass

# ===== PERFORMANCE ANALYSIS FUNCTIONS =====

def find_average_score_of_student(school):
    """Find and display the average score of a student"""
    student_input = input("Enter the student ID: ")
    student = school.find_student(int(student_input))
    if not student:
        print("Student not found")
        return 
    print(f"Average score of student ID: {student_input} is {student.get_average_score():.2f}")


def find_average_score_of_students_in_class(school):
    """Find and display the average score of students in a specific class"""
    student_class_input = input("Enter the class name: ")
    class_students = Analyzer.find_students_in_class(school.students, student_class_input)
    if not class_students:
        print("No students found in this class")
        return
    print(f"Average score of students in class {student_class_input} is {Analyzer.find_overall_average(class_students):.2f}")

def find_average_score_of_students_in_school(school):
    """Find and display the average score of all students in the school"""
    print(f"Average score of students in school is {Analyzer.find_overall_average(school.students):.2f}")
    
def find_high_and_low_performers(school):
    """Identify and display high and low-performing students"""
    while True:
        print("------------------------------------")
        print("Show High and Low performing students")
        print("------------------------------------")
        print("1. Show in a Specific Class")
        print("2. Show in a School")
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_to_show = input("Enter the class name: ")
            specific_class = Analyzer.find_students_in_class(school.students, class_to_show)
            student_to_show = int(input("Enter the number of students to show: "))
            top_perfomers = Analyzer.find_top_performers(specific_class, student_to_show)
            print("Top performers in class")
            for student in top_perfomers:
                student.show_info()
            
            low_perfomers = Analyzer.find_low_performers(specific_class, student_to_show)
            print("Low performers in class")
            for student in low_perfomers:
                student.show_info()
            return
        elif option.strip() == "2":
            student_to_show = int(input("Enter the number of students to show: "))
            top_perfomers = Analyzer.find_top_performers(school.students, student_to_show)
            print("Top performers in school")
            for student in top_perfomers:
                student.show_info()
            
            low_perfomers = Analyzer.find_low_performers(school.students, student_to_show)
            print("Low performers in school")
            for student in low_perfomers:
                student.show_info()
            return
        else: 
            print("Invalid choice. Try again.")
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

def show_dot_plot_age():
    """Show a dot plot of student ages in the school/class"""
    pass

def show_subject_average_scores():
    """Show the average scores for each subject in the school/class"""
    pass

if __name__ == "__main__":
    main_menu()
