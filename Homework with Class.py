class Animal:
    def eat(self):
        return 'Animal is eating'

    def sleep(self):
        return 'Animal is sleeping'

class Bird(Animal):
    def sleep(self):
        return 'Animal is sleeping'
    def eat(self):
        return 'bird is pecking at its food'
    def fly(self):
        return 'Bird is flying'

class Fish(Animal):
    def sleep(self):
        return 'Fish is sleeping'
    def swim(self):
        return 'Animal is swimming'






