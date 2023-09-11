from django.db import models

# Create your models here.

class CommonFields(models.Model):
    GENDER = [
        ("Male", "Male"),
        ("Female", "Female")
    ]

    first_name = models.CharField(max_length=100)

    # This field has not been migrated yet
    # middle_name = models.CharField(max_length=100)
    #################################################
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=13)
    gender = models.CharField(null=True, max_length=6, choices=GENDER)

    # Newly added fields, no migrations yet
    # address = models.CharField(max_length=100)
    # suburb = models.CharField(max_length=50)
    # city = models.CharField(max_length=50)
    # province = models.CharField(max_length=50)
    # postal_code = models.CharField(min_length=4, max_length=4)

    class Meta:
        abstract = True

class Student(CommonFields):

    RELATIONSHIP = [
        ("Father", "Father"),
        ("Mother", "Mother"),
        ("Guardian", "Guardian"),
    ]

    #Newly added fields not common to teachers
    #Fields not migrated to DB yet
    parent_name = models.CharField(max_length=100, null=True)
    parent_rel_to_student = models.CharField(verbose_name="Relationship", max_length=8, null=True, choices=RELATIONSHIP) #might need to figure out how make this a select / it worked 
    contact_number = models.CharField(verbose_name="Contact", max_length=10, null=True) # validation for numbers only
    email = models.CharField(max_length=100, null=True) # validation for numbers only

    #Emergency contact
    # emergency_contact_person = models.CharField(max_length=100)
    # relationship = models.CharField(max_length=50) #might need to figure out how make this a select 
    # contact_number = models.CharField(max_length=10) # validation for numbers only
    # email = models.CharField(max_length=10) # validation for valid email

    # enrollment_date = models.DateField(auto_now_add=True)
    # grade = models.CharField(max_length=2) #make this a choice of available grades
    # previous_school = models.CharField(max_length=100, null=True)
    
    def __str__(self):
        return self.first_name