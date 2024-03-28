class Teacher:
    def __init__(self, name, age, field, teacher_id):
        self.name = name
        self.age = age
        self.field = field
        self.teacher_id = teacher_id

    def display_info(self):
        print(f"{self.name:<45}{self.age:<7}{self.field:>18}{self.teacher_id:>27} \n")

    def teach(self):
        print(f"{self.name} is teaching {self.field}/n")
