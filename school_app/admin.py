from django.contrib import admin

from school_app.models import Student

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
  list_display = ["first_name", "last_name", "id_number"]
  list_per_page = 10
  search_fields = ["id_number"]

admin.site.register(Student, StudentAdmin)