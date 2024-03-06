from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def default(request):
    return HttpResponse("<h1>This is a site to calculate tax</h1>")


def calculate_tax(request, price):
    tax_rate = 0.015
    total_price = price + ( price * tax_rate )
    return HttpResponse( f"<h1>The total price after tax is: {total_price} </h1> " )

def tax_rate(request):

    tax_rate = 15
    return render(request, 'taxrate.html', {'tax_rate': tax_rate})