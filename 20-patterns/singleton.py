class Sun:
    _instance = None  # Class-level variable to hold the single instance

    @classmethod
    def inst(cls):
        if cls._instance is None:
            cls._instance = Sun()  # Create the instance if it doesn't exist
        return cls._instance  # Return the same instance every time

# Usage example:
p = Sun.inst()
f = Sun.inst()
f1 = Sun.inst()
print(p is f)  # Output: True
