def validate(fn):
    '''
    A decorator to validate the arguments of the set_pixel function.
    '''
    def wrapper(x, y, z):
        # Check if x, y, z are integers and are within the range [0, 256]
        if not (isinstance(x, int) and 0 <= x <= 256) or \
           not (isinstance(y, int) and 0 <= y <= 256) or \
           not (isinstance(z, int) and 0 <= z <= 256):
            return "Function call is not valid!"
        
        return fn(x, y, z)

    return wrapper

@validate
def set_pixel(x: int, y: int, z: int) -> str:
    return "Pixel created!"

if __name__ == "__main__":
    print(set_pixel(0, 127, 300))  # Output: Function call is not valid!
    print(set_pixel(0, 127, 255))  # Output: Pixel created!
    print(set_pixel(256, 127, 255))  # Output: Function call is not valid!
    print(set_pixel(-1, 127, 255))  # Output: Function call is not valid!
