# Generated by Django 4.1.4 on 2022-12-21 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_alter_employee_dob_alter_employee_doj'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.DateField(default=datetime.date(2022, 12, 21)),
        ),
        migrations.AlterField(
            model_name='employee',
            name='DOJ',
            field=models.DateField(default=datetime.date(2022, 12, 21)),
        ),
    ]