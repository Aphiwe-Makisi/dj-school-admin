# Generated by Django 4.2.4 on 2023-09-09 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("school_app", "0004_student_relationship_alter_student_gender"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="relationship",
            new_name="parent_rel_to_student",
        ),
        migrations.AddField(
            model_name="student",
            name="contact_number",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="student",
            name="parent_name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]