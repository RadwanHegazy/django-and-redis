from django.db import models
import random


class NameModel (models.Model)  :
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self) : return f'{self.name}'

    def create_(self) : return NameModel.objects.create(name=''.join(random.choices(['ahmed','radwan','ali'])),age=random.randrange(10,20))

    