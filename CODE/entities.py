from abc import ABC, abstractmethod

#===========Student===========
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
        """Get the student ID"""
        return self.__student_id

    @property
    def full_name(self):
        """Get the student's full name"""
        return f"{self.__first_name} {self.__last_name}"

    @property
    def first_name(self):
        """Get the student's first name"""
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        """Set the student's first name"""
        self.__first_name = value

    @property
    def last_name(self):
        """Get the student's last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        """Set the student's last name"""
        self.__last_name = value

    @property
    def gender(self):
        """Get the student's gender"""
        return self.__gender

    @gender.setter
    def gender(self, value):
        """Set the student's gender"""
        self.__gender = value

    @property
    def age(self):
        """Get the student's age"""
        return self.__age
   
    @age.setter
    def age(self, value):
        """Set the student's age (must be positive)"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

    @property
    def is_dropout(self):
        """Get the student's dropout status"""
        return self.__drop_out

    @is_dropout.setter
    def is_dropout(self, value):
        """Set the student's dropout status"""
        self.__drop_out = value

    @property
    def absences(self):
        """Get the student's number of absences"""
        return self.__absences

    @absences.setter
    def absences(self, value):
        """Set the student's number of absences (must be zero or positive)"""
        if value < 0:
            raise ValueError("Absences cannot be negative")
        self.__absences = value

    @property
    def student_class(self):
        """Get the student's class"""
        return self.__student_class

    @student_class.setter
    def student_class(self, value):
        """Set the student's class"""
        self.__student_class = value
    
    @property
    def scores(self):
        """Get the student's scores"""
        return self.__scores

    @scores.setter
    def scores(self, new_scores):
        """Set the student's scores (all must be positive)"""
        if any(score < 0 for score in new_scores.values()):
            raise ValueError("Scores cannot be negative")
        self.__scores = new_scores

    def get_average_score(self):
        """Calculate and return the student's average score"""
        return sum(self.__scores.values()) / len(self.__scores)

    def get_highest_subject(self):
        """Return the subject which the student scored highest"""
        return max(self.__scores.items(), key=lambda x: x[1])[0]

    def get_lowest_subject(self):
        """Return the subject which the student scored lowest"""
        return min(self.__scores.items(), key=lambda x: x[1])[0]

    def show_info(self):
        """Print detailed information about the student"""
        print(f"ID: {self.__student_id}, Name: {self.full_name}, Age: {self.__age}, Class: {self.__student_class}, Attendance: {self.__absences}, Average Score: {self.get_average_score():.2f}")

#===========Group_Of_Student_Abstract_Class===========
class GroupStudent(ABC):
    """A abstract class for grouped student classes"""
    @abstractmethod
    def display_students_info(self):
        """Display information of all students in the group (school or class)"""
        pass

    @abstractmethod
    def find_student(self, student_id: int):
        """Find and return details of a student by their ID"""
        pass

#===========School===========
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

#===========Class===========
class Class(GroupStudent):
    """Represents a specific class in the school"""
    def __init__(self, student_class: str, students=None):
        if students is None:
            students = []   # if no students are provided, initialize with an empty list
        self.__student_class = student_class    # store the class name
        self.__students = students      # store the list of students

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