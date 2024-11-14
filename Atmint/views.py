from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Customer, Account, Transaction, Card, Login, Log
from .forms import CustomerForm, AccountForm, TransactionForm, CardForm, LoginForm, LogForm, UserRegistrationForm, UserLoginForm


@login_required
def home(request):
    return render(request, 'atm/home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'atm/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'atm/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'atm/customer_list.html', {'customers': customers})

@login_required
def customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'atm/customer_form.html', {'form': form})

@login_required
def customer_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'atm/customer_form.html', {'form': form})

@login_required
def customer_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'atm/customer_confirm_delete.html', {'customer': customer})

@login_required
def account_list(request):
  accounts = Account.objects.all()
  return render(request, 'atm/account_list.html', {'accounts': accounts})

@login_required
def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'atm/account_form.html', {'form': form})

@login_required
def account_update(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'atm/account_form.html', {'form': form})

@login_required
def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return redirect('account_list')
    return render(request, 'atm/account_confirm_delete.html', {'account': account})

@login_required
def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'atm/transaction_list.html', {'transactions': transactions})

@login_required
def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'atm/transaction_form.html', {'form': form})

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'atm/transaction_form.html', {'form': form})

@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'atm/transaction_confirm_delete.html', {'transaction': transaction})

@login_required
def card_list(request):
    cards = Card.objects.all()
    return render(request, 'atm/card_list.html', {'cards': cards})

@login_required
def card_create(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm()
    return render(request, 'atm/card_form.html', {'form': form})

@login_required
def card_update(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect('card_list')
    else:
        form = CardForm(instance=card)
    return render(request, 'atm/card_form.html', {'form': form})

@login_required
def card_delete(request, pk):
    card = get_object_or_404(Card, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect('card_list')
    return render(request, 'atm/card_confirm_delete.html', {'card': card})

@login_required
def login_list(request):
    logins = Login.objects.all()
    return render(request, 'atm/login_list.html', {'logins': logins})

@login_required
def login_create(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_list')
    else:
        form = LoginForm()
    return render(request, 'atm/login_form.html', {'form': form})

@login_required
def login_update(request, pk):
    login = get_object_or_404(Login, pk=pk)
    if request.method == 'POST':
        form = LoginForm(request.POST, instance=login)
        if form.is_valid():
            form.save()
            return redirect('login_list')
    else:
        form = LoginForm(instance=login)
    return render(request, 'atm/login_form.html', {'form': form})

@login_required
def login_delete(request, pk):
    login = get_object_or_404(Login, pk=pk)
    if request.method == 'POST':
        login.delete()
        return redirect('login_list')
    return render(request, 'atm/login_confirm_delete.html', {'login': login})

@login_required
def log_list(request):
    logs = Log.objects.all()
    return render(request, 'atm/log_list.html', {'logs': logs})

@login_required
def log_create(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('log_list')
    else:
        form = LogForm()
    return render(request, 'atm/log_form.html', {'form': form})

@login_required
def log_update(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == 'POST':
        form = LogForm(request.POST, instance=log)
        if form.is_valid():
            form.save()
            return redirect('log_list')
    else:
        form = LogForm(instance=log)
    return render(request, 'atm/log_form.html', {'form': form})

@login_required
def log_delete(request, pk):
    log = get_object_or_404(Log, pk=pk)
    if request.method == 'POST':
        log.delete()
        return redirect('log_list')
    return render(request, 'atm/log_confirm_delete.html', {'log': log})
