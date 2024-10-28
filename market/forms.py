from django import forms

class AuthForm(forms.Form):
    username = forms.CharField(label='Логин', max_length=50)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())