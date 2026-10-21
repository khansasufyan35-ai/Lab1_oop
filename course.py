
class InvalidMarksError(Exception):
    """Custom error for invalid student marks."""

class Course:

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
         if marks < 0 or marks > 100:
             raise InvalidMarksError(
                f"Invalid marks for {student}: {marks}"
            )   
               # raise ValueError("Marks must be between 0 and 100")
        
         self.marks[student] = marks

    def average(self):
        if len(self.marks) == 0:
            return 0
        
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        if len(self.marks) == 0:
                    return None
        
        return max(self.marks, key=self.marks.get)

    def __len__(self):
       return len(self.marks) 
    def __str__(self):
        return (
            f"{self.name}: {len(self)} students, "
            f"average {self.average():.1f}"
        )
def load_course(name, filename):
    course = Course(name)

    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                try:
                    student, mark = line.split(",")
                    marks = int(mark)
                    course.add_student(student, marks)

                except ValueError:
                    print("Skipping invalid marks:", line)

                except InvalidMarksError as e:
                    print("Skipping:", e)

    except FileNotFoundError:
        print(f"File not found: {filename}")

    return course
if __name__ == "__main__":
    test = Course("Test")
    test.add_student("A", 50)
    print(test)

