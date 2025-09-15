from django.db import models

class Teacher(models.Model):
    EMPLOYMENT_TYPE = [
        ("FULL", "Full-time"),
        ("PART", "Part-time"),
        ("VIS", "Visiting"),
        ("CONT", "Contract"),
        ("ADJ", "Adjunct"),
    ]
    name = models.CharField(max_length=30)
    designation= models.CharField(max_length=50)
    employess_id = models.CharField(max_length=10)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_TYPE, default="FULL")


    def __str__(self):
        return f"{self.name} ({self.designation})"