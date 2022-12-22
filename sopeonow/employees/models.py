from datetime import date
from uuid import uuid4
from django.db.models.signals import post_save, post_init
from django.db import models


# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=100)
    dp = models.FileField(default="default.png")
    DOB = models.DateTimeField()
    DOJ = models.DateField()
    Department = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    Address = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    ZipCode = models.IntegerField()
    State = models.CharField(max_length=100, blank=True, null=True)
    Active = models.BooleanField(default=True)
    Leave_count = models.IntegerField(default=12)
    on_leave = models.BooleanField(default="False")

    def __str__(self):
        return self.Name

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initialLeave__count = self.Leave_count

    def save(self, *args, **kwargs):
        if self.on_leave != self.__initialLeave__count:
            if self.on_leave == True:
                self.on_leave = self.on_leave - 1
        return super().save(*args, **kwargs)

#     def post_save(sender, instance, created, **kwargs):
#         if instance.on_leave.previous_state != instance.on_leave.state:
#             if instance.on_leave == True:
#                 Leave_count = instance.Leave_count - 1
#
# post_save.connect(Employee.post_save, sender=Employee)
