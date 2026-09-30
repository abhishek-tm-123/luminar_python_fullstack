class Doctor:
    name:str
    specialization:str
    experience:int

    def prescribe_medicine(self):
        print(self.name," prescribe medicine method ....")

    def consult_patents(self):
        print("doctor consult method")

doctor_instance1 = Doctor()
doctor_instance2 = Doctor()

doctor_instance1.name = "abhi"

doctor_instance1.prescribe_medicine()
doctor_instance2.consult_patents()

