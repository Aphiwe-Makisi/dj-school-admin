from django import forms

class StudentRegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    id_number = forms.CharField(min_length=13, max_length=13)
