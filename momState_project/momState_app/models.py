from django.db import models

# Create your models here.




class Mom(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'


class Child(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    mother = models.ForeignKey( Mom, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'



class State(models.Model):
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class Citizen(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    residentState = models.ForeignKey(State,on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.firstName} {self.lastName}'
