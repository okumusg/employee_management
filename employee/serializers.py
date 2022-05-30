from rest_framework import serializers
from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement, Contract


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Employee model
    """
    total_monthly_payment = serializers.SerializerMethodField()

    def get_total_monthly_payment(self, employee_obj):
        """Return total monthly payment of an employee"""
        return employee_obj.get_total_monthly_payment()

    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'name', 'hourly_rate', 'date_joined', 'total_monthly_payment']


class TeamSerializer(serializers.ModelSerializer):
    """
    Serializer for Team model
    """

    class Meta:
        model = Team
        fields = ['id', 'name', 'is_active', 'creation_time']


class TeamEmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for TeamEmployee model
    """

    class Meta:
        model = TeamEmployee
        fields = "__all__"


class TeamLeaderSerializer(serializers.ModelSerializer):
    """
    Serializer for TeamLeader model
    """

    class Meta:
        model = TeamLeader
        fields = "__all__"


class WorkArrangementSerializer(serializers.ModelSerializer):
    """
    Serializer for WorkArrangement model
    """

    class Meta:
        model = WorkArrangement
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    """
    Serializer for Contract model
    """

    class Meta:
        model = Contract
        fields = "__all__"
