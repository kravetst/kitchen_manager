from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Тип страви"
        verbose_name_plural = "Типи страв"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField('Cook', blank=True)

    class Meta:
        verbose_name = "Страва"
        verbose_name_plural = "Страви"

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.CharField(max_length=10)

    class Meta:
        verbose_name = "Кухар"
        verbose_name_plural = "Кухарі"

    def __str__(self):
        return self.get_full_name() or self.username
