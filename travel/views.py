from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .models import Category, Workingtravel
from .forms import CreatWorkingtravel

def home(request):
    work = Workingtravel.objects.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"work": work, "cats": categories})

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    work = cat.work.all()
    categories = Category.objects.all()
    return render(request, 'home.html', context={"work": work, "cats": categories})

def about(request, id):
    work = get_object_or_404(Workingtravel, id=id)
    categories = Category.objects.all()
    return render(request, 'about.html', context={"work": work, "cats": categories})
