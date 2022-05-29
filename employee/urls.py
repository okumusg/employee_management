from django.urls import path, include
from rest_framework import routers

import employee.views as employee_views

app_name = 'employee'

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'employees', employee_views.EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls))
]