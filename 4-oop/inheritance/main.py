from school import Teacher, Student

def main():
    persons = [Teacher("Jane", 40, 3000), Student("Joe", 16, 75)]

    for person in persons:
        print(person.show())

if __name__ == "__main__":
    main()