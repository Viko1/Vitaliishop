from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News


def home(request):
    context = {"text": "This is from context",
               "mynumber": 5544,

               "fruits":{"Aple", "banana", "Pear", "melon"},
               "number": 100,
               }
    return render(request, "home.html", context)

def contact(request):
    context = {"sometext": "This is from contacts to the contact page!",
               "mylist": ["VIko", "Daria", "Babait"]
               }
    return render(request, "contact.html", context)

def about(request):
    context = {}
    return render(request, "about.html", context)



def news_details(request):
    obj = News.objects.get(id = 1)
    context = {
        "object": obj
    }
    return render(request, "news_details.html", context)