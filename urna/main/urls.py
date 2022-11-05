from django.urls import path
from .views import *

urlpatterns = [

    path('category/<int:pk>', category_urn, name='category_urn'),
    path('item/<int:pk>', item, name='item'),
    path('search/', search_urn, name='search_urn'),



    path('catalog/', catalog, name='catalog'),
    path('about/', about, name='about'),

    path('delivery/', delivery, name='delivery'),
    path('pay/', pay, name='pay'),
    path('contacts/', contacts, name='contacts'),
]
