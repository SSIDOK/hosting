from django.shortcuts import render, redirect

def redirect_to_main(request):
    return redirect('main')

def about_page(request):
    return render(request, 'ab_cu_t/about.html')

def contact_page(request):
    return render(request, 'ab_cu_t/contact.html')

def location_page(request):
    return render(request, 'ab_cu_t/locations.html')

def terms_page(request):
    return render(request, 'ab_cu_t/terms.html')