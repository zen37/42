from .person import Person

class Teacher(Person):
    """
    A class representing a teacher.

    Attributes:
    __salary (int): teacher's salary.
    """

    def __init__(self, name: str, age: int, salary: int):
        """
        Initializes the Teacher object.

        Args:
        name (str): The teacher's name.
        age (int): The teacher's age.
        salary (int): The teacher's salary.
        """
        super().__init__(name, age)  # Calls SchoolMember's __init__
        self.__salary = salary

    def get_salary(self) -> int:
        """
        Retrieves the teacher's salary.

        Returns:
        int: The teacher's salary.
        """
        return self.__salary

    def set_salary(self, salary: int):
        """
        Sets the teacher's salary.

        Args:
        salary (int): The new salary.
        """
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = salary

    def show(self) -> str:
        """
        Returns a string representation of the teacher's details.

        Returns:
        str: A formatted string with name, age, and salary.
        """
        return super().show(Salary=self.get_salary())