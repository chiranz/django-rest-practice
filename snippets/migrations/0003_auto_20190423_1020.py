# Generated by Django 2.1.5 on 2019-04-23 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_auto_20190423_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='snippet',
            old_name='titles',
            new_name='title',
        ),
    ]
