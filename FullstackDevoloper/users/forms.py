from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'fio')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'fio')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="Логин: ", widget=forms.TextInput(attrs={"class": "form-input"}))
    password = forms.CharField(label="Пароль: ", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={"class": "form-input"}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={"class": "form-input"}))
    password2 = forms.CharField(label="Повтор пароля", widget=forms.PasswordInput(attrs={"class": "form-input"}))

    class Meta:
        model = get_user_model()   # Текущая модель пользователя
        fields = ["username", "password1", "password2", "fio"]
        widgets = {
            "fio": forms.TextInput(attrs={"class": "form-input"}),
        }