class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f"ФИО:{self.fullname}, Возраст:{self.age}, Женат:{self.is_married}")

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def average_mark(self):
        return print(sum(self.marks.values()) / len(self.marks))

class Teacher(Person):
    salary = 20000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def teacher_salary(self):
        return print(self.salary + (int(self.salary / 100 * 5) * (self.experience - 3) if self.experience > 2 else 0))




def create_student():
    students = []
    student.append(Student('Асан', 16, 'Нет', {
        'Математика': 5,
        'Информатика': 5,
        'Кыргыз тили': 3,
        'Физика': 4
    }))
    return students

students = create_student()
for student in students:
    student.introduce_myself()
    for subject, mark in student.marks.items:
        print(subject, mark)
    print(student.average_mark())