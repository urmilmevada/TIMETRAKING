# Generated by Django 4.2 on 2023-04-17 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetracker', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='badge',
            name='project_team',
        ),
        migrations.RemoveField(
            model_name='project_module',
            name='module_estimated_minutes',
        ),
        migrations.RemoveField(
            model_name='project_task',
            name='task_estimated_minutes',
        ),
        migrations.RemoveField(
            model_name='user_task',
            name='status_id',
        ),
        migrations.RemoveField(
            model_name='user_task',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='user_task',
            name='user_id',
        ),
        migrations.AddField(
            model_name='project_module',
            name='module_estimated_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='project_module',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_task',
            name='task_estimated_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='project_task',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_team',
            name='badge',
            field=models.CharField(choices=[('IN', 'InProgress'), ('QF', 'QuickFinisher'), ('LL', 'LazyLoader'), ('SU', 'SilentUser')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user_task',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user_task',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_task'),
        ),
        migrations.AddField(
            model_name='user_task',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='badge',
            name='badge',
            field=models.CharField(choices=[('IN', 'InProgress'), ('QF', 'QuickFinisher'), ('LL', 'LazyLoader'), ('SU', 'SilentUser')], max_length=25, null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='module_completion_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='module_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='module_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='module_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AlterField(
            model_name='project_module',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='module',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_module'),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='priority',
            field=models.CharField(choices=[('High', 'High Priority'), ('Less', 'Less Priority')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='task_description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='task_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project_task',
            name='task_util_minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='project_team',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AlterField(
            model_name='project_team',
            name='team_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project_team',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task_badge',
            name='badge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.badge'),
        ),
        migrations.AlterField(
            model_name='task_badge',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_task'),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_completion_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_decription',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_estimated_hours',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_file',
            field=models.FileField(blank=True, null=True, upload_to='project_files/'),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_technology',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='project_title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='timetracker',
            name='status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Pending', 'Pending'), ('Cancelled', 'Cancelled')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user_task',
            name='user_totalutil_minutes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterModelTable(
            name='timetracker',
            table='timetracker',
        ),
    ]
