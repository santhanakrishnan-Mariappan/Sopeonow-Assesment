# Generated by Django 4.1.4 on 2022-12-20 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employee_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DOB',
            field=models.DateTimeField(blank=True),
        ),
    ]
