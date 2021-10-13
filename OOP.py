class Person:

    # Properties
    def __init__(self, name, last_name) -> None:
        self.name = name
        self.last_name = last_name
    
    # Methods
    def walk(self):
        return "I can walk"
    
    def eat(self):
        return "I can eat"
    
    def __idk(self):
        return "I'm private method from class Person"
    
class Worker(Person):

    def __init__(self, name, last_name, salary) -> None:
        super().__init__(name, last_name)
        self.salary = salary
        self.__dni = "23134"
    
    def work(self):
        super().__idk()
        return "I can work"
    
    def walk(self):
        return "I can walk by worker"
    
    def set_dni(self, dni):
        self.__dni = dni
    
    def get_dni(self):
        print(self.__settings())
        return "Worker DNI value is: {}".format(self.__dni)
    
    def __settings(self):
        return "I'm private from class Worker"
    
    @classmethod
    def im_classmethod(cls):
        pass

    @staticmethod
    def im_staticmethod():
        return "I'm static method"

worker_2 = Worker("Pepe", "Perez", 2000)
worker_2.cambiar_dni("555555")
print(worker_2.tomar_dni())
