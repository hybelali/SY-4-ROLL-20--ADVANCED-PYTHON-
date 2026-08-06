class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration
        self.fee = fee

    def display(self):
        print("Course Name:", self.name)
        print("Duration:", self.duration, "months")
        print("Fee:", self.fee)

        if self.duration <= 6:
            print("Category: Short-Term")
        else:
            print("Category: Long-Term")


class Institute:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def display_courses(self):
        for course in self.courses:
            course.display()


i = Institute()

n = int(input("Enter number of courses: "))

for x in range(n):
    name = input("Enter course name: ")
    duration = int(input("Enter duration (months): "))
    fee = float(input("Enter fee: "))

    c = Course(name, duration, fee)
    i.add_course(c)

print("Course Details")
i.display_courses()