from django import forms
from .models import Snippet


class ContactForm(forms.Form):
    name = forms.CharField(initial='', label='名前', required=False,)
    email = forms.EmailField(initial='', label='メールアドレス', required=False,)
    comment = forms.CharField(widget=forms.Textarea())

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('name', 'email', 'comment')
