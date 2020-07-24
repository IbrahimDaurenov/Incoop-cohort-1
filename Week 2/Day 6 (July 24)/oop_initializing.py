class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

me = Person('Daniyar', 22, 'Boston', 'USA')
you = Person('Bob', 40, 'Cambridge', 'USA')
print('-'*20)
print(me.name)
print(me.age)
print(me.city)
print(me.country)
print('-'*20)
print(you.name)
print(you.age)
print(you.city)
print(you.country)



class Animal:
    def __init__(self, name = 'Murka', color = 'White', type = 'Cat'):
        self.name = name
        self.color = color
        self.type = type

my_friend = Animal('Flopsi', 'Brown', 'Turtle')
print('-'*20)
print(my_friend.name)
print(my_friend.color)
print(my_friend.type)
print('-'*20)


another_friend = Animal()
another_friend.color = 'Yellow'

print(another_friend.name)
print(another_friend.color)
print(another_friend.type)
print('-'*20)
