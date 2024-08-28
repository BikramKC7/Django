from django.shortcuts import render
from .models import Models,Stores
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.

def all_chai(request):
    chais = Models.objects.all
    return render(request,'chaiapp/chaiapp.html',{'chais':chais})

def chai_detail(request,chai_id):
    chai = get_object_or_404(Models,pk=chai_id)
    return render(request,'chaiapp/chaidetail.html',{'chai':chai})

def chai_stores(request):
    stores = None
    if request.method =='POST':
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = Stores.objects.filter(chai_varieties=chai_variety)
    else:
        form = ChaiVarietyForm()
    return render(request,'chaiapp/chai_stores.html',{'stores':stores,'form':form})