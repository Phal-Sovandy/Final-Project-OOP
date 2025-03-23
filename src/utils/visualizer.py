"""Visualize data with chart, plots,..."""
import matplotlib.pyplot as plt
from src.models.student import Student
from .analyzer import Analyzer

class Visualizer:
    """Show data in visuallized form"""
    @staticmethod
    def show_whisker_plot_avg_scores(students: list[Student]):
        """Show a box plot of scores for every class"""
        
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
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
        
        # VISUALIZATION
        plt.figure(figsize=(12, 8))                                     # Window size
        plt.boxplot(average_scores, vert=True, patch_artist=True)       # Plot Box plots
        plt.xticks(range(1, len(class_labels) + 1), class_labels, rotation=45)       # Point position in X-axis
        plt.title("Box and Whisker Plot of Average Scores by Class", fontsize=16, fontweight="bold")    # Title of the plot
        plt.xlabel("Class", fontweight="bold")                                             # Label of X-axis
        plt.ylabel("Average Score", fontweight="bold")                                     # Label of Y-axis
        plt.show()                                                      # Plotting graph
    @staticmethod
    def show_pie_chart_gender(students: list[Student]):
        """Show a pie chart of gender in school or class"""
        
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return
        
        male_students = [student for student in students if student.gender == "male"]       # List of male studnets
        female_students = [student for student in students if student.gender == "female"]   # List of female students
   
        # VISUALIZATION
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
    def show_number_students(students: list[Student]):
        """Plot dot plot for showing number of student in class or school"""
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return
        
        # A dictionary contains class_name as key and list of its students' average scores
        class_students = {}
        
        for student in students:
            # If a class not yet in dictionary
            if student.student_class not in class_students:
                class_students[student.student_class] = len(Analyzer.find_students_in_class(students, student.student_class))
        
        # VISUALIZATION
        plt.figure(figsize=(12, 8))     # X-axis label
        plt.bar(class_students.keys(), class_students.values(), edgecolor="black", color="dodgerblue")
        plt.title("Students Count Distribution", fontsize=16, fontweight="bold")
        plt.xticks(rotation=45)
        plt.xlabel("Classes", fontweight="bold")
        plt.ylabel(f"Count ({sum(class_students.values())})", fontweight="bold")
        
        bar_height = list(class_students.values())
        # Adding bars values
        for i in range(len(class_students.keys())):
            plt.text(i, bar_height[i] + 0.5, bar_height[i], ha="center") #x, y coordinate of the value, ha = horizontal alignment
        
        plt.grid()
        plt.show() # Plotting
    @staticmethod
    def show_scatter_plot_age(students: list[Student]):
        """Show a scatter plot of student ages in school or class"""
        # NECCESSARY DATA FOR VISULLIZATION
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return
        
        # A dictionary contains Age as key and Number of student with that age as value
        students_age = {}
        
        # Gathering data
        for student in students:
            if student.age not in students_age:
                students_age[student.age] = 1
            else:
                students_age[student.age] += 1
        
        # VISUALIZATION
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
            print("🔍 No students' data available")
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
        
        
        # VISUALIZATION
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
        plt.legend(subjects, title="Subjects", loc= "upper right")   # Add legends
        plt.show()  # Plotting chart
