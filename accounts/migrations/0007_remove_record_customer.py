# Generated by Django 3.2 on 2021-04-18 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_record_survey_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='customer',
        ),
    ]
