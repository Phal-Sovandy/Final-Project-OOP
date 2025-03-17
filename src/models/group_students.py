"""An abstract class for group students class"""
from abc import ABC, abstractmethod
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
