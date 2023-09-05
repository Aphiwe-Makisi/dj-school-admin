from django import forms

from school_app.models import Student

class StudentRegistrationForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=100)
    # last_name = forms.CharField(max_length=100)
    # id_number = forms.CharField(min_length=13, max_length=13)

    class Meta:
        model = Student
        fields = "__all__"

class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
