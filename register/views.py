from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from createorders.models import Order
from register.forms import PatientForm
from register.models import Patient

# Create your views here.

def home_view(request):
    '''Landing page + list view for the orders and corresponding patients'''
    order = Order.objects.all()
    return render(request, "home.html", {"orders": order})

def register(request):
    '''create patient wiht name and address in the model database for patient'''
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return HttpResponseRedirect(reverse("register:home"))# redirecting to a url
    return render(request, "register.html", {"form":form})
