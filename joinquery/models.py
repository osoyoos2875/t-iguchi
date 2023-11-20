from django.db import models

# Register your models here
class Department(models.Model):
    deptid = models.CharField(max_length=16)
    deptname = models.CharField(max_length=64)
    upperdeptid = models.CharField(max_length=16)
    def __str__(self):
        return self.deptname

class Employee(models.Model):
    empid = models.CharField(max_length=16)
    empname = models.CharField(max_length=64)
    deptid = models.CharField(max_length=16)
    mailaddress = models.CharField(max_length=128)
    def __str__(self):
        return self.empname
