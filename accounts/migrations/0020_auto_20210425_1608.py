# Generated by Django 3.2 on 2021-04-25 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20210425_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='record',
            name='user',
        ),
        migrations.AlterField(
            model_name='record',
            name='comment',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='record',
            name='survey',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.survey'),
        ),
    ]
