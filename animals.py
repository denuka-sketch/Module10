class Animal:
    def speak(self):
        print("hello")
    def display(self):
        print("My name is Frank!")
    def move(self):
        print("running")

class Baby(Animal):
    def speak(self):
        print("Dada")
    def display(self):
        print("The baby is cute!")
    def move(self):
        print("crawl")

class Cow(Animal):
    def speak(self):
        print("Moo")
    def display(self):
        print("I am black and white!")
    def move(self):
        print("I move slow sometimes!")

class Aardvark(Animal):
    def speak(self):
        print("I don't make noise!")
    def display(self):
        print("I am subjectively decent!")
    def move(self):
        print("I walk funny!")

class Person():
    def speak(self):
        print("I got vocab!")
    def display(self):
        print("I am decent!")
    def move(self):
        print("I walk and run!")

def animal_attributes(a):
    if not isinstance(a, Animal):
        print("Not an animal!")
        return NotImplemented
    a.speak()
    a.move()
    a.display()

animal = Animal()
baby = Baby()
cow = Cow()
ardvark = Aardvark()
person = Person()
animal_attributes(animal)
animal_attributes(baby)    
animal_attributes(cow)
animal_attributes(ardvark)
animal_attributes(person)