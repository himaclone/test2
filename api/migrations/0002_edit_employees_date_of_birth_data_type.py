# Generated by Django 5.0.3 on 2024-03-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_create_employees_and_informations"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="date_of_birth",
            field=models.DateField(),
        ),
    ]
