import math

from src.utils.analyzer import Analyzer
from .group_students import GroupStudent
#===========Class===========
class Classroom(GroupStudent):
    """Represents a specific class in the school"""
    def __init__(self, student_class: str, students=None):
        if students is None:
            students = []   # if no students are provided, initialize with an empty list
        self.__student_class = student_class    # store the class name
        self.__students = students      # store the list of students
    
    @property
    def student_class(self):
        """Return student's class name"""
        return self.__student_class
    
    @student_class.setter
    def student_class(self, new_class_name: str):
        if new_class_name and all(char.isalpha() or char.isspace() for char in new_class_name):
            self.student_class = new_class_name
    
    @property
    def students(self):
        """"Return students list in class"""
        return self.__students
    
    def find_student(self, student_id: int):
        """Find a student by ID in this class"""
        for student in self.__students:
            if student.student_id == student_id:
                return student      # Return the student if the ID matches  
        return None     # Return None if no student with the given ID is found
    def count_students(self):
        """Return the number of students in this class"""
        return len(self.__students)     # Return the total number of students   
    def get_median(self):
        """Get median average score"""
        self.students.sort(key=lambda student: student.get_average_score())
        num_student = self.count_students()
        if num_student == 0:
            return 0.0
        if num_student % 2 == 0: # Even number of students
            mid1 = math.floor(num_student / 2) - 1
            mid2 =  math.floor(num_student / 2)
            student_1 = self.students[mid1].get_average_score()
            student_2 = self.students[mid2].get_average_score()
            return (student_1 + student_2) / 2
        median_loc = math.floor(num_student / 2) # Odd number of students
        return self.students[median_loc].get_average_score()
    def display_info(self):
        """Display summary information of a class"""
        print("*" * 40)
        print(f"{f"Class: {self.__student_class}":^40}")
        print("*" * 40)
        if not self.__students:
            print("🔍 No students found!")     # Print a message if there are no students 

        print(f"{"Average":20}: {Analyzer.find_overall_average(self.students):.2f}")
        print(f"{"Median":20}: {self.get_median():.2f}")
        print(f"{"Highest Score":20}: {Analyzer.find_top_performers(self.students, 1)[0].get_average_score():.2f}")
        print(f"{"Lowest Score":20}: {Analyzer.find_low_performers(self.students, 1)[0].get_average_score():.2f}")
        print(f"{"Number of Students":20}: {self.count_students()}")
        print("*" * 40)