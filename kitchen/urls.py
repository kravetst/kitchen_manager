from django.urls import path
from . import views

urlpatterns = [
    path("dishes/", views.dish_list, name="dish_list"),
    path("dishes/<int:pk>", views.dish_detail, name="dish_detail"),
]
