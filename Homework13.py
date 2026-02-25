class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_info(self):
        print(f"Student: {self.first_name} {self.last_name}")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, index):
        if 0 <= index < len(self.students):
            self.students.pop(index)
        else:
            print("incorrect index!")

    def show_students(self):
        print(f"School: {self.name}")
        for student in self.students:
            student.get_info()


school1 = School("N221 Public School", "Tbilisi")

student1 = Student("Giorgi", "Beridze", 15)
student2 = Student("Nino", "Kapanadze", 16)
student3 = Student("Luka", "Maisuradze", 14)

school1.add_student(student1)
school1.add_student(student2)
school1.add_student(student3)

school1.show_students()

school1.remove_student(1)

print("\nAfter deletion:")
school1.show_students()