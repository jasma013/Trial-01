class Person:
    def __init__(self, name, age, cid_number):
        self.name = name
        self.age = age
        self.cid_number = cid_number

    def walk(self):
        print(f"{self.name} is walking.")

    def talk(self):
        print(f"{self.name} is talking.")

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def __init__(self, name, age, cid_number, subject, salary, department, designation):
        # Call the __init__ method of the parent class (Person) to initialize inherited attributes
        super().__init__(name, age, cid_number)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

    def grade_students(self):
        print(f"{self.name} is grading students.")

    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

class Student(Person):
    def __init__(self, name, age, cid_number, student_id, course, year, gpa):
        # Call the __init__ method of the parent class (Person) to initialize inherited attributes
        super().__init__(name, age, cid_number)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa

    def study(self):
        print(f"{self.name} is studying.")

    def attend_class(self):
        print(f"{self.name} is attending class.")

    def write_exam(self):
        print(f"{self.name} is writing an exam.")

# Creating a Teacher object
teacher = Teacher("John Doe", 40, "CID123", "Math", 5000, "Math Department", "Professor")
print(teacher.name)  # Output: John Doe
print(teacher.subject)  # Output: Math
teacher.walk()  # Output: John Doe is walking.
teacher.teach()  # Output: John Doe is teaching Math.

# Creating a Student object
student = Student("Jane Doe", 20, "CID456", "123456", "Computer Science", 2, 3.5)
print(student.name)  # Output: Jane Doe
print(student.course)  # Output: Computer Science
student.talk()  # Output: Jane Doe is talking.
student.study()  # Output: Jane Doe is studying.
