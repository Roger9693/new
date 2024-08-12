from django import forms

class Contact_forms(forms.Form):
    name= forms.CharField(label='name',max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea,label='message')