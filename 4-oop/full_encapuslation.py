
class Field:
    """
    class representing a field with full encapsulation.

    Attributes:
    __value (any): The value stored in the field.
    """

    def __init__(self):
        """
        Initializes the Field object.
        """
        self.__value = None

    def get_value(self):
        """
        Retrieves the value stored in the field.

        Returns:
        any: The value stored in the field.
        """
        return self.__value

    def set_value(self, value):
        """
        Sets the value stored in the field.

        Args:
        value (any): New value.
        """
        self.__value = value

field = Field()
print(field.get_value())  # Outputs: Initial value

field.set_value("New value")
print(field.get_value())  # Outputs: New value