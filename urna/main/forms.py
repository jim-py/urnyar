from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input form-input__name', 'placeholder': 'Введите имя...'}))
    surname = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input form-input__last-name', 'placeholder': 'Введите фамилию...'}))
    telephone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class': 'form-input form-input__tel', 'placeholder': 'Введите номер телефона...'}))
    email = forms.CharField(label='Почта', widget=forms.TextInput(attrs={'class': 'form-input form-input__mail', 'placeholder': 'Введите адрес почты...'}))
    comment = forms.CharField(label='Комментарий', widget=forms.TextInput(attrs={'class': 'form-input form-input__comment', 'placeholder': 'Введите ваш комментарий...'}))
