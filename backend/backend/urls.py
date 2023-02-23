
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from TaskDashboard import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/<int:pk>',views.CourseTasksView.as_view({'get':'list'})),
    path('courses',views.CoursesView.as_view({'get':'list'})),
    path('login',views.StudentDetails.as_view()),
    path('order',views.order_id.as_view())
]
