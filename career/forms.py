from django import forms

from career.models import hiring


class HiringForm(forms.ModelForm):
    class Meta:
        model=hiring
        fields='__all__'
