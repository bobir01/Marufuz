# from django.urls import path
# from . import views
# from .views import (
#     home, customer_list, customer_create, customer_update, customer_delete,
#     account_list, account_create, account_update, account_delete,
#     transaction_list, transaction_create, transaction_update, transaction_delete,
#     card_list, card_create, card_update, card_delete,
#     login_list, login_create, login_update, login_delete,
#     log_list, log_create, log_update, log_delete
# )

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/new/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('customers/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('accounts/', views.account_list, name='account_list'),
    path('accounts/new/', views.account_create, name='account_create'),
    path('accounts/<int:pk>/edit/', views.account_update, name='account_update'),
    path('accounts/<int:pk>/delete/', views.account_delete, name='account_delete'),
    path('transactions/',  views.transaction_list, name='transaction_list'),
    path('transactions/new/', views.transaction_create, name='transaction_create'),
    path('transactions/<int:pk>/edit/',  views.transaction_update, name='transaction_update'),
    path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    # path('transactions/', views.transaction_list, name='transaction_list'),
    # path('transactions/new/', views.transaction_create, name='transaction_create'),
    # path('transactions/<int:pk>/edit/', views.transaction_update, name='transaction_update'),
    # path('transactions/<int:pk>/delete/', views.transaction_delete, name='transaction_delete'),
    path('cards/', views.card_list, name='card_list'),
    path('cards/new/', views.card_create, name='card_create'),
    path('cards/<int:pk>/edit/', views.card_update, name='card_update'),
    path('cards/<int:pk>/delete/', views.card_delete, name='card_delete'),
    path('logins/', views.login_list, name='login_list'),
    path('logins/new/', views.login_create, name='login_create'),
    path('logins/<int:pk>/edit/', views.login_update, name='login_update'),
    path('logins/<int:pk>/delete/', views.login_delete, name='login_delete'),
    path('logs/', views.log_list, name='log_list'),
    path('logs/new/', views.log_create, name='log_create'),
    path('logs/<int:pk>/edit/', views.log_update, name='log_update'),
    path('logs/<int:pk>/delete/', views.log_delete, name='log_delete'),


]
