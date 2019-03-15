from django.shortcuts import render, get_object_or_404
from .models import Eat

def dinner(request):
    food = Eat.objects
    return render(request, 'eat/dinner.html', {'eat':food})