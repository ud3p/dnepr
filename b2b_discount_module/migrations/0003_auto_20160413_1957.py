# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('b2b_discount_module', '0002_auto_20160413_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_name',
        ),
        migrations.AddField(
            model_name='country',
            name='country_disp',
            field=models.CharField(help_text=b'This field fill automatically!', max_length=255, null=True, verbose_name=b'Country Name', blank=True),
            preserve_default=True,
        ),
    ]
