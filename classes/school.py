from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()


    def list_students(self):
        for idx, stud in enumerate(self.students):
            print(f"{idx + 1}. {stud.name} {stud.school_id}")

    def find_student_by_id(self, student_id):
        for stud in self.students:
            if student_id == stud.school_id:
                return stud
        return "This ID doesn't match any students."
            



