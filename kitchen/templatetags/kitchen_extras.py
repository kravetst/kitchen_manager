from django import template
import re

register = template.Library()

@register.filter
def dish_img(value):
    """
    Convert dish name to a lowercase filename with underscores and .jpg extension.
    Example: 'Margherita Pizza' -> 'margherita_pizza.jpg'
    """
    if not value:
        return "main-menu.jpg"
    # remove non-alphanumeric characters, replace spaces with underscores
    filename = re.sub(r'[^0-9a-zA-Z ]+', '', value).lower().replace(" ", "_")
    return f"img/curved-images/{filename}.jpg"

@register.filter
def cuisine_img(value):
    """
    Convert cuisine name to a lowercase filename with .jpg extension.
    Example: 'Italian' -> 'Italy.jpg' if you want custom mapping.
    """
    if not value:
        return "main-menu.jpg"

    # Custom mapping for your cuisine names if they differ
    mapping = {
        "Italy": "Italy.jpg",
        "Japanese": "Japanese.jpg",
        "Mexico": "Mexico.jpg",
    }
    return f"img/image-of-cuisine-names/{mapping.get(value, 'main-menu.jpg')}"
