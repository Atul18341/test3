from rest_framework import serializers
from .models import CoursesTasks,Courses

class CourseTaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = CoursesTasks
        fields = '__all__'

class CoursesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'