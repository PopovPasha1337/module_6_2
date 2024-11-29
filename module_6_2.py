class Mammal:
    def __init__(self, name):
        self.name = name
        self.fed = False

    def eat(self, obj):
        if isinstance(obj, Fruit):
         self.fed = True
         print(f'{self.name} съел {obj.name}')
        else:
         print(f'{self.name} не стал есть{obj.name}')

class Predator(Mammal):
    def __init__(self, name):
        super().__init__(name)
        self.alive = True

    def eat(self, odj):
        if isinstance(odj, Flower):
            self.alive = False
            print(f'{self.name} не стал есть {odj.name}')
        else:
            super().eat(odj)
class Flower:
    def __init__(self, name):
        self.name = name
class Fruit:
    def __init__(self, name):
        self.name = name

a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветок семкциветик')
p2 = Fruit ('Заводной апельсин')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)


