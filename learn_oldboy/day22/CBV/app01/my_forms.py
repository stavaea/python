


from django import forms


class DemoForm(forms.Form):
    name=forms.CharField()
    age=forms.IntegerField()
    email=forms.EmailField()