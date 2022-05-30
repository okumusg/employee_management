from employee.tests.base_setup import BaseTestSetup

from employee.serializers import EmployeeSerializer, TeamSerializer, TeamEmployeeSerializer, TeamLeaderSerializer, \
    WorkArrangementSerializer, ContractSerializer


class EmployeeModelTest(BaseTestSetup):
    def setUp(self) -> None:
        super(EmployeeModelTest, self).setUp()
        self.employee_serializer = EmployeeSerializer(self.employee1)
        self.team_serializer = TeamSerializer(self.team)
        self.team_employee_serializer = TeamEmployeeSerializer(self.team_employee2)
        self.team_leader_serializer = TeamLeaderSerializer(self.team_leader)
        self.work_arrangement_serializer = WorkArrangementSerializer(self.full_time)
        self.contract_serializer = ContractSerializer(self.contract)

    def test_employee_serializer_contains_expected_fields(self):
        data = self.employee_serializer.data
        fields = ['id', 'employee_id', 'name', 'hourly_rate', 'date_joined', 'total_monthly_payment']
        self.assertEqual(set(data.keys()), set(fields))

    def test_team_serializer_contains_expected_fields(self):
        data = self.team_serializer.data
        fields = ['id', 'name', 'is_active', 'creation_time']
        self.assertEqual(set(data.keys()), set(fields))

    def test_team_employee_serializer_contains_expected_fields(self):
        data = self.team_employee_serializer.data
        fields = ['id', 'team', 'member']
        self.assertEqual(set(data.keys()), set(fields))

    def test_team_leader_serializer_contains_expected_fields(self):
        data = self.team_leader_serializer.data
        fields = ['id', 'team', 'leader']
        self.assertEqual(set(data.keys()), set(fields))

    def test_work_arrangement_serializer_contains_expected_fields(self):
        data = self.work_arrangement_serializer.data
        fields = ['id', 'employment_type', 'weekly_work_hours']
        self.assertEqual(set(data.keys()), set(fields))

    def test_contract_serializer_contains_expected_fields(self):
        data = self.contract_serializer.data
        fields = ['id', 'employee', 'work_arrangement']
        self.assertEqual(set(data.keys()), set(fields))
