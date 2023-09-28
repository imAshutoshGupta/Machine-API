from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    client_name = models.CharField(max_length=50)
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')

class Project(models.Model):
    project_name = models.CharField(max_length=50)
    client_id = models.ForeignKey(Client,on_delete=models.CASCADE,db_column='client_id')
    uid = models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid')