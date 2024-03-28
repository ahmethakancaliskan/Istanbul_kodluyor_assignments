
class Student:
    def __init__(self, name, age, grade,student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        
    def display_info(self):
        print(f"{self.name:<45}{self.age:<7}{self.grade:>18}{self.student_id:>27}\n")

    def study(self, subject):
        print(f"{self.name} is studying {subject}\n")

