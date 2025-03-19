import math
from src.utils.analyzer import Analyzer
from .group_students import GroupStudent
from .student import Student

class School(GroupStudent):
    """Represents a school containing all students (All data in file)"""
    def __init__(self, students=None):  
        if students is None and not isinstance(students, list):
            students = []   # If no students are provided, initialize as an empty list
        self.__students = students     # store the list of students as a private attribute

    @property
    def students(self):
        """Return the list of all students"""
        return self.__students      
    
    @property
    def classes_list(self):
        """Return a list of class name exist in school in alphabetical sorted ascending order"""
        valid_classses = {student.student_class for student in self.students}
        list_of_classes = list(valid_classses)
        list_of_classes.sort()
        return list_of_classes
    
    @property
    def count_students(self):
        """Return the number of students in the school"""
        return len(self.__students)     # Return the total number of students
    
    @property
    def count_num_class(self):
        """Return the number of class in the school"""
        valid_classses = {student.student_class for student in self.students}
        return len(valid_classses)
    
    @property
    def get_median(self):
        """Get median average score"""
        self.students.sort(key=lambda student: student.get_average_score())
        num_student = self.count_students
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
    
    def find_student(self, student_id: int):
        """Find and return student by ID; Return a student object"""
        for student in self.__students:
            if student.student_id == student_id:    
                return student  # return the student if the ID is matching
        return None     # return None if there is no student with the given ID is found
    def add_student(self, student: Student):
        """Add a new student to the school"""
        self.__students.append(student)     # Add student into the list
        student.student_id = len(self.__students) + 1   # Assign a new student ID based on the current length of the students list       
    def remove_student(self, student_id: int):
        """Mark a student as dropped out"""
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found")   # Raise an error if the student doesn't found
        student.is_dropout = True   # Mark the student as dropped out      
    def modify_student(self, student_id: int, **kwargs: dict[str, float]):
        """Modify a student's details"""
        student = self.find_student(student_id)     # Find the student by their ID
        if not student:
            raise ValueError("Student not found")   # Raise an error tf the student doesn't found
        if "first_name" in kwargs:
            student.first_name = kwargs["first_name"]   # Update the student's first name if provided in kwargs
        if "last_name" in kwargs:
            student.last_name = kwargs["last_name"]     # Update the student's last name if provided in kwargs
        if "gender" in kwargs:
            student.gender = kwargs["gender"]           # Update the student's gender if provided in kwargs
        if "drop_out" in kwargs:
            student.is_dropout = kwargs["drop_out"]     # Update the student's dropout status if provided in kwargs
        if "absences" in kwargs:
            student.absences = kwargs["absences"]       # Update the student's absences if provided in kwargs 
        if "age" in kwargs:
            student.age = kwargs["age"]                 # Update the student's age if provided in kwargs
        if "student_class" in kwargs:
            student.student_class = kwargs["student_class"]     # Update the student's class if provided in kwargs
        for subject in student.scores:
            if subject in kwargs:
                student.scores[subject] = kwargs[subject]   # Update the student's scores for each subject if provided in kwargs 
    def filter_students_by_gender(self, gender: str):
        """Return a list of students filtered by gender"""
        return [student for student in self.__students if student.gender == gender]
        # Return the filtered list
    def display_info(self):
        """Display a summarize information about the school"""
        print("*" * 40)
        print(f"{f"🏫 SCHOOL 🏫":^40}")
        print("*" * 40)
        if not self.__students:
            print("🔍 No students found!")     # Print a message if there are no students

        print(f"{"Average":20}: {Analyzer.find_overall_average(self.students):.2f}")
        print(f"{"Median":20}: {self.get_median:.2f}")
        print(f"{"Highest Score":20}: {Analyzer.find_top_performers(self.students, 1)[0].get_average_score():.2f}")
        print(f"{"Lowest Score":20}: {Analyzer.find_low_performers(self.students, 1)[0].get_average_score():.2f}")
        print("-" * 40)
        print(f"{"Class Name":<20}{"Number of Students":>20}")
        print("-" * 40)
        for classroom in self.classes_list:
            print(f"{classroom.capitalize():<25}{len(Analyzer.find_students_in_class(self.students, classroom)):>15}")
        print("-" * 40)
        print(f"{"Number of Classes":<20}:{self.count_num_class:>19}")
        print(f"{"Number of Students":20}:{self.count_students:>19}")
        print("*" * 40)                        
