#Создание базового класса «Работник» и его наследование для создания классов «Менеджер» и «Инженер». 
# В классе «Работник» будут общие методы, такие как «работать» и «получать зарплату», 
# а классы-наследники будут иметь свои уникальные методы и свойства, 
# такие как «управлять командой» и «проектировать системы».

class Employee:

    def work(self):
        print(self.name, "работает")

    def get_salary(self):
        print(self.name, "получает зарплату")


class Manager(Employee):

    def __init__(self, name):
        self.name = name

    def manage_team(self):
        print(self.name, "управляет командой")


class Engineer(Employee):

    def __init__(self, name):
        self.name = name

    def design_systems(self):
        print(self.name, "проектирует системы")


manager = Manager("Иван")
engineer = Engineer("Петр")

manager.work()
manager.get_salary()
manager.manage_team()

engineer.work()
engineer.get_salary()
engineer.design_systems()