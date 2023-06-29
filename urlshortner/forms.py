from .models import Url
from django import forms

class UrlForm(forms.ModelForm):
    class Meta:
        model = Url
        fields = {'original_link'}
        widgets = {
            'original_link': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the link to shorten'})
        }