from itertools import product
from django.shortcuts import render
from .models import Cars

def home(request):
    cars = Cars.objects.all()

    data = {
        'cars' : cars
    }
    return render(request, 'home.html', data)


def contact(request):
	return render(request, 'contact.html', {})


def cars(request):
    cars = Cars.objects.all()

    data = {
        'cars' : cars
    }

    return render(request, 'cars.html', data)


def about(request):
	return render(request, 'about.html', {})


def terms(request):
	return render(request, 'terms.html', {})


def detail(request):
    cars = Cars.objects.all()

    data = {
        'cars' : cars
    }
    return render(request, 'detail.html', data)