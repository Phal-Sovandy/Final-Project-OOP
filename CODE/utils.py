import csv
import matplotlib.pyplot as plt
from entities import *

class FileManager:
    """Handles file operations such as saving, appending and loading student data."""
    @staticmethod
    def save_file(path: str, data: list):
        """Save student data to file."""
        try:
            with open(path, "w", newline="") as file:
                writer = csv.writer(file)
                for student in data:
                    writer.writerow([student.student_id, student.first_name, student.last_name, student.gender,
                                     student.is_dropout, student.absences, student.age, student.student_class] +
                                    list(student.scores.values()))
                print("File saving... Completed!")
        except Exception as e:
            print(e)
    @staticmethod
    def load_file(path: str):
        """Load student data from file and return it as a list of Student objects."""
        try:
            students = []  # Initialize an empty list to store student objects
            
            with open(path, "r") as file:
                data = csv.reader(file)
                next(data)  # Skip the header row
                
                for row in data:
                    # Convert the row into a Student object
                    student_id = int(row[0])
                    first_name = row[1]
                    last_name = row[2]
                    gender = row[3]
                    drop_out = (row[4] == "TRUE")  # Convert "TRUE" or "FALSE" to boolean value
                    absences = int(row[5])
                    age = int(row[6])
                    student_class = row[7]
                    scores = {
                        "math_score": float(row[8]),
                        "history_score": float(row[9]),
                        "physics_score": float(row[10]),
                        "chemistry_score": float(row[11]),
                        "biology_score": float(row[12]),
                        "english_score": float(row[13]),
                        "geography_score": float(row[14])
                    }
                    
                    # Create a Student object
                    student = Student(student_id, first_name, last_name, gender, drop_out, absences, age, student_class, **scores)
                    
                    students.append(student)
                    
            return students  # Return the list of student objects
            
        except Exception as e:
            print(e)
            return []
    @staticmethod
    def append_to_file(path: str, student: list):
        """Append a single student's data to an existing file."""
        try:
            with open(path, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([student.student_id, student.first_name, student.last_name, student.gender,
                                 student.is_dropout, student.absences, student.age, student.student_class] +
                                list(student.scores.values()))
                print("Student data appended successfully!")
        except Exception as e:
            print(e)        
class Analyzer:
    """Analyzes student performance"""
    @staticmethod
    def find_top_performers(students, n=10):
        """Find the top N students based on average score"""
        sorted_students = sorted(students, key=lambda student: student.get_average_score(), reverse=True)
        return sorted_students[:n]
    @staticmethod
    def find_low_performers(students, n=10):
        """Find the low N students based on average score"""
        sorted_students = sorted(students, key=lambda student: student.get_average_score())
        return sorted_students[:n]
    @staticmethod
    def find_average_score_per_subject(students):
        """Calculate the average score for each subject across all students"""
        subjects = ["math", "history", "physics", "chemistry", "biology", "english", "geography"]
        subject_scores = {subject: [] for subject in subjects}
        
        for student in students:
            for subject, score in student.scores.items():
                subject_scores[subject].append(score)
        
        subject_avg = {subject: sum(scores) / len(scores) for subject, scores in subject_scores.items()}
        return subject_avg
    @staticmethod
    def find_students_in_class(students: list[Student], student_class: str):
        """List students in a given class"""
        # If there is no student in the list passed in and/or no student_class passed in
        if not (students and student_class):
            print("No students' data available")
            return []
        
        return [student for student in students if student.student_class.lower() == student_class.lower()]
    @staticmethod
    def find_overall_average(students: list[Student]):
        """Find overall average score on a group of students"""
        # If there is no student in the list passed in
        if not students:
            print("No students' data available")
            return 0.0
        
        total = 0.0
        # Sum up the average of all students
        for student in students:
            total += student.get_average_score()
        # Find average by divide the sum by number of students
        return total / len(students)
    @staticmethod
    def find_failing_students(students: list[Student]):
        """Identify students who are failing based on average score"""
        # If there is no student in the list passed in
        if not students:
            return []
        # If student fall behind the average score, then consider a fail student
        failing_students = [student for student in students if student.get_average_score() < Analyzer.find_overall_average(students)]
        
        return failing_students
class Visuallize:
    """Show data in visuallized form"""
    @staticmethod
    def show_whisker_plot_avg_scores(students: list[Student]):
        """Show a box plot of scores for every class"""
        
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("No students' data available")
            return
        
        # A dictionary contains class_name as key and list of its students' average scores
        class_avg_scores = {}
        
        for student in students:
            # If a class not yet in dictionary
            if student.student_class not in class_avg_scores:
                class_avg_scores[student.student_class] = []
                
            # Append student average score to their class list
            class_avg_scores[student.student_class].append(student.get_average_score())
        
        class_labels = list(class_avg_scores.keys())        # Label for each entity(class_name)
        average_scores = list(class_avg_scores.values())    # Students' average scores of each class
        
        # VISUALLIZATION
        plt.figure(figsize=(12, 8))                                     # Window size
        plt.boxplot(average_scores, vert=True, patch_artist=True)       # Plot Box plots
        plt.xticks(range(1, len(class_labels) + 1), class_labels)       # Point position in X-axis
        plt.xticks(fontsize=8)                                          # X-axis points font size
        plt.title("Box and Whisker Plot of Average Scores by Class")    # Title of the plot
        plt.xlabel("Class")                                             # Label of X-axis
        plt.ylabel("Average Score")                                     # Label of Y-axis
        plt.tight_layout()                                              # Save space, there are too many label on x axis
        plt.show()                                                      # Plotting graph
    @staticmethod
    def show_pie_chart_gender(students: list[Student]):
        """Show a pie chart of gender in school or class"""
        
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("No students' data available")
            return
        
        male_students = [student for student in students if student.gender == "male"]       # List of male studnets
        female_students = [student for student in students if student.gender == "female"]   # List of female students
   
        # VISUALLIZATION
        plt.figure(figsize=(12, 8))     # Window size
        plt.pie([len(male_students), len(female_students)],
                 labels= ["Male", "Female"],
                 colors= ["royalblue", "deeppink"],
                 autopct='%1.2f%%',
                 startangle=90,
                 textprops={'fontsize': 12}) # Plotting Pie chart
        plt.legend(["Male", "Female"], title="Gender", loc= "upper right")   # Add legends
        plt.title("Students Gender Distribution", fontsize=16, fontweight='bold')   # Chart title
        plt.show()      #Plotting chart
    @staticmethod
    def show_scatter_plot_age(students: list[Student]):
        """Show a scatter plot of student ages in school or class"""
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("No students' data available")
            return
        
        # A dictionary contains Age as key and Number of student with that age as value
        students_age = {}
        
        # Gathering data
        for student in students:
            if student.age not in students_age:
                students_age[student.age] = 1
            else:
                students_age[student.age] += 1
        
        # VISUALLIZATION
        plt.figure(figsize=(12, 8))     # X-axis label
        plt.scatter(students_age.keys(), students_age.values(), color="deeppink") # Plot scatter plot
        plt.xticks(range(0, 101, 5))    # Points on X-axis
        plt.xlabel("Age", fontweight="bold")               # X-axis label
        plt.ylabel("Count", fontweight="bold")             # Y-axis label
        plt.title("Student age distribution", fontsize=16, fontweight="bold")   # Plot title
        plt.show()  # Plotting graph
    @staticmethod
    def show_subject_averages_bar_chart(students: list[Student]):
        """Show a bar chart of average scores for each subject"""
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("No students' data available")
            return
        
        subjects = ["math", "history", "physics", "chemistry", "biology", "english", "geography"]   # All subject
        subject_scores = {subject : [] for subject in subjects}                                     # A dictionary of subject with list of average score of every class as value
        
        # Find every unique class
        classes = []
        for student in students:
            if student.student_class not in classes:
                classes.append(student.student_class)
                
        # Find average score by subject in each class
        for each_class in classes:
            student_in_class = Analyzer.find_students_in_class(students, each_class)            # List of student in a specific class
            avg_score_per_subject = Analyzer.find_average_score_per_subject(student_in_class)   # Return object of each subject average score of a specific class
            
            # Append score of each subject to the dictionary key
            for key in avg_score_per_subject.keys():
                subject_scores[key].append(avg_score_per_subject[key])
        
        
        # VISUALLIZATION
        # Grouped bar chart
        x_positions = list(range(len(classes)))  # X-axis points
        width = 0.12                             # Bar width
        colors = ["deeppink", "springgreen", "tomato", "crimson", "gold", "dodgerblue", "blueviolet"]
        
        plt.figure(figsize=(12, 8))   # Window size
        # Shifting bar position
        for i, subject in enumerate(subjects):
            # Plotting one subject of every class at a time
            offset = i * width  # Shift bar
            adjusted_x = [x + offset for x in x_positions]  # Adjust x ticks for each subject of every class
            plt.bar(adjusted_x, subject_scores[subject], width=width, label=subject, color=colors[i])    # Plot bar chart
            
        plt.xlabel("Subject", fontweight="bold")                   # X-axis label
        plt.ylabel("Average Score", fontweight="bold")             # Y-axis label
        plt.title("Average Score per Subject", fontsize=16, fontweight="bold")  # Chart title
        plt.tight_layout()      # Save space, there are too many label on x axis
        plt.xticks([x + (width * len(subjects) / 2 - width / 2) for x in x_positions], classes, rotation=45)     # Adjusting points on X-axis
        plt.yticks(range(0, 101, 5))
        plt.grid(True)
        plt.show()  # Plotting chart
