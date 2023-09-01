from django.shortcuts import redirect, render

from school_app.forms import NameForm

# Create your views here.
def home(request):
    return render(request, "school_app/home.html")