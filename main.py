from src.models import *
from src.utils import *

DATA_BASE_PATH = "data/student-scores.csv"

def main_menu():
    """Welcome and main menu"""
    print("\n" + "=" * 70)
    print(f"{"📚 STUDENT GRADE ANALYZER 📊":^70}")
    print("=" * 70)
    print("\n🎉 Welcome to the Student Grade Analyzer! 🎉")
    print("🔹 Manage, analyze, and gain insightful data of students' performance.")
    print("🔹 Easily add, remove, modify, and remove student records.")
    print("🔹 Get statistic summaries and analyzed reports.\n")
    print("=" * 70 + "\n")
    
    while True:        
        print("\n" + "=" * 29 + " MAIN MENU " + "=" * 30)
        print("1. Manage Students")
        print("2. Analyze Performance")
        print("3. Visualizer Data")
        print("4. Exit")
        print("-" * 70)
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
        
        if choice == "1":
            manage_students()
        elif choice == "2":
            analyze_performance()
        elif choice == "3":
            visualizer_data()
        elif choice == "4":
            print("Exiting program...")
            return
        else:
            print("❌ Invalid choice. Please enter a valid option.")
def manage_students():
    """Manage student data menu"""
    while True:        
        print("\n" + "=" * 26 + " MANAGE STUDENTS " + "=" * 27)
        print("1. Show All Students")
        print("2. Add Student")
        print("3. Remove Student")
        print("4. Modify Student")
        print("5. Find Student by ID")
        print("6. Count Dropout Students")
        print("7. Back to Main Menu")
        print("-" * 70)
        
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
            print("❌ Invalid choice. Try again.")
def analyze_performance():
    """Analyze data menu"""
    while True:        
        print("\n" + "=" * 25 + " ANALYZE PERFORMANCE " + "=" * 24)
        print("1. Find Alphabetical Grade and GPA of a Student")
        print("2. Find Average Score of Students in Class")
        print("3. Find Average Score of Students in School")
        print("4. Identify Outstanding and Low Performing Students")
        print("5. Find Below Average Students")
        print("6. Summary Report")
        print("7. Back to Main Menu")
        print("-" * 70) 
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
        
        if choice == "1":
            find_grade_of_student()
        elif choice == "2":
            find_average_score_of_students_in_class()
        elif choice == "3":
            find_average_score_of_students_in_school()
        elif choice == "4":
            find_high_and_low_performers()
        elif choice == "5":
            find_below_avg_student()
        elif choice == "6":
            summary_report()
        elif choice == "7":
            return
        else:
            print("❌ Invalid choice. Try again.")
def visualizer_data():
    """Visualize plot/chart menu"""
    while True:       
        print("\n" + "=" * 27 + " VISUALIZE DATA " + "=" * 26)
        print("1. Show Box and Whisker Plot of Scores")
        print("2. Show Pie Chart of Gender Distribution")
        print("3. Show Bar Chart of Student Count Distribution")
        print("4. Show Scatter Plot of Student Ages")
        print("5. Show Subject Average Scores")
        print("6. Back to Main Menu")
        print("-" * 70)
        
        choice = input("Enter your choice: ")
        choice = choice.strip()
   
        if choice == "1":
            show_whisker_plot_scores()
        elif choice == "2":
            show_pie_chart_gender()
        elif choice == "3":
            show_student_count()
        elif choice == "4":
            show_scatter_plot_age()
        elif choice == "5":
            show_subject_average_scores()
        elif choice == "6":
            return
        else:
            print("❌ Invalid choice. Try again.")

# ===== STUDENT MANAGEMENT FUNCTIONS =====

def show_all_students():
    """Display the list of all students in the school"""
    while True:
        print()
        print("-" * 70)
        print("Show List of Students")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        print("-" * 70)
        
        try:
            school = School(FileManager.load_file(DATA_BASE_PATH))
        except Exception as e:
            print(f"⚠️ Error: {e}")
                
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            class_to_show = input("Enter the class name: ")
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class(FileManager.load_file(DATA_BASE_PATH), class_to_show))
            except Exception as e:
                print(f"⚠️ Error: {e}")
            
            print("-" * 112)
            print(f"{"Student in Class " + f"{class_to_show.upper()}":^122}")
            print("-" * 112)
            if not classroom.students:
                print("No student student in class.")
                return
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in classroom.students:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            print("-" * 112)
            print(f"Total Number of Students: {classroom.count_students}")
            print("-" * 112)
            break
        elif option.strip() == "2":
            print("-" * 112)
            print(f"{"Student in School":^122}")
            print("-" * 112)
            if not school.students:
                print("No student student in school.")
                return
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in school.students:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            print("-" * 112)
            print(f"Total Number of Students: {school.count_students}")
            print("-" * 112)
            break
        else:
            print("❌ Invalid choice. Try again.")     # Print a message if the choice is invalid
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def add_student():
    """Add a new student to the school"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
        student_id = len(school.students) + 1
        
        first_name = input("Enter First Name: ").strip()
        while not first_name.isalpha():
            print("❌ Invalid input! First name can only contain letters.")
            first_name = input("Enter First Name: ").strip()

        last_name = input("Enter Last Name: ").strip()
        while not last_name.isalpha():
            print("❌ Invalid input! Last name can only contain letters.")
            last_name = input("Enter Last Name: ").strip()

        gender = input("Enter Gender (male/female): ").strip().lower()
        while gender not in ("male", "female"):
            print("❌ Invalid input! Gender must be 'male' or 'female'.")
            gender = input("Enter Gender (male/female): ").strip().lower()

        is_dropout_input = input("Is the student a dropout? (yes/no): ").strip().lower()
        while is_dropout_input not in ("yes", "no"):
            print("❌ Invalid input! Please enter 'yes' or 'no'.")
            is_dropout_input = input("Is the student a dropout? (yes/no): ").strip().lower()
        is_dropout = is_dropout_input == "yes"

        while True:
            try:
                absences = int(input("Enter number of absences: "))
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number for absences.")

        while True:
            try:
                age = int(input("Enter age: "))
                break
            except ValueError:
                print("❌ Invalid input. Please enter a number for age.")
        
        class_list = school.classes_list
        # Display existed classes name, but user can add other class name too
        print("-" * 70)
        print(f"{"Classes Name in School":^70}")
        print("-" * 70)
        for class_name in class_list:
            print(class_name)
        print("-" * 70)
        student_class = input("Enter class name: ").strip()
        while not all(char.isalpha() or char.isspace() for char in student_class):
            print("❌ Invalid input! Class name can only contain letters.")
            student_class = input("Enter class name: ").strip()

        scores = {}
        score_names = ["math_score", "history_score", "physics_score", "chemistry_score", "biology_score", "english_score", "geography_score"]
        for score_name in score_names:
            while True:
                try:
                    scores[score_name] = float(input(f"Enter {score_name.replace('_', ' ').capitalize()}: "))
                    break
                except ValueError:
                    print(f"❌ Invalid input. Please enter a number for {score_name.replace('_', ' ').capitalize()}.")

        new_student = Student(student_id, first_name.capitalize(), last_name.capitalize(), gender, is_dropout, absences, age, student_class.capitalize(), **scores)
        FileManager.append_to_file(DATA_BASE_PATH, new_student)
        print("✅ Student added successfully!")
        print("-" * 112)
        print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
        print("-" * 112)
        print(f"{new_student.student_id:04} | {new_student.first_name:12} | {new_student.last_name:12} | {new_student.gender:7} | {new_student.is_dropout:7} | {new_student.absences:8} | {new_student.age:3} | {new_student.student_class:21} | {new_student.get_average_score():10.2f}")
        return
    except ValueError:
        print("❌ Invalid input! Please enter correct values.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    return
def modify_student():
    """Modify an existing student's details"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
        while True:
            student_id = input("Enter the student ID to modify: ")     # Let user to enter the student ID
            if student_id.isdigit():
                student_id = int(student_id)
                break
            print("❌ Invalid input. Please enter a numeric ID.")

        for student in school.students:
            if student.student_id == student_id:
                new_first_name = input(f"Enter new First Name ({student.first_name}): ").strip()
                while new_first_name and not new_first_name.isalpha():
                    print("❌ Invalid input! First name can only contain letters.")
                    new_first_name = input(f"Enter new First Name ({student.first_name}): ").strip()
                student.first_name = new_first_name or student.first_name

                new_last_name = input(f"Enter new Last Name ({student.last_name}): ").strip()
                while new_last_name and not new_last_name.isalpha():
                    print("❌ Invalid input! Last name can only contain letters.")
                    new_last_name = input(f"Enter new Last Name ({student.last_name}): ").strip()
                student.last_name = new_last_name or student.last_name

                new_gender = input(f"Enter new Gender ({student.gender}): ").strip().lower()
                while new_gender and new_gender not in ("male", "female"):
                    print("❌ Invalid input! Gender must be 'male' or 'female'.")
                    new_gender = input(f"Enter new Gender ({student.gender}): ").strip().lower()
                student.gender = new_gender or student.gender

                class_list = school.classes_list
                # Display existed classes name, but user can add other class name too
                print("-" * 70)
                print(f"{"Classes Name in School":^70}")
                print("-" * 70)
                for class_name in class_list:
                    print(class_name)
                print("-" * 70)
                student_class = input(f"Enter new Class ({student.student_class}): ").strip()
                while not all(char.isalpha() or char.isspace() for char in student_class):
                    print("❌ Invalid input! Class name can only contain letters and spaces.")
                    student_class = input("Enter class name: ").strip()
                student.student_class = student_class or student.student_class

                FileManager.save_file(DATA_BASE_PATH, school.students)
                print("✅ Student details updated successfully!")
                print("-" * 112)
                print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
                print("-" * 112)
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")  
                return
        print("🔍 Student not found!")
        return
    except Exception as e:
        print(f"⚠️ Error: {e}")
        return
def remove_student():
    """Remove a student from the school"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
        while True:
                student_id = input("Enter the student ID to remove: ")     # Let user to enter the student ID
                if student_id.isdigit():
                    student_id = int(student_id)
                    break
                print("❌ Invalid input. Please enter a numeric ID.")

        updated_students = [student for student in school.students if student.student_id != student_id]

        if len(updated_students) == len(school.students):
            print("🔍 Student not found!")
            return
        FileManager.save_file(DATA_BASE_PATH, updated_students)
        print("✅ Student removed successfully!")
    except ValueError:
        print("❌ Invalid Student ID input. Please enter a valid number.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
def count_dropout_students():
    """Count the number of dropout students"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    dropout_count = 0
    while True:
        print()
        print("-" * 70)
        print("Count Dropout Students")
        print("-" * 70)
        print("1. Count in a Specific Class")
        print("2. Count All Classes")
        print("-" * 70)
        
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            # Display existed classes name, but user can add other class name too
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            class_to_show = input("Enter the class name: ")
            
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class((FileManager.load_file(DATA_BASE_PATH)), class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            dropout_count = sum(1 for student in classroom.students if student.is_dropout)
            break
        elif option.strip() == "2":
            try:
                school = School(FileManager.load_file(DATA_BASE_PATH))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            dropout_count = sum(1 for student in school.students if student.is_dropout)
            break
        else:
            print("❌ Invalid choice. Try again.")
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
    print(f"Total dropout students: {dropout_count}")
def find_student_by_id():
    """Find a student by their ID"""
    while True:
        try:
            school = School(FileManager.load_file(DATA_BASE_PATH))
            while True:
                student_id = input("Enter the student ID: ")     # Let user to enter the student ID
                if student_id.isdigit():
                    student_id = int(student_id)
                    break
                print("❌ Invalid input. Please enter a numeric ID.")

            student = school.find_student(student_id)
            if student:
                    print("Student found:")
                    print("-" * 112)
                    print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
                    print("-" * 112)
                    print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
                    return
            print("🔍 Student not found!")
            continueing = input("Would you like to continue?(y/*): ")
            if continueing.lower != 'y':
                return
        except ValueError:
            print("❌ Invalid Student ID input. Please enter a valid number.")
        except Exception as e:
            print(f"⚠️ Error: {e}")
        continueing = input("Would you like to try again?(y/*): ")
        if continueing.lower().strip() != 'y':
            return

# ===== PERFORMANCE ANALYSIS FUNCTIONS =====
#Should find details of student with this one with GPA, Percentage,...
def find_grade_of_student():
    """Find and display the average score of a student"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    while True:
        student_id = input("Enter the student ID: ")     # Let user to enter the student ID
        if student_id.isdigit():
            student_id = int(student_id)
            break
        print("❌ Invalid input. Please enter a numeric ID.")

    try:
        student = school.find_student(int(student_id))   # find the student by ID
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    if not student:
        print("🔍 Student not found!")      # Print a message if the student doesn't found
        return
    
    if student.get_alpha_grade_gpa():
        print("-" * 127)
        print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score   | Grade | GPA")
        print("-" * 127)
        print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():15.2f} | {student.get_alpha_grade_gpa()[0]:5} | {student.get_alpha_grade_gpa()[1]:.1f}")
        return
    print("⚠️ Student does NOT have Grade!")
    return 
def find_average_score_of_students_in_class():
    """Find and display the average score of students in a specific class"""
    school = School(FileManager.load_file(DATA_BASE_PATH))
    class_list = school.classes_list
    # Display existed classes name, but user can add other class name too
    print("-" * 70)
    print(f"{"Classes Name in School":^70}")
    print("-" * 70)
    for class_name in class_list:
        print(class_name)
    print("-" * 70)
    student_class_input = input("Enter the class name: ")   # Let user to enter the class name
    try:
        classroom = Classroom(student_class_input, Analyzer.find_students_in_class(school.students, student_class_input))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    if not classroom.students:
        print("🔍 No students found in this class")    # Print a message if no students are found in the class
        return
    print(f"Average score of students in class {student_class_input} is {Analyzer.find_overall_average(classroom.students):.2f}")
    # Print the average score of students in the class 
def find_average_score_of_students_in_school():
    """Find and display the average score of all students in the school"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    if not school.students:
        print("🔍 No students found in this school")    # Print a message if no students are found in the school
        return
    print(f"Average score of students in school is {Analyzer.find_overall_average(school.students):.2f}")
    # Print the average score of all students in the school     
def find_high_and_low_performers():
    """Identify and display high and low-performing students"""    
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    while True:
        print()
        print("-" * 70)
        print("Show High and Low performing students")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show in a School")
        print("-" * 70)
        
        option = input("Enter your choice: ")   # Ask user to choose specific class or school
            
        if option.strip() == "1":
            
            class_list = school.classes_list
            # Display existed classes name
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            
            while True:
                class_to_show = input("Enter the class name: ")     # Ask the user to enter the class name
                if class_to_show in class_list:
                    break
                print("❌ Invalid input. Please enter a valid class name.")
                continueing = input("Would you like to try again?(y/*): ")
                if continueing.lower().strip() != 'y':
                    return
                
            try:
                specific_class = Classroom(class_to_show, Analyzer.find_students_in_class(school.students, class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            
            while True:
                student_to_show = input("Enter the number of students to show: ")  # Ask the user to enter the number of students to show
                if student_to_show.isdigit():
                    student_to_show = int(student_to_show)
                    break
                print("❌ Invalid input. Please enter a valid number.")
                
            top_perfomers_in_class = Analyzer.find_top_performers(specific_class.students, student_to_show)   # Find top performers in the class
            print("-" * 112)
            print(f"{"Top Performing Students":^112}")
            print("-" * 112 + "\n")
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in top_perfomers_in_class:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            # Display information of top performers in class

            low_perfomers_in_class = Analyzer.find_low_performers(specific_class.students, student_to_show)   # Find low performers in the class
            print("\n" + "-" * 112)
            print(f"{"Low Performing Students":^112}")
            print("-" * 112 + "\n")
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in low_perfomers_in_class:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            # Display information of low performers in class  
            break      
        elif option.strip() == "2":
            while True:
                student_to_show = input("Enter the number of students to show: ")   # Ask the user to enter the number of students to show
                if student_to_show.isdigit():
                    student_to_show = int(student_to_show)
                    break
                print("❌ Invalid input. Please enter a valid number.")
                
            top_perfomers_in_school = Analyzer.find_top_performers(school.students, student_to_show)  # Find top performers in the school
            print("-" * 112)
            print(f"{"Top Performing Students":^112}")
            print("-" * 112 + "\n")
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in top_perfomers_in_school:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            # Display information of top performers in school
            
            low_perfomers_in_school = Analyzer.find_low_performers(school.students, student_to_show)  # Find low performers in the school
            print("\n" + "-" * 112)
            print(f"{"Low Performing Students":^112}")
            print("-" * 112 + "\n")
            print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
            print("-" * 112)
            for student in low_perfomers_in_school:
                print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
            # Display information of top performers in school   
            break       
        else:
            print("❌ Invalid choice. Try again.")     # Print a message if the choice is invalid
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def find_below_avg_student():
    """List all students that scored below average score among all students (class or school)"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    while True:
        print()
        print("-" * 70)
        print("Show Below Average Students")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show in a School")
        print("-" * 70)
        
        option = input("Enter your choice: ")   # Ask user to choose specific class or school
            
        if option.strip() == "1":
            
            class_list = school.classes_list
            # Display existed classes name
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            
            while True:
                class_to_show = input("Enter the class name: ")     # Ask the user to enter the class name
                if class_to_show in class_list:
                    break
                print("❌ Invalid input. Please enter a valid class name.")
                continueing = input("Would you like to try again?(y/*): ")
                if continueing.lower().strip() != 'y':
                    return
                
            try:
                specific_class = Classroom(class_to_show, Analyzer.find_students_in_class(school.students, class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            below_avg_students = Analyzer.find_failing_students(specific_class.students)
            if below_avg_students:
                print("-" * 112)
                print(f"{("Below Average Students in Class: " + f"{class_to_show.capitalize()}"):^112}")
                print("-" * 112 + "\n")
                print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
                print("-" * 112)
                for student in below_avg_students:
                    print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
                print("-" * 112)
                print(f"Number of Below Average Students: {len(below_avg_students)}")
                print("-" * 112)
                return
            print("🔍 There is NO Below Average students")
            break
        elif option.strip() == "2":
            below_avg_students = Analyzer.find_failing_students(school.students)
            if below_avg_students:
                print("-" * 112)
                print(f"{"Below Average Students in School":^112}")
                print("-" * 112 + "\n")
                print(" ID  | First Name   | Last Name    | Gender  | Dropout | Absences | Age | Class                 | Average Score")
                print("-" * 112)
                for student in below_avg_students:
                    print(f"{student.student_id:04} | {student.first_name:12} | {student.last_name:12} | {student.gender:7} | {student.is_dropout:7} | {student.absences:8} | {student.age:3} | {student.student_class:21} | {student.get_average_score():10.2f}")
                print("-" * 112)
                print(f"Number of Below Average Students: {len(below_avg_students)}")
                print("-" * 112)
                return
            print("🔍 There is NO Below Average students")
            break
        else:
            print("❌ Invalid choice. Try again.")     # Print a message if the choice is invalid
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def summary_report():
    """Print Summary Report of Student/Class/School"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
    
    while True:
        print()
        print("-" * 70)
        print("Show Summary Report of Student/Classroom/School")
        print("-" * 70)
        print("1. Show of a Student")
        print("2. Show in a Specific Class")
        print("3. Show in a School")
        print("-" * 70)
        
        option = input("Enter your choice: ")   # Ask user to choose student, specific class or school
            
        if option.strip() == "1":
            while True:
                student_id = input("Enter the student ID: ")     # Let user to enter the student ID
                if student_id.isdigit():
                    student_id = int(student_id)
                    break
                print("❌ Invalid input. Please enter a numeric ID.")

            try:
                student = school.find_student(int(student_id))   # find the student by ID
            except Exception as e:
                print(f"⚠️ Error: {e}")
            if not student:
                print("🔍 Student not found")      # Print a message if the student doesn't found
                return
            
            student.show_info()
            break
        elif option.strip() == "2":
            class_list = school.classes_list
            # Display existed classes name
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            
            while True:
                class_to_show = input("Enter the class name: ")     # Ask the user to enter the class name
                if class_to_show in class_list:
                    break
                print("❌ Invalid input. Please enter a valid class name.")
                continueing = input("Would you like to try again?(y/*): ")
                if continueing.lower().strip() != 'y':
                    return
                
                
            try:
                specific_class = Classroom(class_to_show, Analyzer.find_students_in_class(school.students, class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            
            specific_class.display_info()
            break  
        elif option.strip() == "3":
            school.display_info()
            break
        else:
            print("❌ Invalid choice. Try again.")     # Print a message if the choice is invalid
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
      
# ===== DATA VISUALIZATION FUNCTIONS =====

def show_whisker_plot_scores():
    """Show a whisker plot (boxplot) of student scores in each class or a class"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    while True:
    
        print()
        print("-" * 70)
        print("Show Box and Whisker Plot of Scores")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        print("-" * 70)
        
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            # Display existed classes name, but user can add other class name too
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            class_to_show = input("Enter the class name: ")
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class(school.students, class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            print("Plotting...📊")
            Visualizer.show_whisker_plot_avg_scores(classroom.students)
            break
        elif option.strip() == "2":
            print("Plotting...📊")
            Visualizer.show_whisker_plot_avg_scores(school.students)
            break
        else:
            print("❌ Invalid choice. Try again.")
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def show_pie_chart_gender():
    """Show a pie chart of the gender distribution in the school/class"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    while True:
        print()
        print("-" * 70)
        print("Show Pie Chart of Genders")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        print("-" * 70)
        
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            # Display existed classes name, but user can add other class name too
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            
            class_to_show = input("Enter the class name: ")
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class((FileManager.load_file(DATA_BASE_PATH)), class_to_show))
            except ValueError:
                print(f"⚠️ Error: {ValueError}")
            except Exception as e:
                print(f"⚠️ Error: {e}")
            print("Plotting...📊")
            Visualizer.show_pie_chart_gender(classroom.students)
            break
        elif option.strip() == "2":
            print("Plotting...📊")
            Visualizer.show_pie_chart_gender(school.students)
            break
        else:
            print("❌ Invalid choice. Try again.")
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def show_student_count():
    """Show number of student across class or school"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    while True:
        print()
        print("-" * 70)
        print("Show Number of Students")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        print("-" * 70)
        
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            # Display existed classes name, but user can add other class name too
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            class_to_show = input("Enter the class name: ")
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class(FileManager.load_file(DATA_BASE_PATH), class_to_show))
            except Exception as e:
                print(f"⚠️ Error: {e}")
            print("Plotting...📊")
            Visualizer.show_number_students(classroom.students)
            break
        elif option.strip() == "2":
            print("Plotting...📊")
            Visualizer.show_number_students(school.students)
            break
        else:
            print("❌ Invalid choice. Try again.")
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def show_scatter_plot_age():
    """Show a scatter plot of student ages in the school/class"""
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except Exception as e:
        print(f"⚠️ Error: {e}")
        
    while True:
        print()
        print("-" * 70)
        print("Show Scatter Plot of Age")
        print("-" * 70)
        print("1. Show in a Specific Class")
        print("2. Show All Classes")
        print("-" * 70)
        
        option = input("Enter your choice: ")
        if option.strip() == "1":
            class_list = school.classes_list
            # Display existed classes name, but user can add other class name too
            print("-" * 70)
            print(f"{"Classes Name in School":^70}")
            print("-" * 70)
            for class_name in class_list:
                print(class_name)
            print("-" * 70)
            class_to_show = input("Enter the class name: ")
            try:
                classroom = Classroom(class_to_show, Analyzer.find_students_in_class(FileManager.load_file(DATA_BASE_PATH), class_to_show))
            except Exception as e:
                print(f"⚠️ Error: {e}")
            print("Plotting...📊")
            Visualizer.show_scatter_plot_age(classroom.students)
            break
        elif option.strip() == "2":
            print("Plotting...📊")
            Visualizer.show_scatter_plot_age(school.students)
            break
        else:
            print("❌ Invalid choice. Try again.")
            continueing = input("Would you like to try again?(y/*): ")
            if continueing.lower().strip() != 'y':
                return
def show_subject_average_scores():
    """Show the average scores for each subject in the school (Compare Each Class based on Subject)"""
    print()
    print("-" * 70)
    print("Show Scatter Plot of Age")
    print("-" * 70)
    print("Plotting...📊")
    try:
        school = School(FileManager.load_file(DATA_BASE_PATH))
    except ValueError:
        print(f"⚠️ Error: {ValueError}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
    Visualizer.show_subject_averages_bar_chart(school.students)

if __name__ == "__main__":
    DATA_BASE_PATH = "data/student-scores.csv"
    main_menu()
