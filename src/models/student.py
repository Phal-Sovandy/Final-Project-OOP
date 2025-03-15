"""A Student class represents a single student"""
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