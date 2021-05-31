from django import forms


class UserContactsForm(forms.Form):
    name=forms.CharField(max_length=200)
    email=forms.CharField(max_length=200)
    subject=forms.CharField(max_length=200)
    message=forms.CharField(max_length=500)