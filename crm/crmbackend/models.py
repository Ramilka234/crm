from django.db import models


class Roles(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

class Users(models.Model):
    login = models.CharField(max_length=55)
    password = models.CharField(max_length=225)
    role = models.ManyToManyField(Roles)
    banned = models.BooleanField(default=False)
    ban_reason = models.CharField(null=True, blank=True)

class Profiles(models.Model):
    user_id = models.OneToOneField(Users, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    pass_seria = models.IntegerField(max_length=4)
    pass_num = models.IntegerField(max_length=6)
    email = models.CharField(max_length=85)
    phone_number = models.IntegerField(max_length=13)

    def __str__(self):
        self.name


class Status(models.Model):
    name = models.CharField(max_length=55)

class Houses(models.Model):
    price = models.FloatField()
    one_bed = models.IntegerField()
    name = models.CharField(max_length=55)
    two_bed = models.IntegerField()
    description = models.CharField(max_length=255)
    is_prepayment = models.BooleanField(default=False)
    min_prepayment = models.FloatField(default=0)

class Orders(models.Model):
    profile_id = models.ManyToManyField(Profiles)
    house_id = models.ForeignKey(Houses, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(null=True, blank=True)
    departure_time = models.DateTimeField(null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    admin_comment = models.CharField(null=True, blank=True)
    total_coast = models.FloatField()
    prepayment = models.FloatField()
class House_Photos(models.Model):
    url = models.CharField()
    house_id = models.ForeignKey(Houses, on_delete=models.CASCADE)
