from django.db import models
from django.contrib.auth.models import User



class Notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description=models.TextField()

def str_(self):
    return self.title
 
class Homework(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject =  models.CharField(max_length=50,default='')
    title = models.CharField(max_length=100,default='')
    description=models.TextField()
    due = models.DateTimeField()
    is_finished=models.BooleanField(default=False)
    
def __str__(self):
    return self.title





class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,default='')
    is_finished=models.BooleanField(default=False)

def __str__(self):
    return self.title