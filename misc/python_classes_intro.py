class Animal:
    def __init__(self, name="Unknown", age=None):
        self.name = name
        self.animal_age = age
        self._name = name
        self.__name = name

    def change_name(self, new_name):
        self.name = new_name


class NewAnimal(Animal):
    def __init__(self, name=None, age=None):
        super().__init__(name, age)

    def change_age(self, new_age):
        self.animal_age = new_age


a0 = Animal()
a1 = Animal("p", 10)
print(f"a0 name = {a0.name}; a0 age = {a0.animal_age}")
print(f"a1 name = {a1.name}; a1 age = {a1.animal_age}")

a0.name = "new name"
print(f"a0 name = {a0.name}; a0 age = {a0.animal_age}")

a1.change_name("changed name")
print(f"a1 name = {a1.name}; a1 age = {a1.animal_age}")

a2 = NewAnimal()
print(f"a2 name = {a2.name}; a2 age = {a2.animal_age}")
a2.change_name("a2 new name")
a2.change_age(20)
print(f"a2 name = {a2.name}; a2 age = {a2.animal_age}")


class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.animal_age = age


p1 = Person('a', 20)


def copy_animal(animal):
    new_animal = Animal(animal.name, animal.animal_age)
    return new_animal


a3 = copy_animal(a0)
a4 = copy_animal(p1)
