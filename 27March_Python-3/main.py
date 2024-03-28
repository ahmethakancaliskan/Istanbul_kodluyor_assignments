from Student import Student
from Teacher import Teacher
import random

# list with student information
students = []

# list with teacher information
teachers = []

# function for getting random unique student number
selected_numbers = []
def get_unique_id():
    while True:
        num = random.randint(100, 150)
        if num not in selected_numbers:
            selected_numbers.append(num)  
            return num

# student adding function       
def add_student():
    while True:
        name = input("\nEnter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student_id = get_unique_id()
        student = Student(name, age, grade,student_id)
        students.append(student)
        choice = input("\nDo you want to add another Student? 'Y' or 'N' (yes/no): ")
        if choice.upper() != 'Y':
            break

# teacher adding function   
def add_teacher():
    while True:
        name = input("\nEnter teacher name: ")
        age = input("Enter teacher age: ")
        subject = input("Enter teacher subject: ")
        teacher_id = get_unique_id()
        teacher = Teacher(name, age, subject,teacher_id)
        teachers.append(teacher)
        choice = input("\nDo you want to add another Teacher? 'Y' or 'N' (yes/no): ")
        if choice.upper() != 'Y':
            break

# Functions for printing lists
        
def display_students():
    print("""
---------------------------------------------------------------------------------------------------------------         
           Student Name          |         Age           |           Grade              |     Student ID 
----------------------------------------------------------------------------------------------------------------""")
    for student in students:
        student.display_info()

def display_teachers():
    print("""
---------------------------------------------------------------------------------------------------------------         
           Teacher Name          |         Age           |           Field              |     Teacher ID 
----------------------------------------------------------------------------------------------------------------""")
    for teacher in teachers:
        teacher.display_info()


# function for removing student or teacher from list
        
def remove_person():
    while True:
        who = input("\n'T' to fire Teacher\n'S' to fire Student\n'H' to back HOMEPAGE... ").upper()
        if who == 'T':
            display_teachers()
            teacher_id = int(input("\nPlease enter an valid ID to remove a teacher : "))
            for teacher in teachers:
                if teacher_id in selected_numbers:
                    teachers.remove(teacher)
                    print("\nTeacher record removed successfully.")
                    break
                else: 
                    print("\nInvalid ID or Student not found.")
                    break
             
        if who == 'S':
            display_students()
            student_id = int(input("\nPlease enter a valid ID to remove a student: "))
            found = False
            for student in students:
                if student_id in selected_numbers:
                    students.remove(student)
                    print("\nStudent record removed successfully.")
                    break
                else:
                    print("\nInvalid ID or Student not found.")
                    break

        if who == 'H':
            break
    

# menu

print("----Welcome to the School Management System----\n")
while True:
    menu = input("""------------------------\n1- ADD STUDENT\n2- ADD TEACHER\n3- DISPLAY STUDENT LIST\n4- DISPLAY TEACHER LIST\n5- FIRE STUDENT/TEACHER\n6- EXIT\n""")

    if menu == '1':
        add_student()

    if menu == '2':
        add_teacher()

    if menu == '3':
        display_students()

    if menu == '4':
        display_teachers()
    
    if menu == '5':
        remove_person()

    if menu == '6':
        break