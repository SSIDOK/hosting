from django.urls import path
from . import views

app_name = 'ab_cu_t'

urlpatterns = [
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('location/', views.location_page, name='location_page'),
    path('terms/', views.terms_page, name='terms_page'),
    path('redirect_to_main/', views.redirect_to_main, name='redirect_to_main'),
]