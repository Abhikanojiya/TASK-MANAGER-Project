from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    email=models.CharField(max_length=100)
    class Meta:
        db_table='user'

class Task(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    createdOn=models.DateField()
    completionDate=models.DateField(null=True)
    completionStatus=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    class Meta:
        db_table='task'