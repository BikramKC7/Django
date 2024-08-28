from django import forms
from .models import Models

class ChaiVarietyForm(forms.Form):
    chai_variety = forms.ModelChoiceField(queryset=Models.objects.all(),label="Select chai variety")
    # chai_variety = forms.CharField()