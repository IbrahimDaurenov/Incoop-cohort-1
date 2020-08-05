from django.db import models


class Type(models.Model):
    name = models.CharField(max_length = 64)
    language = models.CharField(max_length = 64)

    def __str__(self):
        return (self.name)


class Comment(models.Model):
    author = models.CharField(max_length = 64)
    content = models.CharField(max_length = 128)

    def __str__(self):
        return (self.author + ': ' + self.content)

class Animal(models.Model):
    name = models.CharField(max_length = 64)
    type = models.ForeignKey(Type, on_delete = models.CASCADE)
    comments = models.ManyToManyField(Comment, blank = True)
    image = models.ImageField(upload_to = 'animals', null=True, blank=True, default = None)
    
    def __str__(self):
        return (str(self.type) + ' ' + self.name)

class Room(models.Model):
    name = models.CharField(max_length = 64)
    animals = models.ManyToManyField(Animal, blank = True)

    def __str__(self):
        return (self.name)



# Create your models here.
