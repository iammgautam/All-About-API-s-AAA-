from django import forms

class IndexForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label = 'e-Mail')
    subject = forms.CharField(required=False)
    body = forms.CharField(widget = forms.Textarea)