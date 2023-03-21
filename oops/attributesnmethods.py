# define a class
class Dog:
    # class object attribute is like static variable in java which is same of all the instances of a class
    animal_class = 'mammal'

    # init method is a special method in python which is automatically called when you create instance of a class
    # self here is referencing to the instance of a class
    def __init__(self, breed, name="Sammy"):  # default attribute name
        self.breed = breed
        self.name = name
        self.spots = False  # notice we can have other attributes which may not be passed while creating an instance
        # of a class

    # methods
    def bark(self):
        print(f"Woof!! My name is {self.name}")


my_dog = Dog("Lab", "Frankie")

print(my_dog.name)  # fetching name of an instance of a class Dog
print(my_dog.animal_class)
print(my_dog.bark())  # method call
