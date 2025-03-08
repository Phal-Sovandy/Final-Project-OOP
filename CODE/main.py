from utils import *
def main_menu(): 
    while True:
        print("\n===== Student Grade Analyzer =====")
        print("1. Manage Students")
        print("2. Analyze Performance")
        print("3. Visualize Data")
        print("4. Exit")
        print("===============================")
        
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manage_students()
        elif choice == "2":
            analyze_performance()
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

def analyze_performance():
    while True:
        print("\n===== Analyze Performance =====")
        print("1. Find Average Score of Student")
        print("2. Find Average Score of Students in Class")
        print("3. Find Average Score of Students in School")
        print("4. Identify Outstanding and Low Performing Students")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            find_average_score_of_student()
        elif choice == "2":
            find_average_score_of_students_in_class()
        elif choice == "3":
            find_average_score_of_students_in_school()
        elif choice == "4":
            find_high_and_low_performers()
        elif choice == "5":
            return
        else:
            print("Invalid choice. Try again.")

def visualize_data():
    while True:
        print("\n===== Visualize Data =====")
        print("1. Show Whisker Plot of Scores in Each Class")
        print("2. Show Pie Chart of Gender Distribution")
        print("3. Show Dot Plot of Student Ages")
        print("4. Show Subject Average Scores")
        print("5. Back to Main Menu")
        
        choice = input("Enter your choice: ")
        
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

def find_average_score_of_student():
    """Find and display the average score of a student"""
    pass

def find_average_score_of_students_in_class():
    """Find and display the average score of students in a specific class"""
    pass

def find_average_score_of_students_in_school():
    """Find and display the average score of all students in the school"""
    pass

def find_high_and_low_performers():
    """Identify and display high and low-performing students"""
    pass

# ===== DATA VISUALIZATION FUNCTIONS =====

def show_whisker_plot_scores():
    """Show a whisker plot (boxplot) of student scores in each class"""
    pass

def show_pie_chart_gender():
    """Show a pie chart of the gender distribution in the school/class"""
    pass

def show_dot_plot_age():
    """Show a dot plot of student ages in the school/class"""
    pass

def show_subject_average_scores():
    """Show the average scores for each subject in the school/class"""
    pass

if __name__ == "__main__":
    main_menu()
