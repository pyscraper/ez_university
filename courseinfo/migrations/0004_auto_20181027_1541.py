# Generated by Django 2.1.1 on 2018-10-27 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0003_auto_20180923_1539'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together=set(),
        ),
    ]
