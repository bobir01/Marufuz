from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Account, Transaction, Card, Login, Log


class CustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = '__all__'


class AccountForm(forms.ModelForm):
  class Meta:
    model = Account
    fields = '__all__'


class TransactionForm(forms.ModelForm):
  class Meta:
    model = Transaction
    fields = ['account', 'transaction_type', 'amount', 'transaction_date', 'transaction_time', 'description',
              'process_status']


class CardForm(forms.ModelForm):
  class Meta:
    model = Card
    fields = ['card_number', 'customer', 'bank_name', 'card_status']


class LoginForm(forms.ModelForm):
  class Meta:
    model = Login
    fields = '__all__'


class LogForm(forms.ModelForm):
  class Meta:
    model = Log
    fields = '__all__'


class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField(widget=forms.PasswordInput)

  def __init__(self, *args, **kwargs):
    self.user_cache = None
    super().__init__(*args, **kwargs)

  def clean(self):
    username = self.cleaned_data.get('username')
    password = self.cleaned_data.get('password')
    if username and password:
      self.user_cache = authenticate(username=username, password=password)
      if self.user_cache is None:
        raise forms.ValidationError("Invalid username or password")
      elif not self.user_cache.is_active:
        raise forms.ValidationError("This account is inactive.")
    return self.cleaned_data

  def get_user(self):
    return self.user_cache




