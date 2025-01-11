from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    cet_marks = models.IntegerField()
    aadhar_card = models.FileField(upload_to='documents/')
    cet_marksheet = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.name
