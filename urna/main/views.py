from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import *


def catalog(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            telephone = form.cleaned_data['telephone']
            email = form.cleaned_data['email']
            comment = form.cleaned_data['comment']
            name = f'{name} {surname}'
            data = f'Телефон: {telephone}    Почта: {email}    Комментарий: {comment}'
            mail = send_mail(name, data, 'kotik310702@gmail.com', ['kotik310702@gmail.com'])
            if mail:
                return redirect('catalog')
    else:
        form = ContactForm()
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/catalog.html', {'form': form, 'tips': tips, 'categories': categories})


def about(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/about.html', {'tips': tips, 'categories': categories})


def delivery(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/delivery.html', {'tips': tips, 'categories': categories})


def pay(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/pay.html', {'tips': tips, 'categories': categories})


def contacts(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/contacts.html', {'tips': tips, 'categories': categories})


def category_urn(request, pk):
    urn = Item.objects.filter(tip=pk).order_by('name')
    tip = ItemTip.objects.get(pk=pk).name
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/category.html', {'urn': urn, 'category': tip, 'categories': categories, 'tips': tips})


def item(request, pk):
    urn = Item.objects.get(pk=pk)
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/item.html', {'urn': urn, 'categories': categories, 'tips': tips})


def search_urn(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    search = request.GET.get('search')
    if request.method == 'GET':
        if search == "":
            urn = Item.objects.all().order_by('name')
        else:
            urn = Item.objects.filter(name__contains=search).order_by('name')
        return render(request, 'main/category.html', {'urn': urn, 'categories': categories, 'tips': tips})
    else:
        return render(request, 'main/category.html', {'categories': categories, 'tips': tips})
