# Generated by Django 5.0.3 on 2024-03-10 11:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_edit_employees_date_of_birth_data_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="personalinformation",
            name="employee",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="personal_information",
                to="api.employee",
            ),
        ),
        migrations.AlterField(
            model_name="workinformation",
            name="employee",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="work_information",
                to="api.employee",
            ),
        ),
    ]
