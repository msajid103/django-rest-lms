from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=30)
    dep_id = models.CharField(max_length=10)
    description = models.TextField(max_length=150)

    def __str__(self):
        return f"{self.name} ({self.dep_id})"