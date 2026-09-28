class Student:
    def __init__(self, name, student_id, email, age, department, marks=None):
        self.name = name
        self.student_id = student_id
        self.__email = email  
        self.age = age
        self.department = department
        # Method Overloading via default arguments (handles initialized marks if provided)
        self.__marks = marks if marks is not None else []

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" in email:
            self.__email = email
        else:
            print("Invalid email format.")

    def add_marks(self, *args):
        """Allows adding a single mark, multiple marks, or a list of marks."""
        for mark in args:
            if isinstance(mark, list):
                self.__marks.extend(mark)
            else:
                self.__marks.append(mark)

    def calculate_result(self):
        """Calculates the average mark and returns a pass/fail status."""
        if not self.__marks:
            return "No marks recorded"
        
        average = sum(self.__marks) / len(self.__marks)
        status = "Pass" if average >= 40 else "Fail"
        return f"Average: {average:.2f} ({status})"

    def get_student_type(self):
        """Base method to be overridden by child classes."""
        return "General Student"

    def display_info(self):
        """Prints out standard student details."""
        print(f"ID: {self.student_id} | Name: {self.name}")
        print(f"Type: {self.get_student_type()}")
        print(f"Age: {self.age} | Dept: {self.department} | Email: {self.__email}")
        print(f"Result: {self.calculate_result()}")
        print("-" * 40)


class UndergraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, semester):
        super().__init__(name, student_id, email, age, department)
        self.semester = semester 

    def get_student_type(self):
        return "Undergraduate Student"

    def display_info(self):
        super().display_info()
        print(f"Current Semester: {self.semester}")
        print("=" * 40)


class GraduateStudent(Student):
    def __init__(self, name, student_id, email, age, department, research_topic):
        super().__init__(name, student_id, email, age, department)
        self.research_topic = research_topic

    def get_student_type(self):
        return "Graduate Student"

    def display_info(self):
        super().display_info()
        print(f"Research Topic: {self.research_topic}")
        print("=" * 40)


ug_student = UndergraduateStudent("Alice Smith", "UG101", "alice@university.edu", 20, "Computer Science", "4th Semester")
grad_student = GraduateStudent("Bob Jones", "GR502", "bob@university.edu", 25, "Data Science", "AI Ethics in Modern Tech")

ug_student.add_marks(85, 90, 78) 
grad_student.add_marks([92, 88, 95])

student_directory = [ug_student, grad_student]

print("=== SYSTEM STUDENT DIRECTORY ===\n")
for student in student_directory:
    student.display_info()
