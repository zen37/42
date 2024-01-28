def FizzBuzz(from_val, to_val):
    result = []
    for i in range(from_val, to_val+1):
        #print("i=",i)
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

def main():
    result = FizzBuzz(1, 15)
    print(result)

if __name__ == "__main__":
    main()