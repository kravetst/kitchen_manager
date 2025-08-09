from django.db import models
from django.contrib.auth.models import AbstractUser


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=8)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE, related_name="dish_type")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return self.name
