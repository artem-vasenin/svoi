# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
import re

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form__input',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form__input',
        'placeholder': 'Пароль',
    }))


class CodeForm(forms.Form):
    code = forms.CharField(
        max_length=6,
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Введите код*'})
    )


class CustomRegForm(forms.Form):
    first_name = forms.CharField(
        label='Имя',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Имя*'})
    )
    username = forms.CharField(
        label='Логин',
        max_length=30,
        widget=forms.TextInput(attrs={'class': 'form__input', 'placeholder': 'Логин*'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form__input', 'placeholder': 'Email*'})
    )
    phone = forms.CharField(
        label='Телефон',
        widget=forms.TextInput(attrs={
            'class': 'form__input',
            'placeholder': 'Телефон*',
            'pattern': r'^\+7\d{10}$',
            'title': 'Введите номер в формате +7XXXXXXXXXX (11 цифр)'
        })
    )
    birthday = forms.DateField(
        label='День рождения',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form__input'})
    )
    reason = forms.ChoiceField(
        label='Цель знакомства',
        choices=[
            ('Общение', 'Общение'),
            ('Любовь', 'Любовь'),
            ('Дружба', 'Дружба'),
            ('Взаимопомощь', 'Взаимопомощь'),
        ],
        widget=forms.Select(attrs={'class': 'form__input form__input-select'})
    )
    password = forms.CharField(
        label='Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Пароль*'})
    )
    passwordConfirm = forms.CharField(
        label='Повтор пароля',
        widget=forms.PasswordInput(attrs={'class': 'form__input', 'placeholder': 'Повтор пароля*'})
    )
    agree = forms.BooleanField(
        label='Согласие на обработку персональных данных',
        widget=forms.CheckboxInput(attrs={
            'class': 'form__input-check',
            'id': 'check',
        }),
        error_messages={
            'required': 'Необходимо согласие на обработку персональных данных.'
        }
    )

    # === Валидация отдельных полей ===
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError('Этот логин уже занят.')
        return username

    def clean_agree(self):
        agree = self.cleaned_data['agree']
        if not agree:
            raise ValidationError('Необходимо принять соглашение.')
        return agree

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError('Пользователь с таким email уже зарегистрирован.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        pattern = r'^\+7\d{10}$'
        if not re.match(pattern, phone):
            raise ValidationError('Введите номер в формате +7XXXXXXXXXX (11 цифр).')
        return phone

    # === Общая валидация (пароли) ===
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        passwordConfirm = cleaned_data.get('passwordConfirm')

        if password and passwordConfirm and password != passwordConfirm:
            raise ValidationError('Пароли не совпадают.')

        return cleaned_data

    # === Создание пользователя ===
    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            is_active=False,
        )

        return user
