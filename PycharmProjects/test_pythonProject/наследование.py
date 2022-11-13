class Person:
    def _init_(self, name):
        self.name = name

    def say_hello(self):
        print(f"{self.name} says hello!")


class Child(Person):
    name = "Sasha"

    def draw(selfself):
        print("Рисование линии")


class Teacher(Person):
    name = "Inna"

    def draw(selfself):
        print("Рисование прямоугольника")


c1 = Child()
t1 = Teacher()
c1.say_hello()
t1.say_hello()
