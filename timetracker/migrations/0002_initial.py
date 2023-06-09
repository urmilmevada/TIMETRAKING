# Generated by Django 4.2 on 2023-04-04 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timetracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_task',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='task_badge',
            name='badge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.badge'),
        ),
        migrations.AddField(
            model_name='task_badge',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_task'),
        ),
        migrations.AddField(
            model_name='project_team',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AddField(
            model_name='project_team',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='project_task',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_module'),
        ),
        migrations.AddField(
            model_name='project_task',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AddField(
            model_name='project_task',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.status'),
        ),
        migrations.AddField(
            model_name='project_module',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timetracker.timetracker'),
        ),
        migrations.AddField(
            model_name='project_module',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.status'),
        ),
        migrations.AddField(
            model_name='badge',
            name='project_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetracker.project_team'),
        ),
    ]
