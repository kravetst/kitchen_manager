from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, DishType, Dish, Ingredient, Cuisine
from .forms import CookCreationForm, CookChangeForm


@admin.register(Cook)
class CookAdmin(UserAdmin):
    add_form = CookCreationForm
    form = CookChangeForm
    model = Cook
    list_display = ("username", "first_name", "last_name", "email", "years_of_experience")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "years_of_experience")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "first_name", "last_name", "email", "years_of_experience", "password1", "password2"),
        }),
    )


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "dish_type", "price", "get_cooks", "get_ingredients", "image_url")
    search_fields = ("name", "dish_type__name")
    list_filter = ("dish_type",)
    fields = ("name", "description", "price", "dish_type", "cuisine", "cooks", "ingredients", "image_url")

    def get_cooks(self, obj):
        return ", ".join([f"{cook.get_full_name() or cook.username}" for cook in obj.cooks.all()])
    get_cooks.short_description = "Cooks"

    def get_ingredients(self, obj):
        return ", ".join([ingredient.name for ingredient in obj.ingredients.all()])
    get_ingredients.short_description = "Ingredients"


@admin.register(Cuisine)
class CuisineAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
