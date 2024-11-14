from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CustomUser(AbstractUser):
    last_login = models.DateTimeField(null=True, blank=True)

    # Add related_name attributes to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )


class Customer(models.Model):
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=15)
  phone_number = models.CharField(max_length=15)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Account(models.Model):
  ACCOUNT_TYPE_CHOICES = [
    ('SUM', 'Sum'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
  ]

  STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
  ]

  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  account_number = models.CharField(max_length=20)
  account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE_CHOICES)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)

  def __str__(self):
    return f"{self.account_number} - {self.customer.first_name} {self.customer.last_name}"

  class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
      return f"{self.first_name} {self.last_name}"


class Account(models.Model):
  ACCOUNT_TYPE_CHOICES = [
    ('SUM', 'Sum'),
    ('USD', 'USD'),
    ('EUR', 'EUR'),
  ]

  STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
  ]

  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  account_number = models.CharField(max_length=20)
  account_type = models.CharField(max_length=3, choices=ACCOUNT_TYPE_CHOICES)
  balance = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES)

  def __str__(self):
    return f"{self.account_number} - {self.customer.first_name} {self.customer.last_name}"


class Transaction(models.Model):
  TRANSACTION_TYPE_CHOICES = [
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal'),
    ('Transfer', 'Transfer'),
  ]

  PROCESS_STATUS_CHOICES = [
    ('Finished', 'Finished'),
    ('In Process', 'In Process'),
  ]

  account = models.ForeignKey(Account, on_delete=models.CASCADE)
  transaction_type = models.CharField(max_length=20, choices=TRANSACTION_TYPE_CHOICES)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  transaction_date = models.DateField()
  transaction_time = models.TimeField()
  description = models.TextField(blank=True)
  process_status = models.CharField(max_length=20, choices=PROCESS_STATUS_CHOICES, default='In Process')

  def __str__(self):
    return f"{self.transaction_type} - {self.amount} on {self.transaction_date}"


class Card(models.Model):
  CARD_STATUS_CHOICES = [
    ('Active', 'Active'),
    ('Inactive', 'Inactive'),
  ]

  card_number = models.CharField(max_length=20)
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  bank_name = models.CharField(max_length=100)
  security_code = models.CharField(max_length=10)
  card_status = models.CharField(max_length=20, choices=CARD_STATUS_CHOICES, default='Active')

  def __str__(self):
    return self.card_number

class Login(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password_hash = models.CharField(max_length=64)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    ip_address = models.CharField(max_length=45)
    device = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    details = models.TextField()

    def __str__(self):
        return self.action
