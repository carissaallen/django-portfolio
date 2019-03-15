from django.shortcuts import render, get_object_or_404
from .models import Eat
from random import choice

def dinner(request):
    food = Eat.objects
    return render(request, 'eat/dinner.html', {'eat':food})

def meal(request):
    dinner = ['Chicken Tacos', 'Spaghetti', 'Grilled Cheese + Tomato Soup', 'Fettucini Alfredo', 'Roasted Chicken + Butternut Squash + Purple Potatoes', 'Grilled Salmon', 'Steak + Vegetables', 'Grilled Cod + French Fries', 'Chicken Enchiladas', 'Chicken Pot Pie', 'Clam Chowder']
    meal = choice(dinner)
    return render(request, 'eat/meal.html', {'food':meal})
