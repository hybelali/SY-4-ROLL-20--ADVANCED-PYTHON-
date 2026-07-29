# Decorator to add a formatted report header
def report_template(func):
    def wrapper(*args, **kwargs):
        print("=" * 50)
        print("        STUDENT PERFORMANCE REPORT")
        print("=" * 50)

        func(*args, **kwargs)

        print("=" * 50)
        print("        End of Report")
        print("=" * 50)

    return wrapper


class Report:
    # Class Variable
    institute = "Ajeenkya DY Patil Unviversity"

    # Constructor (Magic Method)
    def __init__(self, student_name, roll_number, marks):
        self.student_name = student_name
        self.roll_number = roll_number
        self.marks = marks

    # Class Method
    @classmethod
    def update_institute(cls, new_name):
        cls.institute = new_name

    # Magic Method
    def __str__(self):
        return (
            f"Student Name : {self.student_name}\n"
            f"Roll Number  : {self.roll_number}\n"
            f"Marks        : {self.marks}"
        )

    # Method to calculate grade
    def calculate_grade(self):
        if self.marks >= 80:
            return "A+"
        elif self.marks >= 70:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "F"

    # Decorator applied
    @report_template
    def generate_report(self):
        print(f"Institution : {Report.institute}")
        print(self)

        grade = self.calculate_grade()

        if self.marks >= 40:
            result = "PASS"
        else:
            result = "FAIL"

        print(f"Grade       : {grade}")
        print(f"Result      : {result}")
      
# Main Program
student1 = Report("Aryan Rikke", 201, 88)
student1.generate_report()

print()

# Update institute name using class method
Report.update_institute("Ajeenkya DY Patil University")

student2 = Report("Bharat Patel", 202, 37)
student2.generate_report()