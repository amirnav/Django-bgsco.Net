from django import forms
from contactus.models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model=ContactUs
        fields='__all__'
