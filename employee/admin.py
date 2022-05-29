from django.contrib import admin

from .models import Team, TeamLeader, TeamEmployee, WorkArrangement, Contract, Employee

admin.site.register(Team)
admin.site.register(TeamLeader)
admin.site.register(TeamEmployee)
admin.site.register(WorkArrangement)
admin.site.register(Contract)
admin.site.register(Employee)
