from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cook, DishType, Dish
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


admin.site.register(DishType)
admin.site.register(Dish)
