print("Hello, World")


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"


students = [
    Student("Ali", 72),
    Student("Sara", 45),
    Student("Omar", 50)
]

for student in students:
    print(student)


# Task 2: Test Course Methods
from course import Course, InvalidMarksError, load_course

c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 75)

print(len(c))
print(c.average())
print(c.top_student())


# Task 3: Test Custom Error
try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)

print(c)


# Task 4: Load Students From File
course = load_course("Programming for AI", "marks.txt")

print(course)
print("Top student:", course.top_student())

load_course("Programming for AI", "missing.txt")


# Task 3: Test remove_student()
c = Course("X")
c.add_student("Ali", 88)

c.remove_student("Ali")
print(len(c))

try:
    c.remove_student("Zara")
except KeyError as e:
    print("KeyError:", e)