# Generated by Django 4.1.5 on 2023-01-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_userlibrary_status_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlibrary',
            name='status_value',
            field=models.IntegerField(default=0),
        ),
    ]
