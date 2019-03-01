from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('picture', )
        widgets = {
            'picture': forms.ClearableFileInput(attrs={'multiple': True,'style': 'display: none;'})
        }
