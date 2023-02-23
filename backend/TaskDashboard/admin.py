from django.contrib import admin
from django.db import models
from .models import Courses,CoursesTasks,StudentsProfile
# Register your models here.
mymodels = [Courses,CoursesTasks,StudentsProfile]
admin.site.register(mymodels)