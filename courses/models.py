from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    credit = models.IntegerField()

    def __str__(self):
        return f"{self.title} ({self.code})"