# Generated by Django 3.2 on 2021-04-25 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20210425_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='permission_to_contact',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='rsn_for_score',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
