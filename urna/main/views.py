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
    return render(request, 'main/catalog.html', {'form': form, 'categories': tips, 'cat': categories})


def about(request):
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/about.html', {'categories': categories})


def delivery(request):
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/delivery.html', {'categories': categories})


def pay(request):
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/pay.html', {'categories': categories})


def contacts(request):
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/contacts.html', {'categories': categories})


def category(request):
    urn = Item.objects.all()
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/category.html', {'urn': urn, 'categories': categories})


def category_urn(request, pk):
    urn = Item.objects.filter(tip=pk).order_by('name')
    tip = ItemTip.objects.get(pk=pk).name
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/category.html', {'urn': urn, 'category': tip, 'categories': categories})


def item(request, pk):
    urn = Item.objects.get(pk=pk)
    categories = ItemTip.objects.all().order_by('name')
    return render(request, 'main/item.html', {'urn': urn, 'categories': categories})


def search_urn(request):
    categories = ItemTip.objects.all().order_by('name')
    search = request.GET.get('search')
    if request.method == 'GET':
        if search == "":
            urn = Item.objects.all().order_by('name')
        else:
            urn = Item.objects.filter(name__contains=search).order_by('name')
        return render(request, 'main/category.html', {'urn': urn, 'categories': categories})
    else:
        return render(request, 'main/category.html', {'categories': categories})
