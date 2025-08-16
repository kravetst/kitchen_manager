from django.urls import path
from . import views

app_name = "kitchen"

urlpatterns = [
    path("dishes/", views.dish_list, name="dish_list"),
    path("dishes/<int:pk>/", views.dish_detail, name="dish_detail"),
    path("dishes/create/", views.dish_create, name="dish_create"),
    path("cuisines/", views.cuisine_list, name="cuisine_list"),
    path("cuisines/<int:pk>/", views.cuisine_detail, name="cuisine_detail"),
]
