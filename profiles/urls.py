from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('subscribe_to_maillist/', views.subscribe_to_maillist, name='subscribe_to_maillist'),
]