from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} ({self.roll})"
