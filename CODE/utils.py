import csv
import matplotlib.pyplot as plt

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
        """Load student data from file and return it as a list."""
        try:
            with open(path, "r") as file:
                data = csv.reader(file)
                return list(data)
        except Exception as e:
            print(e)

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
    def find_overall_average(students):
        """Find overall average score on a group of students"""
        total = 0
        for student in students:
            total += student.get_average_scores()
        return total / len(students)

    @staticmethod
    def find_failing_students(students):
        """Identify students who are failing based on average score"""
        total_score = 0
        for student in students:
            total_score += student.get_average_score()

        average_among_all = total_score / len(students)
        
        failing_students = []
        for student in students:
            if student.get_average_score() < average_among_all:
                failing_students.append(student)

        return failing_students


    
class Visuallize(Analyzer):
    """Show data in visuallized form"""

    @staticmethod
    def show_whisker_plot_avg_scores():
        """Show a box plot of scores for every class"""
        pass

    @staticmethod
    def show_pie_chart_gender():
        """Show a pie chart of gender in school or class"""
        pass

    @staticmethod
    def show_scatter_plot_age():
        """Show a scatter plot of student ages in school or class"""
        pass

    @staticmethod
    def show_subject_averages_bar_chart():
        """Show a bar chart of average scores for each subject"""
        pass
