from django.db import models
from django.contrib.auth.models import AbstractUser


class Cuisine(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image_url = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Cuisine"
        verbose_name_plural = "Cuisines"

    def __str__(self):
        return self.name


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dish Type"
        verbose_name_plural = "Dish Types"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=225, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField("Cook", blank=True)
    ingredients = models.ManyToManyField(Ingredient, blank=True)
    cuisine = models.ForeignKey(
        Cuisine, on_delete=models.CASCADE,
        null=True, blank=True
    )
    image_url = models.URLField(max_length=500, blank=True)

    class Meta:
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return self.get_full_name() or self.username
