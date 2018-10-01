from django import forms
from .models import Publicidad

class PostForm(forms.ModelForm):
    class Meta:
        model = Publicidad
        fields = ('titulo', 'texto',)
