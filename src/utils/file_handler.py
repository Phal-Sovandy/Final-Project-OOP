"""Handle saving, loading, appending to .CSV file"""
import csv
from src.models.student import Student

class FileManager:
    """Handles file operations such as saving, appending and loading student data."""
    @staticmethod
    def save_file(path: str, data: list):
        """Save student data to file."""
        header_row = (
            "id",
            "first_name",
            "last_name",
            "gender",
            "drop_out",
            "grade",
            "age",
            "class",
            "math_score",
            "history_score",
            "physics_score",
            "chemistry_score",
            "biology_score",
            "english_score",
            "geography_score"
        )

        try:
            with open(path, "w", newline="") as file:
                writer = csv.writer(file)
                
                writer.writerow(header_row) # Write a header row to file
                
                for student in data:
                    writer.writerow([student.student_id, student.first_name, student.last_name, student.gender,
                                     student.is_dropout, student.absences, student.age, student.student_class] +
                                    list(student.scores.values()))
                print("File saving... Completed!")
        except Exception as e:
            print(e)
    @staticmethod
    def load_file(path: str):
        """Load student data from file and return it as a list of Student objects."""
        try:
            students = []  # Initialize an empty list to store student objects
            
            with open(path, "r") as file:
                data = csv.reader(file)
                next(data)  # Skip the header row
                
                for row in data:
                    # Convert the row into a Student object
                    student_id = int(row[0])
                    first_name = row[1]
                    last_name = row[2]
                    gender = row[3]
                    drop_out = (row[4] == "True")  # Convert "True" or "True" to boolean value
                    absences = int(row[5])
                    age = int(row[6])
                    student_class = row[7]
                    scores = {
                        "math_score": float(row[8]),
                        "history_score": float(row[9]),
                        "physics_score": float(row[10]),
                        "chemistry_score": float(row[11]),
                        "biology_score": float(row[12]),
                        "english_score": float(row[13]),
                        "geography_score": float(row[14])
                    }
                    
                    # Create a Student object
                    student = Student(student_id, first_name, last_name, gender, drop_out, absences, age, student_class, **scores)
                    
                    students.append(student)
                    
            return students  # Return the list of student objects
            
        except Exception as e:
            print(e)
            return []
    @staticmethod
    def append_to_file(path: str, student: list):
        """Append a single student's data to an existing file."""
        try:
            with open(path, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([student.student_id, student.first_name, student.last_name, student.gender,
                                 student.is_dropout, student.absences, student.age, student.student_class] +
                                list(student.scores.values()))
                print("Student data appended successfully!")
        except Exception as e:
            print(e)        