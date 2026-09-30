class Employee:
    id:int
    name:str
    department:str
    experience:int

    def punch_in(self):
        print("Employee punchIn")

    def work(self):
        print("Employee start working")

    def punch_out(self):
        print("Employee punchOut")

employee_instance1 = Employee()

employee_instance2 = Employee()

employee_instance1.punch_in()
employee_instance2.work()
