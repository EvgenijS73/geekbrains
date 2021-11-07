from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.height = height
        self.size = size

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class ConsumptionMaterial(Clothes):
    def coat(self):
        self.exp = self.size / 6.5 + 0.5
        print(self.exp)
        return self.exp

    def suit(self):
        self.out = 2 * self.height + 0.3
        print(self.out)
        return self.out

    @property
    def outgo(self):
        return f'total expense: {self.exp + self.out}'


cm = ConsumptionMaterial(10, 10)
cm.coat()
cm.suit()
print(cm.outgo)
