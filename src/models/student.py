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
        return f"{self.__first_name.capitalize()} {self.__last_name.capitalize()}"

    @property
    def first_name(self):
        """Get the student's first name"""
        return self.__first_name.capitalize()

    @first_name.setter
    def first_name(self, value: str):
        """Set the student's first name"""
        if value and all(char.isalpha() for char in value):
            self.__first_name = value
        else:
            raise ValueError("First Name must contains only characters (No Spaces)")

    @property
    def last_name(self):
        """Get the student's last name"""
        return self.__last_name.capitalize()

    @last_name.setter
    def last_name(self, value: str):
        """Set the student's last name"""
        if value and all(char.isalpha() for char in value):
            self.__last_name = value
        else:
            raise ValueError("Last Name must contains only characters (No Spaces)")

    @property
    def gender(self):
        """Get the student's gender"""
        return self.__gender

    @gender.setter
    def gender(self, value: str):
        """Set the student's gender"""
        if value and all(char.isalpha() for char in value):
            self.__gender = value
        else: 
            raise ValueError("Gender must be character")

    @property
    def age(self):
        """Get the student's age"""
        return self.__age
   
    @age.setter
    def age(self, value: int):
        """Set the student's age (must be positive)"""
        if value < 0:
            raise ValueError("Age cannot be negative")
        self.__age = value

    @property
    def is_dropout(self):
        """Get the student's dropout status"""
        return self.__drop_out

    @is_dropout.setter
    def is_dropout(self, value: bool):
        """Set the student's dropout status"""
        if isinstance(value, bool):
            self.__drop_out = value
        else:
            raise ValueError("Drop Out state must be a boolean")

    @property
    def absences(self):
        """Get the student's number of absences"""
        return self.__absences

    @absences.setter
    def absences(self, value: int):
        """Set the student's number of absences (must be zero or positive)"""
        if value < 0:
            raise ValueError("Absences cannot be negative")
        self.__absences = value

    @property
    def student_class(self):
        """Get the student's class"""
        return self.__student_class

    @student_class.setter
    def student_class(self, new_class_name: str):
        """Set the student's class"""
        if new_class_name and all(char.isalpha() or char.isspace() for char in new_class_name):
            self.student_class = new_class_name

    @property
    def scores(self):
        """Get the student's scores"""
        return self.__scores

    @scores.setter
    def scores(self, new_scores: dict):
        """Set the student's scores (all must be positive)"""
        subjects = list(self.scores.keys())
        if any(score < 0 for score in new_scores.values()):
            raise ValueError("Scores cannot be negative")
        if any(key not in subjects for key in new_scores.keys()):
            raise ValueError(f"Subjects can only be {subjects}")
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
    def get_alpha_grade_gpa(self):
        """Return a alphabetical grade of student and GPA"""
        grades = {
            # GRADE : (low-bound, high-bound, GPA)
            "A" : (90, 100, 4.0),
            "B" : (80, 89.9, 3.0),
            "C" : (70, 79.9, 2.0),
            "D" : (60, 69.9, 1.0),
            "E" : (50, 59.9, 0.5),
            "F" : (0, 49.9, 0.0)
        }
        for key, value in grades.items():
            if round(self.get_average_score(), 1) >= value[0] and round(self.get_average_score(), 1) <= value[1]:
                return (key.upper(), value[2]) # (Alpha_Grade, GPA)
        return None         
    def show_info(self):
        """Print detailed information about the student"""
        print("*" * 40)
        print(f"{"🙍‍♂️ Student Information 🙍‍♂️":^40}")
        print("*" * 40)
        print(f"{"ID":<20}: {self.student_id}")
        print(f"{"First Name":<20}: {self.first_name}")
        print(f"{"Last Name":<20}: {self.last_name}")
        print(f"{"Gender":<20}: {self.gender}")
        print(f"{"Age":<20}: {self.age}")
        print(f"{"Class":<20}: {self.student_class}")
        print(f"{"Drop Out State":<20}: {"Yes" if self.is_dropout else "No"}")
        print(f"{"Number of Absences":<20}: {self.absences}")
        print("-" * 40)
        print(f"{"Subject":<20}{"Score":>20}")
        print("-" * 40)
        for subject, score in self.scores.items():
            print(f"{subject.capitalize():<20}{score:>20}")
        print("-" * 40)
        print(f"{"Average Score":<20}:{self.get_average_score():>19.2f}")
        if self.get_alpha_grade_gpa():
            print(f"{"Alphabetical Grade":<20}:{self.get_alpha_grade_gpa()[0]:>19}")
            print(f"{"GPA":<20}:{self.get_alpha_grade_gpa()[1]:>19.1f}")
        else:
            print("⚠️ Cannot get Alphabetical Grade and GPA")
        print("*" * 40)