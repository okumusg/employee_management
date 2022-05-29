from django.utils.translation import ugettext_lazy as _

FULL_TIME = 'FULL_TIME'
PART_TIME = 'PART_TIME'
EMPLOYMENT_TYPES = [
    (FULL_TIME, _("Full time")),
    (PART_TIME, _("Part time")),
]

WEEK_COUNT_IN_MONTH = 4
TEAM_LEADER_INCREASE_PERCENTAGE = 10
