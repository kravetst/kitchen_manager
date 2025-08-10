from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Cook, Dish, DishType


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience"
        )


class CookChangeForm(UserChangeForm):
    password = None  # прибираємо поле пароля

    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "years_of_experience"
        )


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ["name", "description", "price", "dish_type", "cooks", "ingredients"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 3}),
            "cooks": forms.CheckboxSelectMultiple(),
            "ingredients": forms.CheckboxSelectMultiple(),
        }
