from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

class Users(models.Model):
    login = models.CharField(max_length=55)
    password = models.CharField(max_length=225)
    role = models.ManyToManyField(Roles)

class Profile(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    pass_seria = models.IntegerField(max_length=4)
    pass_num = models.IntegerField(max_length=6)