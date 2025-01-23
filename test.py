from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @abstractmethod
    def say_hi(self):
        pass

class Man(Person):
    def __init__(self, name, age, handsome_rate):
        super().__init__(name, age)
        self.handsome_rate = handsome_rate
    def say_hi(self):
        print(f"Hello I'm {self.name}")

class Woman(Person):
    def say_hi(self):
        print(f"Hi I'm {self.name}")
    def __init__(self, name, age, size3ring):
        super().__init__(name, age)
        self.size3ring = list(size3ring)

def main():
    Trung = Man("Thanh Trung", 20, 100)
    Nga = Woman("Nga", 18, [90,60,90])
    Trung.say_hi()
    Nga.say_hi()
main()