"""Analyze data of students"""
from src.models.student import Student

class Analyzer:
    """Analyzes student performance"""
    @staticmethod
    def find_top_performers(students, n=10):
        """Find the top N students based on average score"""
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return []
        sorted_students = sorted(students, key=lambda student: student.get_average_score(), reverse=True)
        return sorted_students[:n]
    @staticmethod
    def find_low_performers(students, n=10):
        """Find the low N students based on average score"""
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return []
        sorted_students = sorted(students, key=lambda student: student.get_average_score())
        return sorted_students[:n]
    @staticmethod
    def find_average_score_per_subject(students):
        """Calculate the average score for each subject across all students"""
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return {}
        subjects = ["math", "history", "physics", "chemistry", "biology", "english", "geography"]
        subject_scores = {subject: [] for subject in subjects}
        
        for student in students:
            for subject, score in student.scores.items():
                subject_scores[subject].append(score)
        
        subject_avg = {subject: sum(scores) / len(scores) for subject, scores in subject_scores.items()}
        return subject_avg
    @staticmethod
    def find_students_in_class(students: list[Student], student_class: str):
        """List students in a given class"""
        # If there is no student in the list passed in and/or no student_class passed in
        if not (students and student_class):
            print("🔍 No students' data available")
            return []
        
        return [student for student in students if student.student_class.lower() == student_class.lower()]
    @staticmethod
    def find_overall_average(students: list[Student]):
        """Find overall average score on a group of students"""
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return 0.0
        
        total = 0.0
        # Sum up the average of all students
        for student in students:
            total += student.get_average_score()
        # Find average by divide the sum by number of students
        return total / len(students)
    @staticmethod
    def find_failing_students(students: list[Student]):
        """Identify students who are failing based on average score"""
        # If there is no student in the list passed in
        if not students:
            print("🔍 No students' data available")
            return []
        # If student fall behind the average score, then consider a fail student
        failing_students = [student for student in students if student.get_average_score() < Analyzer.find_overall_average(students)]
        
        return failing_students