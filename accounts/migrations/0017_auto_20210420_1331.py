# Generated by Django 3.2 on 2021-04-20 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_alter_customer_org'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='id',
        ),
        migrations.AddField(
            model_name='record',
            name='surveyid',
            field=models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='Survey ID'),
        ),
    ]
