# Generated by Django 3.2 on 2021-04-25 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20210425_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='osat',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='permission_to_contact',
        ),
        migrations.RemoveField(
            model_name='survey',
            name='rsn_for_score',
        ),
    ]