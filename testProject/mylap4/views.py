from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# first page
def default(request):
    return HttpResponse("<h1> this is a site to calculate tax </h1>")

#second page

def calculate_tax(request, price):
    tax_rate = 0.15
    total_price = price + ( price * tax_rate )
    return HttpResponse( f"<h1>The total price after tax is: {total_price} </h1> " )

#third page
def tax_rate(request):

    tax_rate = 15
    return render(request, 'taxrate.html', {'tax_rate': tax_rate})