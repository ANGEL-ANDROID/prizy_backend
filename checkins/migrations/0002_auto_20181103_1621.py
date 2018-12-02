# Generated by Django 2.1.2 on 2018-11-03 16:21

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0003_auto_20181101_2117'),
        ('checkins', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='checkin',
            unique_together={('account', 'event')},
        ),
    ]
