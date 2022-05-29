from rest_framework import serializers
from .models import Employee, Team, TeamEmployee, TeamLeader, WorkArrangement, Contract


class EmployeeSerializer(serializers.ModelSerializer):
    total_monthly_payment = serializers.SerializerMethodField()

    def get_total_monthly_payment(self, employee_obj):
        return employee_obj.get_total_monthly_payment()

    class Meta:
        model = Employee
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"


class TeamEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamEmployee
        fields = "__all__"


class TeamLeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamLeader
        fields = "__all__"


class WorkArrangementSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkArrangement
        fields = "__all__"


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
