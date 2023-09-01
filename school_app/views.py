from django.shortcuts import redirect, render
from school_app.forms import StudentRegistrationForm
from .models import Student

# Create your views here.
def home(request):
    context = {"all_students": Student.objects.all()}
    return render(request, "school_app/home.html", context)

def add_new_student(request):
    # If the method on the form is POST
    if request.method == "POST":
        # Instantiate the form
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            id_number = form.cleaned_data["id_number"]

            Student.objects.create(first_name=first_name, last_name=last_name, id_number=id_number)
            return redirect("/students/")
    else:
        form = StudentRegistrationForm()
        
    return render(request, "school_app/student_form.html", {"form": form})