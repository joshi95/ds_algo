class Student:
    def __init__(self, name, age, roll_no): # First thing which gets called when you make an instance (Constructor)
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def mark_attendance(self):
        print("student ", self.name, "is marking his attenance")
        print("student ", self.name, "marked successfully")

    def give_test(self, test_name):
        print("student", self.name, "is giving test", test_name)


class Batch:
    def __init__(self, name, size, students):
        self.name = name
        self.size = size
        self.students = students
    
    def print_all_students(self):
        for student in self.students:
            print(student.name, student.roll_no)

    def get_size_of_batch(self):
        print(self.name, "size is ", self.size)

    def add_student(self, student):
        self.students.append(student)
    



if __name__ == '__main__':
    student1 = Student("shubham", 10, 1) # Makes an instance of student
    student2 = Student("vinod", 15, 2)
    student3 = Student("roushan", 10, 11)
    # print(student1.name, student1.age)
    # print(student2.name, student2.age)

    # student1.mark_attendance()

    # student2.mark_attendance()

    # student1.give_test("abcd")

    aryabhatta = Batch("Aryabhatta", 150, [])
    cv_raman = Batch("CV Raman", 100, [student3])
    #aryabhatta.print_all_students()
    #cv_raman.print_all_students()
    # cv_raman.get_size_of_batch()
    # aryabhatta.get_size_of_batch()
    aryabhatta.add_student(student1)
    aryabhatta.print_all_students()
    aryabhatta.add_student(student2)
    aryabhatta.print_all_students()


   