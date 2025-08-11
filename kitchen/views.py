from django.shortcuts import render, get_object_or_404, redirect
from kitchen.forms import DishForm
from kitchen.models import Dish


def dish_list(request):
    dishes = Dish.objects.all().prefetch_related(
        "ingredients",
        "cooks",
        "dish_type"
    )
    return render(
        request,
        "kitchen/dish_list.html",
        {"dishes": dishes}
    )


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(
        request,
        "kitchen/dish_detail.html",
        {
            "dish": dish,
        },
    )

def dish_create(request):
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dish_list")
    else:
        form = DishForm()
    return render(
        request,
        "kitchen/dish_form.html",
        {"form": form}
    )
