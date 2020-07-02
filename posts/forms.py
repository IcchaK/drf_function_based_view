from django.forms import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )