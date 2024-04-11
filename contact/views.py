from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Відправте лист на електронну пошту
            send_mail(
                'Повідомлення від користувача',
                f'Ім\'я: {name}\nЕлектронна адреса: {email}\nПовідомлення: {message}',
                settings.DEFAULT_FROM_EMAIL,
                ['pavlokolodiy824@gmail.com'],  # Замініть це на свою адресу електронної пошти
                fail_silently=False,
            )

            return redirect('contact:contact')  # Змініть на свій URL підтвердження
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

def send_message(name, email, message):
    pass