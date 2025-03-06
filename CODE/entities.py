from abc import ABC, abstractmethod

class Student:
    """Represents a single student"""

    def __init__(self, student_id: int, first_name: str, last_name: str, gender: str,
                 drop_out: bool, absences: int, age: int, student_class: str,
                 math_score: float, history_score: float, physics_score: float,
                 chemistry_score: float, biology_score: float, english_score: float,
                 geography_score: float):
        
        self.__student_id = student_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__drop_out = drop_out
        self.__absences = absences
        self.__age = age
        self.__student_class = student_class
        self.__scores = {
            "math": math_score,
            "history": history_score,
            "physics": physics_score,
            "chemistry": chemistry_score,
            "biology": biology_score,
            "english": english_score,
            "geography": geography_score
        }

    @property
    def student_id(self):
        """Return student's ID"""
        pass

    @property
    def full_name(self):
        """Return full name of the student"""
        pass

    @property
    def age(self):
        """Return student's age"""
        pass

    @property
    def is_dropout(self):
        """Return True if the student is a dropout, otherwise False"""
        pass

    @property
    def scores(self):
        """Return student's total scores"""
        pass

    def get_average_score(self):
        """Calculate and return the student's average score"""
        pass

    def get_highest_subject(self):
        """Return the subject which the student scored highest"""
        pass

    def get_lowest_subject(self):
        """Return the subject which the student scored lowest"""
        pass

    def show_info(self):
        """Print detailed information about the student"""
        pass
class GroupStudent(ABC):
    @abstractmethod
    def display_students_info(self):
        """Display information of all students in the group (school or class)"""
        pass

    @abstractmethod
    def find_student(self, student_id: int):
        """Find and return details of a student by their ID"""
        pass
class School(GroupStudent):
    """Represents a school containing all students (All data in file)"""
    
    def __init__(self, students: list=[]):
        self.__students = students

    @property
    def students(self):
        """Return list of all students"""
        pass

    def display_students_info(self):
        """Display a list of all students in the school"""
        pass

    def find_student(self, student_id: int):
        """Find and return student by ID; Return a student object"""
        pass

    def add_student(self, student: Student):
        """Add a new student to the school"""
        pass

    def remove_student(self, student_id: int):
        """Mark a student as dropped out"""
        pass

    def modify_student(self, student_id: int, **kwargs):
        """Modify a student's details"""
        pass

    def count_students_in_class(self, student_class: str):
        """Return the number of students in a given class"""
        pass

    def filter_students_by_gender(self, gender: str):
        """Return a list of students filtered by gender"""
        pass 
class Class(GroupStudent):
    """Represents a specific class in the school"""

    def __init__(self, student_class: str, students: list=[]):
        self.__student_class = student_class
        self.__students = students

    def display_students_info(self):
        """Display information of all students in this class"""
        pass

    def find_student(self, student_id: int):
        """Find a student by ID in this class"""
        pass

    def count_students(self):
        """Return the number of students in this class"""
        pass
    
