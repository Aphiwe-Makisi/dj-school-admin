from django.shortcuts import redirect, render
from school_app.forms import StudentRegistrationForm, UpdateStudentForm
from .models import Student

# - Home page view.
def home(request):
    context = {"all_students": Student.objects.all()}
    return render(request, "school_app/home.html", context)

# - Add new student
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

# - View individual student details
def view_student_details(request, pk):
    student = Student.objects.get(pk=pk)
    context = {"student": student}
    return render(request, "school_app/student_details.html", context=context)

# - Update exisiting student
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

# - Delete student from DB
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect("home")

################################################################

# - User login
def user_login(request):
    return render(request, "school_app/user_login_form.html") 

# - User registration

def user_registration(request):
    return render(request, "school_app/user_reg_form.html")