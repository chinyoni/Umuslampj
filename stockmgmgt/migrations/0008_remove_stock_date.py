# Generated by Django 2.2.13 on 2020-10-10 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockmgmgt', '0007_stockhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='date',
        ),
    ]
