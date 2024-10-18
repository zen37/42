from .person import Person

class Student(Person):
    """
    A class representing a student.

    Attributes:
    __grades (int): The student's grade.
    """

    def __init__(self, name: str, age: int, grades: int):
        """
        Initializes the Student object.

        Args:
        name (str): The student's name.
        age (int): The student's age.
        grades (int): The student's grade.
        """
        super().__init__(name, age)  # Calls SchoolMember's __init__
        self.__grades = grades

    def get_grades(self) -> int:
        """
        Retrieves the student's grade.

        Returns:
        int: The student's grade.
        """
        return self.__grades

    def set_grades(self, grades: int):
        """
        Sets the student's grade.

        Args:
        grades (int): The new grade.
        """
        if grades < 0 or grades > 100:
            raise ValueError("Grade must be between 0 and 100")
        self.__grades = grades

    def show(self) -> str:
        """
        Returns a string representation of the student's details.

        Returns:
        str: A formatted string with name, age, and grade.
        """
        return super().show(Grade=self.get_grades())
