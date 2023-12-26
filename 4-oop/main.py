def main():
    obj = class1(100)
    obj.method1()
    obj.method2()

    obj2 = class2()
    obj2.method(100)


class class1:
    def __init__(anything, number):
        print("class1: object has been created")
        anything.number = number

    def method1(anything_else):
        print("class1: method1 called")
        print(anything_else.number)

    def method2(self):
        print("class1: method2 called")
        print(self.number)

class class2:
    def method(self, number):
        print("class2: method called")
        print(number)

if __name__ == "__main__":
    main()