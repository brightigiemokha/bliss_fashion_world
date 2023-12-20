from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
    path('apply_coupon/', views.apply_coupon, name="apply_coupon"),
    path('delete_coupon/', views.delete_coupon, name="delete_coupon"),
    path('apply_next_day_delivery/', views.apply_next_day_delivery, name="apply_next_day_delivery"),
    path('delete_next_day_delivery/', views.delete_next_day_delivery, name="delete_next_day_delivery"),
]