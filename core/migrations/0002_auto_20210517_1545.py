# Generated by Django 3.2.3 on 2021-05-17 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='employee',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Employee:'),
        ),
        migrations.AlterField(
            model_name='project',
            name='month',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.projectmonth', verbose_name='Month:'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.projectname', verbose_name='Project:'),
        ),
    ]