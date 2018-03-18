from django import forms

class login(forms.Form):
    user_id = forms.CharField(label='Login id', max_length=100)
    user_pwd = forms.CharField(label='Password', max_length=10)