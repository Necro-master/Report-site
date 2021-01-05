from django import forms
from .models import Url_data

class UrlForm(forms.Form):
    OPTIONS = (
        (0, 'позитив'),
        (1, 'негатив'),
    )
    tone = forms.ChoiceField(choices=OPTIONS)