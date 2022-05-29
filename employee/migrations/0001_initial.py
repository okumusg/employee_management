# Generated by Django 3.2.13 on 2022-05-29 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(help_text='Unique id for an employee which consist of char and number', max_length=30, unique=True, verbose_name='Employee ID')),
                ('name', models.CharField(help_text='Full name of the employee', max_length=255, verbose_name='Name')),
                ('hourly_rate', models.DecimalField(blank=True, decimal_places=2, help_text='Hourly rate of an employee', max_digits=8, null=True, verbose_name='Hourly rate')),
                ('date_joined', models.DateTimeField(auto_now_add=True, help_text="Employee's entry date to company", verbose_name='Date joined')),
            ],
            options={
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the team', max_length=255, verbose_name='Team name')),
                ('is_active', models.BooleanField(default=True, help_text='Is the team is active or passive?', verbose_name='Is the team active?')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('members', models.ManyToManyField(blank=True, related_name='team_member', to='employee.Employee', verbose_name='Team members')),
            ],
            options={
                'ordering': ['-creation_time'],
            },
        ),
        migrations.CreateModel(
            name='WorkArrangement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employment_type', models.CharField(choices=[('FULL_TIME', 'Full time'), ('PART_TIME', 'Part time')], default='FULL_TIME', help_text='Is employee working full or part time?', max_length=10, verbose_name='Employment type')),
                ('weekly_work_hours', models.PositiveSmallIntegerField(default=40, help_text='Total work hours in a week', verbose_name='Weekly work hours')),
            ],
        ),
        migrations.CreateModel(
            name='TeamLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leader', models.OneToOneField(help_text='The employee which leads the team', on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='employee.employee', verbose_name='Team leader')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='employee.team', verbose_name='Team')),
            ],
        ),
        migrations.CreateModel(
            name='TeamEmployee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(help_text='The employee which is the member of a team', on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='employee.employee', verbose_name='Team member')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_members', to='employee.team', verbose_name='Team')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(help_text='The employee who has this work contract.', on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='employee.employee', verbose_name='Employee')),
                ('work_arrangement', models.ForeignKey(help_text='The employee who has this work contract.', on_delete=django.db.models.deletion.CASCADE, related_name='contracts', to='employee.workarrangement', verbose_name='Work arrangement')),
            ],
            options={
                'ordering': ['-creation_time'],
            },
        ),
    ]