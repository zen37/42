def reverse_number(num):
    # Convert the number to a string
    num_str = str(num)
    
    # Check if the number is negative
    if num_str[0] == '-':
        # Reverse the string excluding the first character (negative sign)
        reversed_str = num_str[1:][::-1]
        # Convert the reversed string back to an integer and reapply the negative sign
        reversed_num = -int(reversed_str)
    else:
        # Reverse the string
        reversed_str = num_str[::-1]
        # Convert the reversed string back to an integer
        reversed_num = int(reversed_str)
    
    return reversed_num


def oppositeNumber(num):
    return -num

if __name__ == "__main__":
    num = 3221
    print(reverse_number(num)) # Output: 3221
    #print(oppositeNumber(num))