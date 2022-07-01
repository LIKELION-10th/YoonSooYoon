from django import forms
from .models import Geust

class GeustModelForm(forms.ModelForm):
    class Meta:
        model = Geust
        fields = ['nickname', 'body']