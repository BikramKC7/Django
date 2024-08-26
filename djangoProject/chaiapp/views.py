from django.shortcuts import render
from .models import Models
from django.shortcuts import get_object_or_404

# Create your views here.

def all_chai(request):
    chais = Models.objects.all
    return render(request,'chaiapp/chaiapp.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(Models,pk=chai_id)
    return render(request,'chaiapp/chaidetail.html',{'chai':chai})