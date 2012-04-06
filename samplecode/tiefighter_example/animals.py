#!/usr/bin/env python

class Animal(object):
    def __init__(self, name):
        self.name = name

    def can_eat(self, food):
        pass

    def eat(self, food):
        pass

    def speak(self):
        pass

    def die(self):
        print self.name, "lived a good life"

    def __str__(self):
        return self.__class__.__name__ + ": " + self.name

class Dog(Animal):
    def can_eat(self, food):
        return True

    def eat(self, food):
        print self.name, "gobbles", food

    def speak(self):
        print self.name + ": woof"


class Cat(Animal):
    def __init__(self, name):
        Animal.__init__(self, "Mrs. "+name)

    def can_eat(self, food):
        return food.lower() == "fish"

    def eat(self, food):
        print self.name, "sniffs", food

    def speak(self):
        print self.name, "walks away"

class Robot(object):
    battery = 0

    def charge(self, amnt):
        self.battery += amnt


    def die(self):
        print self.name, "cannot die"

class RobotDog(Robot, Dog):
    def die(self, typ=Dog):
        typ.die(self)

charlie = RobotDog("Charlie")
charlie.eat("stuff")
charlie.charge(3)
print charlie.battery
charlie.die()
charlie.die(Robot)
charlie.die(typ=Dog)
charlie.die(Dog)
