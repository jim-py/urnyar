from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail
from .forms import *
from itertools import chain
from operator import attrgetter


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
            mail = send_mail(name, data, 'from@gmail.com', ['to@gmail.com'])
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


def category_urn(request, category_name, pk):
    urn = list(sorted(chain(Urna.objects.filter(tip=pk).order_by('name'),
                            UrnaMetal.objects.filter(tip=pk).order_by('name'),
                            Bench.objects.filter(tip=pk).order_by('name'),
                            Bases.objects.filter(tip=pk).order_by('name')),
                      key=attrgetter('name')))
    tip = ItemTip.objects.get(pk=pk).name
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    return render(request, 'main/category.html',
                  {'urn': urn, 'category': tip, 'categories': categories, 'tips': tips, 'category_name': category_name,
                   'pk': pk})


def item(request, pk, id, category_name):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    if category_name == 'Урны':
        if str(ItemTip.objects.get(pk=id).name) == 'Металлические':
            urn = UrnaMetal.objects.get(pk=pk)
            return render(request, 'main/item2urn.html',
                          {'urn': urn, 'categories': categories, 'tips': tips, 'name': urn.name})
        else:
            urn = Urna.objects.get(pk=pk)
            return render(request, 'main/item.html',
                          {'urn': urn, 'categories': categories, 'tips': tips, 'name': urn.name})
    elif category_name == 'Лавки':
        urn = Bench.objects.get(pk=pk)
        return render(request, 'main/tovar-lavka.html',
                      {'urn': urn, 'categories': categories, 'tips': tips, 'name': urn.name})
    elif category_name == 'Ортопедические основания':
        urn = Bases.objects.get(pk=pk)
        return render(request, 'main/tovar-osn.html',
                      {'urn': urn, 'categories': categories, 'tips': tips, 'name': urn.name})


def search_urn(request):
    categories = Category.objects.all()
    tips = ItemTip.objects.all().order_by('name')
    search = request.GET.get('search')
    if request.method == 'GET':
        if search == "":
            urn = list(sorted(chain(Urna.objects.all().order_by('name'),
                                    UrnaMetal.objects.all().order_by('name'),
                                    Bench.objects.all().order_by('name'),
                                    Bases.objects.all().order_by('name')),
                              key=attrgetter('name')))
        else:
            urn = list(sorted(chain(Urna.objects.filter(name__contains=search).order_by('name'),
                                    UrnaMetal.objects.filter(name__contains=search).order_by('name'),
                                    Bench.objects.filter(name__contains=search).order_by('name'),
                                    Bases.objects.filter(name__contains=search).order_by('name')),
                              key=attrgetter('name')))
        return render(request, 'main/search.html', {'urn': urn, 'categories': categories, 'tips': tips})
    else:
        return render(request, 'main/search.html', {'categories': categories, 'tips': tips})
