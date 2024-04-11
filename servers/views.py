from django.shortcuts import render, redirect

def redirect_to_main(request):
    return redirect('main')

def dedicated_page(request):
    return render(request, 'servers/dedicated.html')

def shared_page(request):
    return render(request, 'servers/shared.html')

def virtual_page(request):
    return render(request, 'servers/virtual.html')

def redirect_to_login(request):
    return render(request, '')

def payment_page(request):
    price = request.GET.get('price', '')  # Отримати ціну з параметру URL
    return render(request, 'payment/payment_method.html', {'price': price})
