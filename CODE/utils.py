import csv
class FileManager:
    """Handles file operations such as saving, appending and loading student data."""

    @staticmethod
    def save_file(path: str, data: list):
        """Save student data to file."""
        try:
            with open(path, "w") as file:
                writer = csv.writer(file)
                for student in data:
                    writer.writerow(student)
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
        pass        


class Analyzer:
    """Analyzes student performance"""

    @staticmethod
    def find_top_performers(n=10):
        """Find the top N students based on average score"""
        pass

    @staticmethod
    def find_low_performers(n=10):
        """Find the low N students based on average score"""
        pass

    @staticmethod
    def find_average_score_per_subject():
        """Calculate the average score for each subject across all students"""
        pass

    @staticmethod
    def find_failing_students():
        """Identify students who are failing in multiple subjects"""
        pass

    
class visuallize(Analyzer):
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
