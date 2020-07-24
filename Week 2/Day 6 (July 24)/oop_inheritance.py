class Animal:
    def __init__(self, name = 'Murka', color = 'White', type = 'Cat'):
        self.name = name
        self.color = color
        self.type = type



class Dog(Animal):
    def __init__(self, name, color, type, woof_type):
        self.woof_type = woof_type
        super().__init__(name, color, type)

a = Dog('Trixie', 'Black', 'Labrador', 'WOOOOOOOOOOOOF')
print(a.name)
print(a.color)
print(a.type)
print(a.woof_type)
