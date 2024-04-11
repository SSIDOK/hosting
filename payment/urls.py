from django.urls import path
from . import views

app_name = "payment"

urlpatterns = [

    path('payment/', views.payment_page, name='payment_page'),  # Це ваша сторінка у додатку payment
    path('payment/', views.success_page, name='success_page'),  # URL для сторінки успішної оплати
]
