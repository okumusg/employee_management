from decimal import Decimal

from employee.constants import WEEK_COUNT_IN_MONTH, TEAM_LEADER_INCREASE_PERCENTAGE
from employee.models import Employee, TeamEmployee, Team, TeamLeader, WorkArrangement, Contract
from employee.tests.base_setup import BaseTestSetup


class EmployeeModelTest(BaseTestSetup):
    def test_employee_representation(self):
        self.assertEquals(self.employee1.__str__(), self.employee1.name)

    def test_employee_id_label(self):
        field_label = Employee._meta.get_field('employee_id').verbose_name
        self.assertEquals(field_label, 'Employee ID')

    def test_name_label(self):
        field_label = Employee._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Name')

    def test_name_hourly_rate(self):
        field_label = Employee._meta.get_field('hourly_rate').verbose_name
        self.assertEquals(field_label, 'Hourly rate')

    def test_name_date_joined(self):
        field_label = Employee._meta.get_field('date_joined').verbose_name
        self.assertEquals(field_label, 'Date joined')

    def test_get_hourly_rate_func(self):
        self.assertEquals(self.employee1.get_hourly_rate(), self.employee1.hourly_rate)

    def test_is_team_leader(self):
        self.assertTrue(self.employee1.is_team_leader())

    def test_get_total_monthly_payment(self):
        """
        Hourly rate -> 10
        Monthly work hours -> 4 * 40 = 160
        Monthly base payment should be -> 160 * 10 = 1600 for employee_1 and employee_2
        %10 percent increase -> 1600 + 160 = 1760 for employee_1
        """
        self.assertAlmostEqual(self.employee1.get_total_monthly_payment(), Decimal(1760))


class TeamModelTest(BaseTestSetup):
    def test_team_representation(self):
        self.assertEquals(self.team.__str__(), self.team.name)

    def test_name_label(self):
        field_label = Team._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'Team name')

    def test_is_active_label(self):
        field_label = Team._meta.get_field('is_active').verbose_name
        self.assertEquals(field_label, 'Is the team active?')


class TeamEmployeeTest(BaseTestSetup):
    def test_team_employee_representation(self):
        self.assertEquals(self.team_employee2.__str__(),
                          f"{self.team_employee2.member} member of team ->{self.team_employee2.team}")

    def test_team_label(self):
        field_label = TeamEmployee._meta.get_field('team').verbose_name
        self.assertEquals(field_label, 'Team')

    def test_member_label(self):
        field = TeamEmployee._meta.get_field('member').verbose_name
        self.assertEquals(field, 'Team member')


class TeamLeaderTest(BaseTestSetup):
    def test_team_leader_representation(self):
        self.assertEquals(self.team_leader.__str__(),
                          f"{self.team_leader.leader} leader of team ->{self.team_leader.team}")

    def test_team_label(self):
        field_label = TeamLeader._meta.get_field('team').verbose_name
        self.assertEquals(field_label, 'Team')

    def test_leader_label(self):
        field = TeamLeader._meta.get_field('leader').verbose_name
        self.assertEquals(field, 'Team leader')


class WorkArrangementTest(BaseTestSetup):
    def test_work_arrangement_representation(self):
        self.assertEquals(self.full_time.__str__(),
                          f"{self.full_time.employment_type}/{self.full_time.weekly_work_hours} hours in a week.")

    def test_employement_type_label(self):
        field_label = WorkArrangement._meta.get_field('employment_type').verbose_name
        self.assertEquals(field_label, 'Employment type')

    def test_weekly_work_hours_label(self):
        field = WorkArrangement._meta.get_field('weekly_work_hours').verbose_name
        self.assertEquals(field, 'Weekly work hours')

    def test_monthly_work_hours(self):
        self.assertEquals(self.full_time.get_monthly_work_hours(),
                          WEEK_COUNT_IN_MONTH * self.full_time.weekly_work_hours)
        self.assertEquals(self.full_time.get_monthly_work_hours(), 160)


class ContractTest(BaseTestSetup):
    def test_contract_representation(self):
        self.assertEquals(self.contract.__str__(),
                          f"{self.contract.employee} - work contract")

    def test_employee_label(self):
        field_label = Contract._meta.get_field('employee').verbose_name
        self.assertEquals(field_label, 'Employee')

    def test_work_arrangement_label(self):
        field_label = Contract._meta.get_field('work_arrangement').verbose_name
        self.assertEquals(field_label, 'Work arrangement')

    def test_pre_calculate_monthly_payment(self):
        """
        Hourly rate -> 10
        Monthly work hours -> 160
        Monthly payment should be -> 1600
        """
        self.assertEquals(self.contract._pre_calculate_monthly_payment(),
                          self.contract.work_arrangement.get_monthly_work_hours() * self.contract.employee.get_hourly_rate())
        self.assertEquals(self.contract._pre_calculate_monthly_payment(), 1600)

    def test_team_leader_increase(self):
        """
        Hourly rate -> 10
        Monthly work hours -> 160
        Monthly payment should be -> 1600
        %10 percent increase -> 1600 + 160 = 1760
        """
        monthly_payment = self.contract._pre_calculate_monthly_payment()
        monthly_payment_with_team_leader_increase = monthly_payment + (
                monthly_payment * Decimal(TEAM_LEADER_INCREASE_PERCENTAGE / 100))

        self.assertAlmostEqual(self.contract._team_leader_increase(),
                               monthly_payment_with_team_leader_increase)
        self.assertAlmostEqual(self.contract._team_leader_increase(), Decimal(1760))

    def test_calculate_monthly_payment(self):
        """
        Hourly rate -> 10
        Monthly work hours -> 4 * 40 = 160
        Monthly base payment should be -> 160 * 10 = 1600 for employee_1 and employee_2
        %10 percent increase -> 1600 + 160 = 1760 for employee_1

        Hourly rate -> 20.2
        Monthly work hours -> 4 * 10 = 40
        Monthly base payment should be -> 40 * 20.2 = 808 for employee_3
        """
        if self.contract.employee.is_team_leader():
            result = self.contract._team_leader_increase()
        else:
            result = self.contract._pre_calculate_monthly_payment()
        self.assertEquals(self.contract.calculate_monthly_payment(), result)
        self.assertAlmostEqual(self.contract.calculate_monthly_payment(), 1760)
        self.assertAlmostEqual(self.contract2.calculate_monthly_payment(), 1600)
        self.assertAlmostEqual(self.contract3.calculate_monthly_payment(), 808)
