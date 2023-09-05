from django.shortcuts import redirect, render
from school_app.forms import StudentRegistrationForm, UpdateStudentForm
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
            form.save()
            return redirect("home")
    else:
        form = StudentRegistrationForm()
        
    return render(request, "school_app/student_form.html", {"form": form})

def view_student_details(request, pk):
    student = Student.objects.get(pk=pk)
    context = {"student": student}
    return render(request, "school_app/student_details.html", context=context)

def update_student_details(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UpdateStudentForm(instance=student)
    
    context = {"student": student, "form": form}
    return render(request, 'school_app/update_student_form.html', context=context)

def user_login(request):
    return render(request, "school_app/user_login.html") 