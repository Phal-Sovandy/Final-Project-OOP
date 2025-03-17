"""Represent a group of student in the same class"""
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
        return self.__student_class
    @property
    def students(self):
        return self.__students
    
    def display_students_info(self):
        """Display information of all students in this class"""
        print(f"Class: {self.__student_class}")     #Print the class name
        if not self.__students:
            print("No students found!")     # Print a message if there are no students 
        for student in self.__students:
            student.show_info()     # Loop through all students and call the show_info method for each student

    def find_student(self, student_id: int):
        """Find a student by ID in this class"""
        for student in self.__students:
            if student.student_id == student_id:
                return student      # Return the student if the ID matches  
        return None     # Return None if no student with the given ID is found

    def count_students(self):
        """Return the number of students in this class"""
        return len(self.__students)     # Return the total number of students