from django import forms

class regform(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    phone = forms.IntegerField()
    password = forms.CharField(max_length=20)
    cpassword = forms.CharField(max_length=20)

class logform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=20)

class calform(forms.Form):
    first = forms.FloatField()
    second = forms.FloatField()
    option = forms.CharField(max_length=10)

