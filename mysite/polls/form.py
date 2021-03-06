from django import forms

from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('title', 'text',)