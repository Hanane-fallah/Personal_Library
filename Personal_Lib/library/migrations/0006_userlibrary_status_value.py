# Generated by Django 4.1.5 on 2023-01-08 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_userlibrary_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlibrary',
            name='status_value',
            field=models.FloatField(default=0),
        ),
    ]