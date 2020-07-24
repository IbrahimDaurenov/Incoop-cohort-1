<center>Day 1 Outline</center>


<b>Python 3: </b>
<ul>
  <li> Object Oriented Programming

```
class Person:
  pass

p = Person()
print(p)
```

```
class Person:
      def __init__ (self, name):
          self.name =name

p = Person('Daniyar')
print(p.name)
print(p)

```

```
class Person:
      def __init__(self, first_name, last_name, age, country, city):
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.country = country
          self.city = city


p = Person('Daniyar', 'Aubekerov', 22, 'USA', 'Boston')
print(p.first_name)
print(p.last_name)
print(p.age)
print(p.country)
print(p.city)

```


```
class Person:
      def __init__(self, first_name, last_name, age, country, city):
          self.first_name = first_name
          self.last_name = last_name
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Daniyar', 'Aubekerov', 22, 'USA', 'Boston')
print(p.person_info())
```


```
class Person:
      def __init__(self, firstname='Daniyar', lastname='Aubekerov', age=22, country='USA', city='Boston'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```


```
class Person:
      def __init__(self, firstname='Daniyar', lastname='Aubekerov', age=22, country='USA', city='Boston'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```



```
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

  </li>
  <li> File Handling

```

with open('innovators.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Contribution"])
    writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
    writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
    writer.writerow([3, "Guido van Rossum", "Python Programming"])

```

```
    with open('ugly_results.csv') as file:
          csv_reader = csv.reader(file, delimiter = ',')
          for row in csv_reader:
              if row[0][0:3] not in results.keys():
                  results[row[0][0:3]] = int(row[1])
              else:
                  results[row[0][0:3]] = results[row[0][0:3]] + int(row[1])

```

```
file = open(“testfile.txt”,”w”)

file.write(“Hello World”)
file.write(“This is our new text file”)
file.write(“and this is another line.”)
file.write(“Why? Because we can.”)

file.close()
```


```
file = open(“testfile.text”, “r”)
print file.read()
print file.readline(3)
print file.readlines()
for line in file:
  print line

```

```

```


  </li>


  </ul>




<b>Homework:</b>
You need to develop social media network. User should have opportunity to:
- Register (login, password)
- Login (login, password)

Once your user is registered/loged he/she must be able to:
- Search for other users (by login)
  - send a friend request
  - If already friends then send a message
- View all friends (list of all friends logins)
- View all friend requests
  - Accept or decline them
- View all unread messages
  - Open one of them
- View last 5 inbox messages
- View last 5 sent messages
- Sign out / Exit
