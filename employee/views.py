from rest_framework import viewsets, permissions
from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement, Contract
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for listing all employees
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
