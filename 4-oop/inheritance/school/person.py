class Person:
    """
    A class representing a school member.

    Attributes:
    __name (str): The school member's name.
    __age (int): The school member's age.
    """

    def __init__(self, name: str, age: int):
        """
        Initializes the SchoolMember object.

        Args:
        name (str): The school member's name.
        age (int): The school member's age.
        """
        self.__name = name
        self.__age = age

    def get_name(self) -> str:
        """
        Retrieves the school member's name.

        Returns:
        str: The school member's name.
        """
        return self.__name

    def set_name(self, name: str):
        """
        Sets the school member's name.

        Args:
        name (str): The new name.
        """
        self.__name = name

    def get_age(self) -> int:
        """
        Retrieves the school member's age.

        Returns:
        int: The school member's age.
        """
        return self.__age

    def set_age(self, age: int):
        """
        Sets the school member's age.

        Args:
        age (int): The new age.
        """
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

    def show(self, **kwargs) -> str:
        """
        Returns a string representation of the school member's details.

        Args:
        **kwargs: Additional attributes to include.

        Returns:
        str: A formatted string with name, age, and additional attributes.
        """
        base_str = f"Name: {self.get_name()}, Age: {self.get_age()}"
        return base_str + ", " + ", ".join(f"{key}: {value}" for key, value in kwargs.items())