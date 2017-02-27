from django import forms

class Registration(forms.Form):
    username = forms.CharField(max_length=200)
    classname = forms.CharField(max_length=200)
    phone = forms.IntegerField()
