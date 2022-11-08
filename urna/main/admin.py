from django.contrib import admin
from django.forms import ModelChoiceField

from .models import *


class UrnaMetalAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return ModelChoiceField(queryset=ItemTip.objects.filter(name='Металлические'), initial=request.user, label='Тип')


class UrnaAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return ModelChoiceField(queryset=ItemTip.objects.filter(category=Category.objects.get(name='Урны').pk).exclude(name='Металлические'), initial=request.user, label='Тип')


class BenchAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return ModelChoiceField(queryset=ItemTip.objects.filter(category=Category.objects.get(name='Лавки').pk), initial=request.user, label='Тип')


class BasesAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return ModelChoiceField(queryset=ItemTip.objects.filter(category=Category.objects.get(name='Ортопедические основания').pk), initial=request.user, label='Тип')


admin.site.register(Urna, UrnaAdmin)
admin.site.register(UrnaMetal, UrnaMetalAdmin)
admin.site.register(Bench, BenchAdmin)
admin.site.register(Bases, BasesAdmin)
admin.site.register(ItemTip)
admin.site.register(Category)
