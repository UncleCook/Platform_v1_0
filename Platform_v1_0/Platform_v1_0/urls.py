"""
Definition of urls for Platform_v1_0.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('trading/', views.trading, name='trading'),
    path('contact/', views.contact, name='contact'),
    path('menu-chart/', views.menu_chart, name='menu-chart'),
    path('bidding-chart/', views.bidding_chart, name='bidding-chart'),
    path('bidding-chart2/', views.bidding_data, name='bidding-chart2'),
    path('trading-chart-child-currentbidpricevalue/', views.bidding_data, name='trading-chart-child-currentbidpricevalue'),
    path("json/", views.json_response),
    
    
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
