# Generated by Django 3.2 on 2021-04-17 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_records_surveys'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Records',
            new_name='Record',
        ),
        migrations.RenameModel(
            old_name='Surveys',
            new_name='Survey',
        ),
    ]
