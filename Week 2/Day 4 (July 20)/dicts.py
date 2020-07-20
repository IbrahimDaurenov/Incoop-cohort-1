



person = {
    'name': 'Daniyar',
    'age': 22,
    'height': 188.5,
    'students': ['Ibra', 'Yaroslav'],
}

print(person)
print(person['name'])
print(person['age'])
print(person['height'])
print(person['students'])

person['age'] = person['age'] + 1

print(person)

person['phone'] = '+7701....'
print(person)


print(list(person.keys()))

print(list(person.values()))
