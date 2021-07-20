from django.shortcuts import render
from django.http import HttpResponse
from catalog.models import Category
from django.core.mail import send_mail
from django.views.generic import View, TemplateView

from .forms import ContactForm


class IndexView(TemplateView):
    template_name = 'core/index.html'


index = IndexView.as_view()

# def index(request):

#     return render(request, 'core/index.html')


def contact(request):
    success = False
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.send_email()
        success = True

    context = {
        'form': form,
        'success': success
    }
    return render(request, 'core/contact.html', context)


# def product(request):
#     return render(request, 'core/product.html')
