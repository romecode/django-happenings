# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('happenings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='banner',
            field=mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Banner image', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='description_short',
            field=mezzanine.core.fields.RichTextField(verbose_name='Short description', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=mezzanine.core.fields.FileField(max_length=255, null=True, verbose_name='Event image', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=mezzanine.core.fields.RichTextField(verbose_name='Main description', blank=True),
        ),
    ]
