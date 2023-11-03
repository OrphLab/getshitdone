from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    picture = models.ImageField(upload_to='profile_pics', null = True, blank= True)
    

    def __str__(self) -> str:
        return self.username


class Task(models.Model):
    task_category =[
        ('P', 'Private'),
        ('J', 'Job')
    ]

    task_importance =[
        ('H', 'High'),
        ('N', 'Normal'),
        ('L', 'Low')
    ]
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    creation = models.DateTimeField()
    category = models.CharField(max_length=50, choices=task_category, default='P')
    deadline = models.DateTimeField()
    content  = models.TextField()
    isdone = models.BooleanField()
    importance = models.CharField(max_length=20, choices=task_importance, default='N')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)



