from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telephone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-control'}))
    comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class': 'form-control'}))
