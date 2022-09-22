from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import database
from store.models import OrderItem, Product, Variation
from django.db.models import Count, F, Value

def homepage(request):
    return render(
        request,
        "testapp/homepage.html"
    )


def database_update(request):
    database.UPDATE_DISCOUNT()
    database.UPLOAD_CATEGORIES()
    database.UPLOAD_PRODUCTS()
    database.UPLOAD_TAGS()
    database.UPDATE_PROUCTS()
    database.UPDATE_KEYVALUE()
    database.UPDATE_VARIATIONS()
    database.inventory()
    return HttpResponseRedirect(reverse("store:homepage"))



def clear_database_but_images(request):
    database.clear_all_but_images()
    return HttpResponseRedirect(reverse("store:homepage"))



def clear_database_images(request):
    database.clear_images()
    return HttpResponseRedirect(reverse("store:homepage"))