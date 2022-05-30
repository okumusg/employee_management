from django.test import TestCase

from employee.constants import FULL_TIME, PART_TIME
from employee.models import Employee, Team, TeamLeader, TeamEmployee, WorkArrangement, Contract


class BaseTestSetup(TestCase):
    def setUp(self) -> None:
        # Create some employees
        self.employee1_data = {
            "employee_id": "EDI1000",
            "name": "Employee 1",
            "hourly_rate": 10
        }
        self.employee2_data = {
            "employee_id": "EDI1001",
            "name": "Employee 2",
            "hourly_rate": 10
        }
        self.employee3_data = {
            "employee_id": "EDI1002",
            "name": "Employee 3",
            "hourly_rate": 20.2
        }
        self.employee1 = Employee.objects.create(**self.employee1_data)
        self.employee2 = Employee.objects.create(**self.employee2_data)
        self.employee3 = Employee.objects.create(**self.employee3_data)
        # Create a team and add its leader and members
        self.team = Team.objects.create(name='Team 1')

        self.team_leader = TeamLeader.objects.create(team=self.team,
                                                     leader=self.employee1)

        self.team_employee2 = TeamEmployee.objects.create(team=self.team, member=self.employee2)
        self.team_employee3 = TeamEmployee.objects.create(team=self.team, member=self.employee3)

        # Create work arrangements
        self.full_time = WorkArrangement.objects.create(employment_type=FULL_TIME, weekly_work_hours=40)
        self.part_time = WorkArrangement.objects.create(employment_type=PART_TIME, weekly_work_hours=10)

        # Create contracts
        self.contract = Contract.objects.create(employee=self.employee1, work_arrangement=self.full_time)
        self.contract2 = Contract.objects.create(employee=self.employee2, work_arrangement=self.full_time)
        self.contract3 = Contract.objects.create(employee=self.employee3, work_arrangement=self.part_time)
