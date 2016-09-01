from django import forms
from .models import PhotoPost

class PhotoForm(forms.ModelForm):
   
   class Meta:
      model = PhotoPost
      fields = ('title','description', 'photographer','producer', 'photo',)
   