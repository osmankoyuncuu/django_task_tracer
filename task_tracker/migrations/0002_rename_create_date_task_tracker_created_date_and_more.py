# Generated by Django 4.1.4 on 2022-12-27 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_tracker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task_tracker',
            old_name='create_date',
            new_name='created_date',
        ),
        migrations.RenameField(
            model_name='task_tracker',
            old_name='update_date',
            new_name='updated_date',
        ),
    ]