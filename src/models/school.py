"""A School class represent a group of students and classes(All students in database)"""
from .group_students import GroupStudent
from .student import Student

class School(GroupStudent):
    """Represents a school containing all students (All data in file)"""
    def __init__(self, students=None):  
        if students is None:
            students = []   # If no students are provided, initialize as an empty list
        self.__students = students     # store the list of students as a private attribute

    @property
    def students(self):
        """Return the list of all students"""
        return self.__students      
    
    def display_students_info(self):
        """Display a list of all students in the school"""
        if not self.__students:
            print("No students found!")     # Print a message if there are no students exist
        for student in self.__students:
            student.show_info()     # Loop through all students and call the show_info method for each student                        

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
        
    def modify_student(self, student_id: int, **kwargs):
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

    def count_students_in_class(self, student_class: str):
        """Return the number of students in a given class"""
        count = 0
        for student in self.__students:
            if student.student_class == student_class:
                count += 1  # Increment the count if the student's class matches
        return count    # return the total count of students

    def filter_students_by_gender(self, gender: str):
        """Return a list of students filtered by gender"""
        return [student for student in self.__students if student.gender == gender]
        # Return the filtered list
