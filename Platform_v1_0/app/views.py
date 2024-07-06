"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import JsonResponse
from django.db.models import Avg, Sum, Count
from .models import Bids, Contact, Menu, Item
from .forms import BidForm

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )


def trading(request):
    """Renders the trading page."""
    assert isinstance(request, HttpRequest)

    return render(
        request,
        'app/trading.html',
        {
            'title':'Trading',
            'message':'Submit bids to the auction.',
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    
    # Retrieve all contacts in the database table
    contact_list = Contact.objects.order_by('name')

    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
            'contact_list': contact_list, # Embed data into the HttpResponse object
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def menu_chart(request):
    labels = []
    data = []

    queryset = Item.objects.values('menu__name_menu').annotate(menu_price=Sum('price'))
    #for entry in queryset:
    #    labels.append(entry['menu__name_menu'])
    #    data.append(entry['menu_price'])

    labels = list(queryset.values_list('menu__name_menu', flat=True).order_by('menu__name_menu'))
    data = list(queryset.values_list('menu_price', flat=True).order_by('menu__name_menu'))
    data={
        'labels': labels,
        'data': data,
    }
    
    return JsonResponse(data)


def bidding_chart(request):
    
    #labels = []
    #data = []
    #labels = list(Bids.objects.values_list('id', flat=True))
    #data = list(Bids.objects.values_list('bid_value', flat=True))
    #data={
    #    'labels': labels,
    #    'data': data,
    #}

    data = list(Bids.objects.values())
    for d in data:
        d['x'] = d.pop('id')
        d['y'] = d.pop('bid_value')

    return JsonResponse(data, safe=False)


def json_response(request):
    
    #labels = []
    #data = []
    #queryset = Item.objects.values('menu__name_menu').annotate(menu_price=Sum('price'))
    #labels = list(queryset.values_list('menu__name_menu', flat=True).order_by('menu__name_menu'))
    #data = list(queryset.values_list('menu_price', flat=True).order_by('menu__name_menu')) 
    #data={
    #    'labels': labels,
    #    'data': data,
    #}

    data = list(Bids.objects.values()[0:10])
    # for d in data:
    #    d['x'] = d.pop('id')
    #    d['y'] = d.pop('bid_value')

    return JsonResponse(data, safe=False)


def bidding_data(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            form.save()
    
    data = list(Bids.objects.values())
    #for d in data:
    #    d['x'] = d.pop('id')
    #    d['y'] = d.pop('bid_value')

    return JsonResponse(data, safe=False)