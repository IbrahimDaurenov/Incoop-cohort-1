class Car:
    def __init__(self, model, year, color, transmission):
        self.model = model
        self.year = year
        self.color = color
        self.transmission = transmission

    def description(self):
        descr = 'My car is: ' + self.model + '. It was built in '+ str(self.year) + '. It is ' + self.color + ' and has ' + self.transmission + ' transmission.'
        return descr

    def print(self):
        descr = 'My car is: ' + self.model + '. It was built in '+ str(self.year) + '. It is ' + self.color + ' and has ' + self.transmission + ' transmission.'
        print (descr)




my_car = Car('Tesla S', 2018, 'White', 'AT')
another_car = Car('Kia Rio', 2015, 'Brown', 'MT')

my_car.print()
another_car.print()

#print(my_car.description())
#print(another_car.description())
print('-'*20)


class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.skills = []

    def add_skill(self, skill):
        self.skills.append(skill)





e = Employee('Daniyar', 'Quantatitive Developer')
e.add_skill('Python')
e.add_skill('Java')
e.add_skill('C#')

print(e.name)
print(e.skills)
