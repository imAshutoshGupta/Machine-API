# Generated by Django 4.2.5 on 2023-09-29 07:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_client_uid_alter_project_client_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 29, 12, 33, 59, 981768)),
        ),
    ]
