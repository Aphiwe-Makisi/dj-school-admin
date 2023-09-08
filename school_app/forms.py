from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from school_app.models import Student

class StudentRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "First name"}), min_length=3, max_length=25)
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Last name"}), min_length=3, max_length=25)
    id_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "ID Number"}), 
        min_length=13, max_length=13,
       validators= [RegexValidator(r'\d+', message="Ensure you only enter digits.")]
    )
    gender = forms.CharField(widget=forms.Select(choices=[("Male", "Male"), ("Female", "Female")]))

    class Meta:
        model = Student
        fields = "__all__"

class UpdateStudentForm(forms.ModelForm):
    
    gender = forms.CharField(widget=forms.Select(choices=[("Male", "Male"), ("Female", "Female")]))
    
    class Meta:
        model = Student
        fields = "__all__"


######################################################################################################
# AUTHENTICATION

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]