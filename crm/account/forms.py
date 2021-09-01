from django.forms import ModelForm
from .models import *

class AddContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        exclude=['user']