from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from school_app.forms import StudentRegistrationForm, UpdateStudentForm, UserRegistrationForm
from .models import Student

# - Home page view.
def home(request):
    return render(request, "school_app/home.html")

@login_required(login_url="login")
def get_all_students(request):
    context = {"all_students": Student.objects.all()}
    return render(request, "school_app/student_list.html", context)

# - Add new student
@login_required(login_url="login") # Need to make this work once I have learned authication
def add_new_student(request):
    # If the method on the form is POST
    if request.method == "POST":
        # Instantiate the form
        form = StudentRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentRegistrationForm()
        
    return render(request, "school_app/student_form.html", {"form": form})

# - View individual student details
@login_required(login_url="login")
def view_student_details(request, pk):
    student = Student.objects.get(pk=pk)
    context = {"student": student}
    return render(request, "school_app/student_details.html", context=context)

# - Update exisiting student
@login_required(login_url="login")
def update_student_details(request, pk):
    student = Student.objects.get(pk=pk)

    if request.method == "POST":
        form = UpdateStudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = UpdateStudentForm(instance=student)
    
    context = {"student": student, "form": form}
    return render(request, 'school_app/update_student_form.html', context=context)

# - Delete student from DB
@login_required(login_url="login")
def delete_student(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect("student_list")

################################################################

# - User login
def user_login(request):

    
    if request.method == "POST":
        form = AuthenticationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                # return redirect("student_details")
            else:
                return redirect("login")
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "school_app/user_login_form.html", context=context)

def user_logout(request):
    logout(request)
    # return redirect("login")



# - User registration

def user_registration(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        form.save()
        return redirect("login")

    context = {
        "form": form
    }
    return render(request, "school_app/user_reg_form.html", context=context)