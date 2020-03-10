from django.db import models

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    is_staff = models.CharField(max_length=50)
    is_superuser = models.CharField(max_length=50)

class Faculty(models.Model):
    facuty_id = models.IntegerField(primary_key=True)
    facuty_name = models.CharField(max_length=50)

class Restaurant(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    faculy_id = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name =  models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    picture = models.ImageField((""), upload_to=None, height_field=100, width_field=100,)
    open_time = models.DateField(auto_now=False)
    rating = models.IntegerField()
    approve_by = models.CharField(max_length=50)
    approve_date = models.DateField(auto_now=False)

class Food(models.Model):
    food_id = models.IntegerField()
    food_name = models.CharField(max_length=50)
    is_vegan = models.BooleanField(default=True)

class RestaurentFood(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    food_id = models.ForeignKey(Food,on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
