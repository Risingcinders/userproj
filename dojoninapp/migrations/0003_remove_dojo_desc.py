# Generated by Django 2.2.4 on 2020-10-07 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojoninapp', '0002_dojo_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dojo',
            name='desc',
        ),
    ]