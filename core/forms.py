from django import forms
from django.forms.fields import CharField

from django.conf import settings
from django.core.mail import send_mail


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    # após inclusão do widget-tweaks, removemos a função abaixo
    # def __init__(self, *args, **kwargs):
    #     super(ContactForm, self).__init__(*args, **kwargs )
    #     self.fields['name'].widget.attrs['class'] = 'form-control'
    #     self.fields['email'].widget.attrs['class'] = 'form-control'
    #     self.fields['message'].widget.attrs['class'] = 'form-control'
    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        message = 'Nome:{0}\nE-mail:{1}\n{2}'.format(name, email, message)
        send_mail('Contato Django Ecommerce', message, settings.DEFAULT_FROM_EMAIL,
                  [settings.DEFAULT_FROM_EMAIL])
