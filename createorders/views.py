from django.shortcuts import render, reverse
from django.http.response import HttpResponseRedirect
from createorders.forms import OrderForm

# Create your views here.
def create_order(request):
    '''Create an order for a patient'''
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save() 
        return HttpResponseRedirect(reverse("register:home"))# redirecting to a url
    return render(request, "create_orders.html", {"form":form})
