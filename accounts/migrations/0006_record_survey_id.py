# Generated by Django 3.2 on 2021-04-18 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210417_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='survey_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
