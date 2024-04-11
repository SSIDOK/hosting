from django.urls import path
from . import views

app_name = "servers"

urlpatterns = [
    path('dedicated/', views.dedicated_page, name='dedicated_page'),
    path('shared/', views.shared_page, name='shared_page'),
    path('virtual/', views.virtual_page, name='virtual_page'),
    path('redirect_to_main/', views.redirect_to_main, name='redirect_to_main'),
    path('redirect_to_login/', views.redirect_to_login, name='redirect_to_login'),
    path('payment/', views.payment_page, name='payment_page'),
]