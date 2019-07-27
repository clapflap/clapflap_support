from django.contrib import admin
from .models import Snippet
from django import forms

admin.site.register(Snippet)


class SnippetForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':100}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'size':100}))
