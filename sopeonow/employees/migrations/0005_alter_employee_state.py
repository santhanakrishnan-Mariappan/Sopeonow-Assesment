# Generated by Django 4.1.4 on 2022-12-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0004_alter_employee_on_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='State',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
