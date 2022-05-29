from rest_framework import viewsets, permissions
from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement, Contract
from .serializers import EmployeeSerializer, TeamSerializer, TeamEmployeeSerializer, TeamLeaderSerializer, \
    WorkArrangementSerializer, ContractSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all teams
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamEmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for all team employees
    """
    queryset = TeamEmployee.objects.all()
    serializer_class = TeamEmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamLeaderViewSet(viewsets.ModelViewSet):
    """
    API endpoint for team leaders
    """
    queryset = TeamLeader.objects.all()
    serializer_class = TeamLeaderSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkArrangementViewSet(viewsets.ModelViewSet):
    """
    API endpoint for work arrangements
    """
    queryset = WorkArrangement.objects.all()
    serializer_class = WorkArrangementSerializer
    permission_classes = [permissions.IsAuthenticated]


class ContractViewSet(viewsets.ModelViewSet):
    """
    API endpoint for contracts
    """
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    permission_classes = [permissions.IsAuthenticated]
