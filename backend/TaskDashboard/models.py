from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Courses(models.Model):
    Course_Name = models.CharField(max_length=100)
    Course_Duration = models.IntegerField(default=0)
    Total_Tasks = models.IntegerField(default=0)
    
    def __str__(self):
        return self.Course_Name
    class Meta:
        db_table = "Training-Courses"

class CoursesTasks(models.Model):
    Course_Name = models.ForeignKey(Courses,related_name="courses",on_delete=models.CASCADE)
    Task_No = models.IntegerField(default=0)
    Task_Content = models.CharField(max_length=255)

    def __str__(self):
        Result="{} Task-{}".format(self.Course_Name,self.Task_No)
        return Result
    class Meta:
        db_table = "Courses-Tasks"

class StudentsProfile(models.Model):
    Username = models.ForeignKey(User,on_delete=models.CASCADE)   
    Course = models.ForeignKey(Courses,on_delete=models.CASCADE)
    Name = models.CharField(max_length=200,default="")
    College_Name = models.CharField(max_length=200,default="")
    Contact_No = models.BigIntegerField(default=0)
    Certificate_Link = models.CharField(max_length=255,default="")

    def __str__(self):
        return self.Username.username
    class Meta:
        db_table = "Student-Profile"