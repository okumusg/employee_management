from decimal import Decimal

from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import *


class Employee(models.Model):
    """
    Employee model:
        It will contain basic information about our employees.
    """
    employee_id = models.CharField(verbose_name=_("Employee ID"),
                                   max_length=30,
                                   unique=True,
                                   help_text=_("Unique id for an employee which consist of char and number"))
    name = models.CharField(verbose_name=_("Name"),
                            max_length=255,
                            help_text=_("Full name of the employee"))
    hourly_rate = models.DecimalField(verbose_name=_("Hourly rate"),
                                      max_digits=8,
                                      decimal_places=2,
                                      null=True, blank=True,
                                      help_text=_("Hourly rate of an employee"))
    date_joined = models.DateTimeField(verbose_name=_("Date joined"),
                                       auto_now_add=True,
                                       help_text=_("Employee's entry date to company"))

    def __str__(self):
        return self.name

    def get_hourly_rate(self):
        return self.hourly_rate

    def is_team_leader(self):
        # Check if the employee is a team leader in one of the teams
        return hasattr(self, 'team_leader')

    def get_total_monthly_payment(self):
        """
        Calculate the monthly payment of an employee. We should consider that there will
        be several contracts for an employee.
        """
        payments = [contract.calculate_monthly_payment() for contract in self.contracts.all() if
                    self.contracts.all().exists()]
        print(payments)
        return sum(payments)

    class Meta:
        ordering = ['-date_joined']


class Team(models.Model):
    """
    Team model:
        It will contain basic information about our teams.
    """
    name = models.CharField(verbose_name=_("Team name"),
                            max_length=255,
                            help_text=_("Name of the team"))
    is_active = models.BooleanField(verbose_name=_("Is the team active?"),
                                    default=True,
                                    help_text=_("Is the team is active or passive?"))
    creation_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-creation_time']


class TeamEmployee(models.Model):
    team = models.ForeignKey(Team,
                             verbose_name=_("Team"),
                             on_delete=models.CASCADE,
                             related_name='team_members')
    member = models.ForeignKey(Employee,
                               verbose_name=_("Team member"),
                               on_delete=models.CASCADE,
                               related_name='team_members',
                               help_text=_("The employee which is the member of a team"))

    def __str__(self):
        return f"{self.member} member of team ->{self.team}"


class TeamLeader(models.Model):
    team = models.OneToOneField(Team,
                                verbose_name=_("Team"),
                                on_delete=models.CASCADE,
                                related_name='team_leader')
    leader = models.OneToOneField(Employee,
                                  verbose_name=_("Team leader"),
                                  on_delete=models.CASCADE,
                                  related_name='team_leader',
                                  help_text=_("The employee which leads the team"))

    def __str__(self):
        return f"{self.leader} leader of team ->{self.team}"


class WorkArrangement(models.Model):
    employment_type = models.CharField(verbose_name=_("Employment type"),
                                       max_length=10,
                                       choices=EMPLOYMENT_TYPES,
                                       default=FULL_TIME,
                                       help_text=_("Is employee working full or part time?"))
    weekly_work_hours = models.PositiveSmallIntegerField(verbose_name=_("Weekly work hours"),
                                                         default=40,
                                                         help_text=_("Total work hours in a week"))

    def __str__(self):
        return f"{self.employment_type}/{self.weekly_work_hours} hours in a week."

    def get_monthly_work_hours(self):
        return WEEK_COUNT_IN_MONTH * self.weekly_work_hours


class Contract(models.Model):
    """
    We will save the employee's contract information in this model.
    """
    employee = models.ForeignKey(Employee,
                                 verbose_name=_("Employee"),
                                 on_delete=models.CASCADE,
                                 related_name='contracts',
                                 help_text=_("The employee who has this work contract."))
    work_arrangement = models.ForeignKey(WorkArrangement,
                                         verbose_name=_("Work arrangement"),
                                         on_delete=models.CASCADE,
                                         related_name='contracts',
                                         help_text=_("The work arrangement for this contract."))
    creation_time = models.DateTimeField(auto_now_add=True)

    def _pre_calculate_monthly_payment(self) -> Decimal:
        return self.work_arrangement.get_monthly_work_hours() * self.employee.get_hourly_rate()

    def _team_leader_increase(self):
        """
        Adding additonal payment percentage for team leaders
        """
        monthly_payment = self._pre_calculate_monthly_payment()
        return monthly_payment + (monthly_payment * Decimal(TEAM_LEADER_INCREASE_PERCENTAGE / 100))

    def calculate_monthly_payment(self) -> Decimal:
        """
        Returning monthly payment for an employee based on his/her contract.
        """
        if self.employee.is_team_leader():
            return self._team_leader_increase()
        return self._pre_calculate_monthly_payment()

    def __str__(self):
        return f"{self.employee} - work contract"

    class Meta:
        ordering = ['-creation_time']
