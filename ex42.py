## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

class Dog(Animal):  # Dog is-a Animal
    def __init__(self, name):
        self.name = name

class Cat(Animal):  # Cat is-a Animal
    def __init__(self, name):
        self.name = name

class Person(object):  # Person is-a object
    def __init__(self, name):
        self.name = name
        self.pet = None  # Person has-a pet of some kind

class Employee(Person):  # Employee is-a Person
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):  # Fish is-a object
    pass

class Salmon(Fish):  # Salmon is-a Fish
    pass

class Halibut(Fish):  # Halibut is-a Fish
    pass

rover = Dog("Rover")  # rover is-a Dog
satan = Cat("Satan")  # satan is-a Cat

mary = Person("Mary")  # mary is-a Person
mary.pet = satan  # mary has-a pet (satan)

frank = Employee("Frank", 120000)  # frank is-a Employee
frank.pet = rover  # frank has-a pet (rover)

flipper = Fish()  # flipper is-a Fish
crouse = Salmon()  # crouse is-a Salmon

harry = Halibut()  # harry is-a Halibut
