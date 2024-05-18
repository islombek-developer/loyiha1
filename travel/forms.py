from django import forms
from .models import Workingtravel

class CreatWorkingtravel(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput({"class": "form-control"}))
    price = forms.IntegerField(widget=forms.TextInput({"class": "form-control", "type": "number"}))
    
    class Meta:
        model = Workingtravel
        fields = ('name', 'price','category','image')
