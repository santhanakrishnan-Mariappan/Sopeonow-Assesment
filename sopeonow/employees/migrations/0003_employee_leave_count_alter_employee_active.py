# Generated by Django 4.1.4 on 2022-12-18 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0002_alter_employee_dp'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Leave_count',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Active',
            field=models.BooleanField(default=True),
        ),
    ]
