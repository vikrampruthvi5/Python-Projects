from django.shortcuts import render, redirect
from isbnlib import meta, cover

from .models import book

def index(request):
    context = {
        'books' : book.objects.all()
    }

    return render(request, "BookShop/index.html", context)