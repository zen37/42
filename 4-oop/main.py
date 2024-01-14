def main():
    obj = Class1(100)
    obj.method1()
    obj.method2()

    obj2 = Class2()
    obj2.method(100)


class Class1:
    def __init__(anything, number):
        print("Class1: object has been created")
        anything.number = number

    def method1(anything_else):
        print("Class1: method1 called")
        print(anything_else.number)

    def method2(self):
        print("Class1: method2 called")
        print(self.number)

class Class2:
    def method(self, number):
        print("Class2: method called")
        print(number)

if __name__ == "__main__":
    main()