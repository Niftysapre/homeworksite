from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import get_user_model

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', 
                    widget=forms.TextInput(attrs={'class':'form-input', 'placeholder':"Имя пользователя"}))
    password = forms.CharField(label='Пароль', 
                    widget=forms.PasswordInput(attrs={'class':'form-input', 'placeholder':"Пароль"}))
    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин')
    password1 = forms.CharField(label='Пароль')
    password2 = forms.CharField(label='Повтор пароля')
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name','username', 'email',  'password1', 'password2']
        labels = {
            'username': 'username', 
            'password1': 'password1',
            'password2': 'password2',
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True, label='Логин')
    class Meta:
        model = get_user_model()
        fields = ['username','first_name', 'last_name', 'email']
        labels = {
            'username': 'username', 
            'email': 'E-mail',
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }