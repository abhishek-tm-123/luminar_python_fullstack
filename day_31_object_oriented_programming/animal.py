class Animal:
    name:str
    age:int

    def eat(self):
        print("Animal is eating")

    def sleep(self):
        print("Animal is sleeping")

animal_instance1 = Animal()
animal_instance2 = Animal()

animal_instance1.eat()
animal_instance2.sleep()

