from django.shortcuts import render
from .forms import SubscriberForm
from products.models import Product

def landing(request):
    name = "Viko"
    current_day = "07.02.19 22:10"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data

        print(form.cleaned_data["name"])
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())

def home(request):
    products = Product.objects.filter(is_active=True)
    return render(request, 'landing/home.html', locals())
