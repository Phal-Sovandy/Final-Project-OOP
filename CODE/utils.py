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
    def find_students_in_class(students, student_class):
        """List students in a given class"""
        if not (students and student_class):  #If empty list of student
            return []
        return [student for student in students if student.student_class.lower() == student_class.lower()]
    @staticmethod
    def find_overall_average(students):
        """Find overall average score on a group of students"""
        if not students: #If empty list of student
            return 0.0
        
        total = 0.0
        for student in students:
            total += student.get_average_scores()
        return total / len(students)

    @staticmethod
    def find_failing_students(students):
        """Identify students who are failing based on average score"""
        if not students: #If empty list of student, then return empty list
            return []
        
        total_score = 0.0
        for student in students:
            total_score += student.get_average_score()

        average_among_all = total_score / len(students)
        
        failing_students = [student for student in students if student.get_average_score() < average_among_all]

        return failing_students


    
class Visuallize:
    """Show data in visuallized form"""

    @staticmethod
    def show_whisker_plot_avg_scores(students: list):
        """Show a box plot of scores for every class"""
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
        
        # Data Visuallization
        
        class_labels = list(class_avg_scores.keys())        # Label for each entity(class_name)
        average_scores = list(class_avg_scores.values())    # Students' average scores of each class
        
        #Plotting
        plt.figure(figsize=(12, 8))
        plt.boxplot(average_scores, vert=True, patch_artist=True)
        plt.xticks(range(1, len(class_labels) + 1), class_labels)
        plt.xticks(fontsize=8)
        plt.title("Box and Whisker Plot of Average Scores by Class")
        plt.xlabel("Class")
        plt.ylabel("Average Score")
        plt.tight_layout() # There are too many label on x axis
        plt.show()
    @staticmethod
    def show_pie_chart_gender(students: list):
        """Show a pie chart of gender in school or class"""
        if not students:
            print("No students' data available")
            return
        
        male_students = [student for student in students if student.gender == "male"]
        female_students = [student for student in students if student.gender == "female"]
   
        plt.figure(figsize=(12, 8))
        plt.pie([len(male_students), len(female_students)], labels= ["Male", "Female"], colors= ["Skyblue", "Pink"])
        plt.title("Students Gender Distribution")
        plt.show()

    @staticmethod
    def show_scatter_plot_age(students: list):
        """Show a scatter plot of student ages in school or class"""
        students_age = {}
        
        for student in students:
            if student.age not in students_age:
                students_age[student.age] = 1
            else:
                students_age[student.age] += 1
        
        plt.figure(figsize=(12, 8))
        plt.scatter(students_age.keys(), students_age.values(), color="tomato")
        plt.xticks(range(0, 101, 5))
        plt.xlabel("Age")
        plt.ylabel("Count")
        plt.title("Student age distribution")
        plt.show()

    @staticmethod
    def show_subject_averages_bar_chart(students: list):
        """Show a bar chart of average scores for each subject"""
        subjects_score = Analyzer.find_average_score_per_subject(students)
        
        plt.figure(figsize=(12, 8))
        plt.bar(subjects_score.keys(), subjects_score.values(), color="tomato")
        plt.xlabel("Subject")
        plt.ylabel("Average Score")
        plt.title("Average Score per Subject")
        plt.show()
    

Visuallize.show_subject_averages_bar_chart(FileManager.load_file("DATA\student-scores.csv"))
