# inheritance is when one class inherits properties from another class

class Animal:

    def __init__(self):
        print("I am an Animal")

    def speak(self):
        raise NotImplementedError("SubClass will implement the abstract methods")


class Dog(Animal):  # Inheritance

    def __init__(self, name):
        super().__init__()
        print("I am a Dog")
        self.name = name

    def speak(self):
        print(f"{self.name} says woof!")

    def eat(self):
        print("Dog is eating")


class Cat(Animal):

    def __init__(self, name):
        super().__init__()
        print("I am a Cat")
        self.name = name

    def speak(self):
        print(f"{self.name} says meow!")

    def eat(self):
        print("Cat is eating")


nani = Dog("Nani")
isis = Cat("Isis")

print(type(nani))
nani.speak()
nani.eat()


def pet_speak(pet):
    pet.speak()


# polymorphism pet_speak() executes different method implementations of Dog and Cat class based the instance type
# passed to the method

pet_speak(nani)
pet_speak(isis)
