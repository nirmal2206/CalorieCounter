from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django import forms


username_attrs = {'class':'form-control', 'placeholder':'Username', 'autofocus':''}

email_attrs = {'class':'form-control','placeholder':'Email Address', }
password_one_attrs = {'class':'form-control', 'placeholder':'Password',}
password_two_attrs = {'class':'form-control', 'placeholder':'Password Confirmation',}

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs=username_attrs),)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs=email_attrs))
    password1 = forms.CharField(min_length=8, max_length=25, widget=forms.PasswordInput(attrs=password_one_attrs),)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=password_two_attrs),)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        User.objects.create_user(username=username, email=email, password=password1)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count():
            raise forms.ValidationError('Email already registered.')
        return email
    
    def clean_password1(self):
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        if str(username) in str(password1):
            raise forms.ValidationError('Password contains personal information.')
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError('Password Mismatch.')
        return password2
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not username.isalnum():
            raise forms.ValidationError('Username must contain only alphabets and digits.')
        return username

