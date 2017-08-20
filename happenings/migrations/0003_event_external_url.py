# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0002_auto_20160622_1812'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='external_url',
            field=models.CharField(max_length=255, verbose_name='external url', blank=True),
        ),
    ]
