class Student:
    id:int
    name:str
    standard:str
    stream:str

    def sit(self):
        print("student sitting in class")

    def listen(self):
        print("student listening to class")

    def write(self):
        print("student writing notes")

student_instance1 = Student()
student_instance2 = Student()

student_instance1.sit()
student_instance2.listen()