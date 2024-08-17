from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    email = models.EmailField(max_length=277, verbose_name="Student Email")
    number = models.CharField(max_length=15, verbose_name="Student Number")  
    
    def __str__(self):
        return str(self.id)
