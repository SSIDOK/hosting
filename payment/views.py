# views.py

from django.shortcuts import render, redirect


def payment_page(request):
    price = request.GET.get('price', '')  # Отримати ціну з параметру URL
    return render(request, 'payment/payment_method.html', {'price': price})


def success_page(request):
    return render(request, 'payment/success_page.html')
