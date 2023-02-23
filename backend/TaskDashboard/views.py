from django.shortcuts import redirect
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CourseTaskSerializers,CoursesSerializers
from .models import CoursesTasks,Courses
from django.contrib.auth.models import User

import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
# Create your views here.


class CourseTasksView(viewsets.ModelViewSet):
    serializer_class = CourseTaskSerializers
    def get_queryset(self):
        course = self.kwargs['pk']
        return CoursesTasks.objects.filter(Course_Name = course)

class CoursesView(viewsets.ModelViewSet):
    serializer_class = CoursesSerializers
    def get_queryset(self): 
        response=Courses.objects.all()
        return response
    
class StudentDetails(APIView):
    def post(self,request):
       Email=request.data['email']
       Validate=User.objects.filter(email=Email)
       if len(Validate) == 0:
        response = "You are not registered for any course. Kindly register to login."
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
       else:

        #redirect('dashboard')
        return Response('Login Successful.Redirecting to dashboard', status=status.HTTP_200_OK)


# authorize razorpay client with API Keys.
razorpay_client = razorpay.Client(
    auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

class order_id(APIView):
    def post(self,request):
        currency = 'INR'
        amount = 500
        # Create a Razorpay Order
        razorpay_order = razorpay_client.order.create(dict(amount=amount,currency=currency,payment_capture='0'))
        print(razorpay_order['id']);
        return Response(razorpay_order, status=status.HTTP_200_OK)