from django.urls import path, include
from rest_framework import routers

import employee.views as employee_views

app_name = 'employee'

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'employees', employee_views.EmployeeViewSet)
router.register(r'teams', employee_views.TeamViewSet)
router.register(r'team-employees', employee_views.TeamEmployeeViewSet)
router.register(r'team-leaders', employee_views.TeamLeaderViewSet)
router.register(r'work-arrangements', employee_views.WorkArrangementViewSet)
router.register(r'contracts', employee_views.ContractViewSet)

urlpatterns = [
    path('', include(router.urls))
]
