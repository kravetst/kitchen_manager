from django.shortcuts import render, get_object_or_404, redirect
from kitchen.forms import DishForm
from kitchen.models import Dish, Cuisine, Cook
from django.core.paginator import Paginator


def dish_list(request):
    dishes_qs = Dish.objects.all().prefetch_related(
        "ingredients",
        "cooks",
        "dish_type"
    )

    paginator = Paginator(dishes_qs, 9)
    page_number = request.GET.get("page")
    dishes = paginator.get_page(page_number)

    cooks = Cook.objects.all()

    return render(
        request,
        "kitchen/dish_list.html",
        {"dishes": dishes, "cooks": cooks}
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
            return redirect("kitchen:dish_list")
    else:
        form = DishForm()
    return render(
        request,
        "kitchen/dish_form.html",
        {"form": form}
    )

def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    return render(request, "kitchen/cuisine_list.html", {"cuisines": cuisines})

def cuisine_detail(request, pk):
    cuisine = get_object_or_404(Cuisine, pk=pk)
    dishes_qs = Dish.objects.filter(cuisine=cuisine)

    paginator = Paginator(dishes_qs, 6)  # 6 dishes per page
    page_number = request.GET.get("page")
    dishes = paginator.get_page(page_number)

    return render(
        request,
        "kitchen/cuisine_detail.html",
        {"cuisine": cuisine, "dishes": dishes}
    )
