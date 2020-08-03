from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length = 30)
    code = models.CharField(max_length = 3)

    def __str__(self):
        return (self.name + ' (' + self.code + ')')

class Pizza(models.Model):
    name = models.CharField(max_length = 20)
    country = models.ForeignKey(Country, on_delete = models.CASCADE, related_name = 'countries')
    diameter = models.IntegerField()

    def __str__(self):
        return (self.name + ' ' + str(self.country) + ' ' + str(self.diameter) + 'cm')
