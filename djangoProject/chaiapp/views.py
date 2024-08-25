from django.shortcuts import render
from .models import Models

# Create your views here.

def all_chai(request):
    chais = Models.objects.all
    return render(request,'chaiapp/chaiapp.html')